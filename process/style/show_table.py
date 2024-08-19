import dash_html_components as html
from dash_table import DataTable

from process import DASHBOARD_STYLE


def render_table(tab, data_and_model):
    if tab == "tab-data":
        return html.Div(
            [
                DataTable(
                    id="table",
                    columns=[
                        {"name": i, "id": i} for i in data_and_model["data"].columns
                    ],
                    data=data_and_model["data"].to_dict("records"),
                    filter_action="native",
                    fill_width=False,
                    style_data=DASHBOARD_STYLE["data"]["style"]["cell"],
                    style_header=DASHBOARD_STYLE["data"]["style"]["header"],
                    style_table=DASHBOARD_STYLE["data"]["style"]["table"],
                ),
            ]
        )
