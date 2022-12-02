import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids

import json
response = open('./data/geojson-counties-fips.json')
counties = json.load(response)

import pandas as pd
df = pd.read_csv("./data/fips-unemp-16.csv", dtype={"fips": str})


def render(app: Dash) -> html.Div:
    fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
    return html.Div(
        dcc.Graph(figure=fig, id=ids.MAP_BOX)
    )



    # @app.callback(
    #     Output(ids.BAR_CHART, "children"),
    #     [
    #         Input(ids.NATION_DROPDOWN, "value"),
    #     ],
    # )
    # def update_bar_chart(nations: list[str]) -> html.Div:
    #     filtered_data = MEDAL_DATA.query("nation in @nations")

    #     if filtered_data.shape[0] == 0:
    #         return html.Div("No data selected.", id=ids.BAR_CHART)

    #     fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")

    #     return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    # return html.Div(id=ids.BAR_CHART)
