from process import DASHBOARD_STYLE


def show_hide_content_ctl(selected_tab):
    if selected_tab == "tab-data":
        data_container_style = DASHBOARD_STYLE["data-container"]["style"]
        if "display" in data_container_style:
            data_container_style.pop("display")
        return (
            data_container_style,
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            0,
        )
    elif selected_tab == "tab-data-insight":
        updated_style = {}
        for container_key in [
            "output-container",
            "prompt-container",
            "submit-button",
            "llm-radio",
        ]:
            updated_style[container_key] = DASHBOARD_STYLE[container_key]["style"]
            if "display" in updated_style[container_key]:
                updated_style[container_key].pop("display")
        return [
            {"display": "none"},
            updated_style["output-container"],
            updated_style["prompt-container"],
            updated_style["submit-button"],
            updated_style["llm-radio"],
            0,
        ]
    elif selected_tab == "tab-about":
        return (
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            0,
        )
    else:
        return (
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            0,
        )
