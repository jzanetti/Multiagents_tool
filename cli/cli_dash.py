# import dash
# import dash_bootstrap_components as dbc
# import dash_core_components as dcc
# import dash_html_components as html
from dash import State
from dash.dependencies import Input, Output

# from process import DASHBOARD_STYLE, LOCAL_MODEL_SETUPS
from process.app import create_app
from process.style.show_hide_content import show_hide_content_ctl
from process.style.show_insight import show_insight
from process.style.show_table import render_table

# from process.utils import create_img, replace_substrings
from process.wrapper import load_data_and_model

# from dash_table import DataTable


# export PYTHONPATH=/home/zhangs/Github/Multiagents_tool
app = create_app()
data_and_model = load_data_and_model()


@app.callback(
    [
        Output("data-container", "style"),
        Output("output-container", "style"),
        Output("prompt-container", "style"),
        Output("submit-button", "style"),
        Output("llm-radio", "style"),
        Output(component_id="submit-button", component_property="n_clicks"),
    ],
    Input("tabs", "value"),
)
def show_hide_content_wrapper(selected_tab):
    return show_hide_content_ctl(selected_tab)


@app.callback(Output("data-container", "children"), Input("tabs", "value"))
def render_content_wrapper(tab):
    return render_table(tab, data_and_model)


@app.callback(
    Output(component_id="llm-radio", component_property="children"),
    Input(component_id="llm-radio", component_property="value"),
    prevent_initial_call=True,
)
def update_llm_ratio_wrapper(llm_flag):
    return llm_flag


@app.callback(
    [
        Output(component_id="output-container", component_property="children"),
        Output(
            component_id="pandas-instruction-container", component_property="children"
        ),
    ],
    Input("tabs", "value"),
    Input(component_id="submit-button", component_property="n_clicks"),
    [
        State(component_id="llm-radio", component_property="value"),
        State(component_id="prompt-container", component_property="value"),
        State(component_id="output-container", component_property="children"),
    ],
    prevent_initial_call=True,
)
def update_output(tab, n_clicks, llm_flag, prompt, current_output):
    return show_insight(tab, n_clicks, llm_flag, prompt, current_output, data_and_model)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
