DATA_PATH = {"leaft": "etc/data/leaft_data_v2.0.xlsx"}


DASHBOARD_STYLE = {
    "title": {
        "style": {
            "color": "#0074D9",  # Blue text color
            "textAlign": "center",  # Center the text
            "padding": "20px",  # Padding around the text
            "backgroundColor": "#1E1E1E",  # Dark background for the header
            "borderRadius": "10px",  # Rounded corners for the header
            "margin": "20px 0",  # Margin above and below the header
            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",  # Shadow effect
        }
    },
    "tab-container": {"style": {"width": "700px", "display": "inline-block"}},
    "tabs": {
        "style": {
            "default": {
                "backgroundColor": "#1E1E1E",  # Dark background for the tab
                "color": "#FFFFFF",  # White text color
                "padding": "10px",  # Padding around the text
                "fontWeight": "bold",  # Bold font weight
                "borderRadius": "5px",  # Rounded corners
                "margin": "5px",  # Margin around each tab
            },
            "selected": {
                "backgroundColor": "#0074D9",  # Blue background for the selected tab
                "color": "#FFFFFF",  # White text color for the selected tab
                "padding": "10px",  # Padding around the text for the selected tab
                "fontWeight": "bold",  # Bold font weight for the selected tab
                "borderRadius": "5px",  # Rounded corners for the selected tab
                "margin": "5px",  # Margin around the selected tab
            },
        },
    },
    "output-container": {
        "width": {"size": 3, "offset": 0},
        "style": {
            "backgroundColor": "white",  # Light grey background
            "borderRadius": "10px",  # Rounded corners
            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.1)",  # Subtle shadow
            "padding": "20px",  # Padding inside the Col
            "margin": "10px 0",  # Vertical margin
            "display": "flex",  # Use flexbox layout
            "flexDirection": "column",  # Stack children vertically
            "justifyContent": "center",  # Center children vertically
            "alignItems": "center",  # Center children horizontally
            "overflowY": "scroll",
            "maxHeight": "500px",
            "minHeight": "500px",
            "border": "1px solid",
        },
    },
    "data-container": {"style": {"display": "none"}},
    "data": {
        "style": {
            "table": {
                "maxHeight": "50vh",
                "overflowY": "scroll",
                "width": "100%",
                "minWidth": "100%",
            },
            "header": {
                "backgroundColor": "#0074D9",
                "color": "white",
                "fontWeight": "bold",
                "textAlign": "center",
                "padding": "15px",
                "border": "1px solid #ddd",
            },
            "cell": {
                "textAlign": "left",
                "padding": "10px",
                "border": "1px solid #ddd",
            },
        },
    },
    "prompt-container": {
        "style": {
            "border": "1px solid",
            "backgroundColor": "#e9e9e9",
            "borderRadius": "10px",
            "padding": "10px",
            "maxHeight": "50px",
            "minHeight": "20px",
            "overflowY": "scroll",
            "boxShadow": "inset 0 1px 3px rgba(0, 0, 0, 0.1)",
            "width": "90%",
            "color": "black",
            "font-size": "15px",
            "margin-top": "20px",
            "margin-bottom": "20px",
            "margin-right": "10px",
        }
    },
    "prompt": {
        "style": {
            "font-family": "Courier",
            "font-size": "20px",
            "color": "blue",
            "text-align": "left",
        }
    },
    "answer": {
        "style": {
            "white-space": "pre-wrap",
            "font-size": "20px",
            "color": "#99ff99",
            "text-align": "right",
        }
    },
    "image": {"style": {"text-align": "right"}},
    "submit-button": {
        "style": {
            "backgroundColor": "#007bff",  # Bootstrap primary button color
            "color": "white",
            "padding": "10px 20px",
            "border": "none",
            "borderRadius": "5px",
            "cursor": "pointer",
            "fontSize": "16px",
            "fontWeight": "bold",
            "outline": "none",
            "boxShadow": "0 2px 2px 0 rgba(0,123,255,.25)",
        },
    },
    "llm-radio": {
        "style": {
            "padding": "20px",
            "border": "1px solid #ddd",
            "borderRadius": "5px",
            "boxShadow": "inset 0 1px 1px rgba(0,0,0,.075)",
            "marginBottom": "10px",
        }
    },
}


LOCAL_MODEL_SETUPS = {
    "embedding_model": {"path": "etc/models/BAAI"},
    "code_model": {"path": "etc/models/CodeLlama-34b-Instruct.gguf"},
    "llm": {
        "path": "etc/models/Meta-Llama-3-8B-Instruct.gguf",
        "prompt_template": "The question is {prompt} The answer as '{response}'. "
        + "Combine the question and answer and give one definte sentence. "
        + "Strickly no extra other texts beyond this sentence.",
    },
}
