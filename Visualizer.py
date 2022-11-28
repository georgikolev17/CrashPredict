import folium
import pandas as pd
import geojson


def Visualize(df: pd.DataFrame, pathToGeoJSON: str, pathToSave: str):
    # Reads the GeoJSON and parses into it's respective python structure
    with open(pathToGeoJSON) as f:
        gj = geojson.load(f)
    _features = gj['features']

    # This line changes the internal structure of gj which is a representation of a GeoJSON which is used for both the
    # visualization as well as for the tooltip data
    for fs in _features:
        fs["properties"]["TotalProblem"] = \
            df.loc[df['postalCode'] == fs["properties"]["postalCode"]]["TotalProblem"].values[0]

    m = folium.Map([43, -100], zoom_start=4)
    custom_scale = (df['TotalProblem'].quantile((0, 0.2, 0.4, 0.6, 0.8, 1))).tolist()
    cp = folium.Choropleth(
        geo_data=gj,
        data=df,
        key_on="feature.properties.postalCode",
        columns=["postalCode", "TotalProblem"],
        threshold_scale=custom_scale,
        fill_color="YlGn",
        legend_name="Crash Severity",
        highlight=True
    ).add_to(m)
    folium.LayerControl().add_to(m)

    folium.GeoJsonTooltip(['postalCode', "TotalProblem"], aliases=["postalCode", "Intensity"]).add_to(cp.geojson)
    m.save(pathToSave)
