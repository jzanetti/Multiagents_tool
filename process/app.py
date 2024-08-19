from dash import Dash
from dash_bootstrap_components import Col, Container, Row
from dash_core_components import Graph, Input, Interval, RadioItems, Tab, Tabs
from dash_html_components import H1, Button, Div

from process import DASHBOARD_STYLE


def create_app():
    app = Dash(__name__)

    app.layout = Container(
        [
            H1(
                "ESR Interative Data Reporting", style=DASHBOARD_STYLE["title"]["style"]
            ),
            Div(
                style=DASHBOARD_STYLE["tab-container"]["style"],
                children=[
                    Tabs(
                        id="tabs",
                        value="tab-data-insight",
                        children=[
                            Tab(
                                label="Data Insights",
                                value="tab-data-insight",
                                style=DASHBOARD_STYLE["tabs"]["style"]["default"],
                                selected_style=DASHBOARD_STYLE["tabs"]["style"][
                                    "selected"
                                ],
                            ),
                            Tab(
                                label="Data",
                                value="tab-data",
                                style=DASHBOARD_STYLE["tabs"]["style"]["default"],
                                selected_style=DASHBOARD_STYLE["tabs"]["style"][
                                    "selected"
                                ],
                            ),
                            Tab(
                                label="About",
                                value="tab-about",
                                style=DASHBOARD_STYLE["tabs"]["style"]["default"],
                                selected_style=DASHBOARD_STYLE["tabs"]["style"][
                                    "selected"
                                ],
                            ),
                        ],
                    )
                ],
            ),
            Div(id="tabs-content"),
            Row(
                [
                    Col(
                        id="data-container",
                        style=DASHBOARD_STYLE["data-container"]["style"].update(
                            {"display": "none"}
                        ),
                    )
                ]
            ),
            Row(
                [
                    Col(
                        [
                            RadioItems(
                                id="llm-radio",
                                options=[
                                    {"label": "CodeLLM + LLM", "value": "use_llm"},
                                    {"label": "CodeLLM", "value": "not_use_llm"},
                                ],
                                value="not_use_llm",
                                labelStyle={"display": "inline-block"},
                                style=DASHBOARD_STYLE["llm-radio"]["style"].update(
                                    {"display": "none"}
                                ),
                            )
                        ],
                    ),
                    Col(
                        id="output-container",
                        width=DASHBOARD_STYLE["output-container"]["width"],
                        style=DASHBOARD_STYLE["output-container"]["style"].update(
                            {"display": "none"}
                        ),
                    ),
                    Col(
                        [
                            Input(
                                id="prompt-container",
                                type="text",
                                placeholder="Enter your prompt:",
                                style=DASHBOARD_STYLE["prompt-container"][
                                    "style"
                                ].update({"display": "none"}),
                            ),
                            Button(
                                id="submit-button",
                                children="Submit",
                                n_clicks=0,
                                style=DASHBOARD_STYLE["submit-button"]["style"].update(
                                    {"display": "none"}
                                ),
                            ),
                        ],
                        width=3,
                    ),
                ],
            ),
            Div(
                id="pandas-instruction-container",
                children=[],  # You can add content here dynamically
                style={"margin-top": "20px"},  # Adjust styling as needed
            ),
        ],
        fluid=True,
    )

    return app
