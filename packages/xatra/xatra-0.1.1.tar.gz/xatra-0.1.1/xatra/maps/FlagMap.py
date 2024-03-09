import folium
import matplotlib
import geopandas as gpd
from folium.plugins import TimestampedGeoJson
from abc import ABC, abstractmethod
from xatra.utilities import NAME_max, NameSetter
from xatra.data import DataCollection


class Flag:
    """A "Flag" is a declaration that a particular polity (Flag.name) ruled
    over some particular set of features (Flag.matcher), optionally for some
    particular specific period of history (Flag.period).

    Attributes:
        name (str): Name of polity
        matcher (Callable[[Dict], bool]): Function that returns True onn the
            set of features included by the Flag.
        period (tuple[int|float, int|float] | None): tuple of start and end years, for
            dynamic Maps
        ref (str | None): source for claim

    """

    def __init__(self, name, matcher, period=None, ref=None):
        """Constructs a Flag.

        Args:
            name (str): Name of polity
            matcher (Callable[[Dict], bool]): Function that returns True onn the
                set of features included by the Flag.
            period (tuple[int|float, int|float], optional): tuple of start and end years,
                for dynamic Maps
            ref (str, optional): source for claim
        """
        self.name = name
        self.matcher = matcher
        self.period = period
        self.ref = ref

class Map(ABC):
    """Abstract class for Maps: subclass this with custom methods .flag(), .geojson(), and 
    optionally .geojson_rivers, .custom_colors to define a Map.

    Attributes:
        flags (List[Flag]): List of flags
        geojson (List[Dict]): List of features (GeoJSON dicts), loaded from xatra.data
        geojson_rivers (List[Dict]): List of rivers (GeoJSON dicts), loaded from xatra.data
        custom_colors (Dict[str, str]): Dictionary mapping Flag names to custom (not calculated)
            colours. Defaults to {} in which case all colours are calculated.
        breakpoints (List[int|float]): List of years at which territorial changes occur,
            according to self.flags.
        geojson_by_year (Dict[int|float, List[Dict]]): Dict showing for each year, the GeoJSON
            with matching flags appended to each feature.
        color_map (Dict[str, str]): Dict specifying the colour for each flag name.
        options (Dict[str, any]): Dict with keys "color_segments", "location", "zoom_start" : 5,
            "color_legend" : True, "custom_html" : "", "size" : 1.0, "names_on_map" : True
        
    Methods:
        plot: Plot with Folium.
        plot_flags_as_layers: Plot each flag as a separate layer, ignoring year/period.
    
    """
    
    def __init__(self, **kwargs):
        """Initialize map with options.
        
        Args:
            **kwargs: Recognized kwargs follow.

        Keyword Arguments:
            verbose (bool): Print progress? Defaults to False.
            color_segments (int): Flags within this distance of each other in
                self.flags will be assigned contrasting colours (unless forced otherwise
                in self.custom_colors). Defaults to 8.
            location (List[float]): Initial position of Folium map. Defaults to calculated as center
                of geojson, or from std_start.
            zoom_start (int): Initial zoom of Folium map. Defaults to 5, or calculated from std_start.
            std_start (str): A recognized string: "india", "meru", or "brahmavarta". If not recognized, will
                be ignored. Should not be specified with location or zoom; will overrule both of them.
            color_legend (bool): to include a legend of colours? Defaults to True.
            custom_html (str): Custom HTML to be dded to the top of the legend, e.g. a title. Defaults to "".
            size (float): scale of legend. Defaults to 1.0.
            names_on_map (bool): show flag labels on the map? (tooltips will show on hover regardless). Defaults
                to True.

        """ 
        self.verbose = kwargs.get("verbose", False)
        
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Calculating options")
        
        # calculated location from geojson
        gdf = gpd.GeoDataFrame.from_features(self.geojson)
        calculated_location = [
            gdf.geometry.centroid.y.mean(),
            gdf.geometry.centroid.x.mean(),
        ]
        
        # default options
        self.options = {
            "color_segments": 8,
            "location": calculated_location,
            "zoom_start": 5,
            # "std_start" : None,
            "color_legend": True,
            "custom_html": "",
            "size": 1.0,
            "names_on_map": True,
        }
        self.options.update(kwargs)  # update with supplied arguments
        
        # recognized std_starts
        std_start_recog = {
            "india": {"location": [20.5937, 78.9629], "zoom_start": 5},
            "brahmavarta": {"location": [29.9691899, 76.7260054], "zoom_start": 5},
            "meru": {"location": [39, 71.9610313], "zoom_start": 5},
        }

        std_start = kwargs.get("std_start", "NA")  # supplied std_start
        calculated_from_std_start = std_start_recog.get(
            std_start, {}
        )  # calculate location and zoom from this
        self.options.update(calculated_from_std_start)  # update self.options with this

        if self.verbose:
            print(f"Map {self.__class__.__name__}: Calculating cache properties")
        
        # cache properties
        # self.flags = self.flags()
        # self.geojson = self.geojson()
        # self.geojson_rivers = self.geojson_rivers()
        self.breakpoints = self._breakpoints()
        self.geojson_by_year = self._geojson_by_year()
        self._unique_flag_names = self._unique_flag_names()
        self.color_map = self._color_map()
    
    @property
    @abstractmethod
    def flags(self):
        pass
    
    @property
    @abstractmethod
    def geojson(self):
        pass
    
    @property
    @abstractmethod
    def geojson_rivers(self):
        return []
    
    @property
    @abstractmethod
    def custom_colors(self):
        return {}
    
    def _breakpoints(self):
        """Breakpoints at which the map needs to be computed, basically all
        the endpoints of each flag's period in self.flags. NOTE: self.breakpoints == []
        can be used to test if a map is static.

        """
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Calculating breakpoints")
        points = []
        for flag in self.flags:
            if flag.period is not None:
                points.extend(flag.period)
        return sorted(set(points))

    def _geojson_with_flags(self, year=None):
        """self.geojson with list of claiming flags in a particular year
        added to each feature. To be used in self.geojson_by_year

        Args:
            year (int|float, optional): _description_. Defaults to None.

        Returns:
            List[Dict]: List of Dicts where each such dict["properties"] has additional
            keys "flag", "flags", and "NAME_max".

        """
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Calculating geojson with flags for year {year}")
        result = []
        for feature in self.geojson:
            if self.verbose:
                print(f"Map {self.__class__.__name__}: Adding flags to feature {NAME_max(feature)['NAME_n']}")
            feature_copies = []
            matching_flags = [
                flag.name
                for flag in self.flags
                if flag.matcher(feature)
                and (
                    year == None
                    or flag.period is not None
                    or (flag.period[0] <= year < flag.period[1])
                )
            ]
            for flag_name in matching_flags:
                feature_copy = feature.copy()
                feature_copy["properties"]["flag"] = flag_name
                feature_copy["properties"]["flags"] = matching_flags
                feature_copy["properties"]["NAME_max"] = NAME_max(feature_copy)[
                    "NAME_n"
                ]  # for tooltip
                feature_copies.append(feature_copy)
            result.extend(feature_copies)
        return result

    def _geojson_by_year(self):
        """Dict showing for each year, the GeoJSON with matching flags appended to each feature, i.e.
        a dictionary of year : self._geojson_with_flags(year). For a static map it will simply return
        { "static": self._geojson_with_flags() }.

        Returns:
            Dict[int|float|str, List[Dict]]: as described

        """
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Stacking _geojson_with_flags for breakpoint years")
        if self.breakpoints:
            return {year: self._geojson_with_flags(year) for year in self.breakpoints}
        else:
            return {"static": self._geojson_with_flags()}

    def _unique_flag_names(self):
        """List of unique flag names for generating colour map.

        Returns:
            List[str]: List of unique flag names in self.flags.

        """
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Calculating relevant flags")
        # get a list of all relevant flags
        flag_names_from_fby = [
            feature["properties"]["flag"]
            for year, feature_list in self.geojson_by_year.items()
            for feature in feature_list
        ]
        # ^ this would work, but we want them to be in the original order in self.flags,
        # so we can assign a contrasting colour map to it
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Doing a weird thing to maintain original order of flags")
        flag_names = [
            flag.name for flag in self.flags if flag.name in flag_names_from_fby
        ]
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Making unique")
        flag_names = list(dict.fromkeys(flag_names))  # make unique
        return flag_names

    def _color_map(self):
        """Color map, calculated to ensure contrast between Flags that are within
        self.options["color_segments"] of each other in self._unique_flag_names (which is also
        roughly the same as being within that distance in self.flags). Any colors specified
        in self.custom_colors overrides the ones automatically calculated.

        Returns:
            Dict[str, str]: Dict specifying the colour for each flag name.

        """
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Calculating color map")
        flag_names = self._unique_flag_names
        cmap = matplotlib.cm.get_cmap("tab20", len(flag_names))
        color_mapping = {}
        colors_per_segment = max(
            1, cmap.N // self.options["color_segments"]
        )  # Calculate the number of colors per segment

        # Assign colors from different segments to ensure contrast
        for i, flag_name in enumerate(flag_names):
            segment_index = i % self.options["color_segments"]
            color_index = (i // self.options["color_segments"]) % colors_per_segment
            color_position = segment_index * colors_per_segment + color_index
            color = cmap(color_position)[:3]  # Get the RGB part of the color
            color_mapping[flag_name] = matplotlib.colors.rgb2hex(color)

        # custom colors override calculated colors
        for flag_name in color_mapping:
            if flag_name in self.custom_colors:
                color_mapping[flag_name] = self.custom_colors[flag_name]
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Calculated color map")
        
        return color_mapping

    def plot(self, path_out=None):
        """Plot with Folium.

        Args:
            path_out (str, optional): To save the produced HTML somewhere. Defaults to None.

        Returns:
            Folium.Map: Folium Map Object
        """
        
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Plotting")

        m = folium.Map(
            location=self.options["location"], zoom_start=self.options["zoom_start"]
        )

        # add layer for each breakpoint year
        for year, features in self.geojson_by_year.items():
            if self.verbose:
                print(f"Map {self.__class__.__name__}: Adding layer for year {year}")
            layer = folium.FeatureGroup(name=str(year))
            for feature in features:
                if self.verbose:
                    print(f"Map {self.__class__.__name__}: Adding feature {feature['properties']['NAME_max']}")
                layer.add_child(
                    folium.GeoJson(
                        data=feature,
                        name="Flags",
                        style_function=lambda feature: {
                            "fillColor": self.color_map.get(
                                feature["properties"]["flag"], "#808080"
                            ),
                            "color": "black",
                            "weight": 0,
                            "fillOpacity": 0.5,  # for visual overlap transparency
                        },
                        tooltip=folium.GeoJsonTooltip(
                            fields=["NAME_max", "flags"], aliases=["NAME", "Flag"]
                        ),
                    )
                )
            m.add_child(layer)

        # add rivers
        if self.geojson_rivers:
            rivers = folium.FeatureGroup(name="Rivers", show=True)
            for river in self.geojson_rivers:
                if self.verbose:
                    print(f"Map {self.__class__.__name__}: Adding river {river['properties']['river_name']}")
                rivers.add_child(
                    folium.GeoJson(
                        data=river,
                        style_function=lambda x: {
                            "color": "blue",
                            "weight": 2,
                            "fillOpacity": 0,
                        },
                        tooltip=folium.GeoJsonTooltip(fields=["river_name", "id"]),
                    )
                )
            m.add_child(rivers)

        # layer control
        folium.LayerControl().add_to(m)

        if self.options["color_legend"]:
            legend_html = (
                '<div style="position: fixed; bottom: 50px; left: 50px; width: 150px; height: {}px; background-color: white; border:2px solid grey; z-index:9999; font-size:14px;">'
                "&nbsp; <b>Legend</b> <br>".format(
                    25 + len(self._unique_flag_names) * 20
                )
            )
            for flag, color in self.color_map.items():
                legend_html += '&nbsp; <i style="background:{}; width: 15px; height: 15px; float: left; margin-right: 5px;"></i>{}<br>'.format(
                    color, flag
                )
            legend_html += "</div>"
            m.get_root().html.add_child(folium.Element(legend_html))

        if self.verbose:
            print(f"Map {self.__class__.__name__}: Saving to {path_out}")
        if path_out:
            m.save(path_out)
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Done")

        return m

    def plot_flags_as_layers(self, show_by_default=None, path_out=None):
        """Plot each flag as a separate layer, ignoring year/period.

        Args:
            show_by_default (List[str] | None, optional): List of flag names to show by default. If None, all flags. Defaults to None.
            path_out (str, optional): To save the produced HTML somewhere. Defaults to None.
        """
        features_list = self._geojson_with_flags(year=None)
        if show_by_default is None:
            show_by_default = self._unique_flag_names

        m = folium.Map(
            location=self.options["location"], zoom_start=self.options["zoom_start"]
        )

        # add layer for each relevant flag
        for flag in self.flags:
            if flag.name in self._unique_flag_names:  # relevant flags only
                if self.verbose:
                    print(f"Map {self.__class__.__name__}: Adding layer for flag {flag.name}")
                layer = folium.FeatureGroup(
                    name=flag.name, show=flag.name in show_by_default
                )
                for feature in features_list:
                    if feature["properties"]["flag"] == flag.name:
                        if self.verbose:
                            print(f"Map {self.__class__.__name__}: Adding feature {feature['properties']['NAME_max']}")
                        layer.add_child(
                            folium.GeoJson(
                                data=feature,
                                name="Flags",
                                style_function=lambda feature: {
                                    "fillColor": self.color_map.get(
                                        feature["properties"]["flag"], "#808080"
                                    ),
                                    "color": "black",
                                    "weight": 0,
                                    "fillOpacity": 0.5,  # for visual overlap transparency
                                },
                                tooltip=folium.GeoJsonTooltip(
                                    fields=["NAME_max", "flags"],
                                    aliases=["NAME", "Flag"],
                                ),
                            )
                        )
                m.add_child(layer)

        # add rivers
        if self.geojson_rivers:
            rivers = folium.FeatureGroup(name="Rivers", show=True)
            for river in self.geojson_rivers:
                if self.verbose:
                    print(f"Map {self.__class__.__name__}: Adding river {river['properties']['river_name']}")
                rivers.add_child(
                    folium.GeoJson(
                        data=river,
                        style_function=lambda x: {
                            "color": "blue",
                            "weight": 2,
                            "fillOpacity": 0,
                        },
                        tooltip=folium.GeoJsonTooltip(fields=["river_name", "id"]),
                    )
                )
            m.add_child(rivers)

        # layer control
        folium.LayerControl().add_to(m)

        if self.options["color_legend"]:
            legend_html = (
                '<div style="position: fixed; bottom: 50px; left: 50px; width: 150px; height: {}px; background-color: white; border:2px solid grey; z-index:9999; font-size:14px;">'
                "&nbsp; <b>Legend</b> <br>".format(
                    25 + len(self._unique_flag_names) * 20
                )
            )
            for flag, color in self.color_map.items():
                legend_html += '&nbsp; <i style="background:{}; width: 15px; height: 15px; float: left; margin-right: 5px;"></i>{}<br>'.format(
                    color, flag
                )
            legend_html += "</div>"
            m.get_root().html.add_child(folium.Element(legend_html))

        if self.verbose:
            print(f"Map {self.__class__.__name__}: Saving to {path_out}")
        if path_out:
            m.save(path_out)
        if self.verbose:
            print(f"Map {self.__class__.__name__}: Done")

        return m