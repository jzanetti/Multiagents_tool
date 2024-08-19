import dash_html_components as html

from process import DASHBOARD_STYLE, LOCAL_MODEL_SETUPS
from process.utils import create_img, replace_substrings


def show_insight(tab, n_clicks, llm_flag, prompt, current_output, data_and_model):

    if tab == "tab-data-insight":
        if n_clicks > 0:
            if prompt:
                response = data_and_model["query_engine"].query(prompt)
                pandas_instruction_str = response.metadata["pandas_instruction_str"]
                # plot "PurifiedRCP/JuiceDM" and "R.DM.Sep", and their difference
                if "plot" in pandas_instruction_str.lower():
                    image_src = create_img(
                        data_and_model["data"], pandas_instruction_str
                    )

                    return [
                        html.Div(
                            [
                                current_output,
                                html.P(
                                    f"Q: {prompt}",
                                    style=DASHBOARD_STYLE["prompt"]["style"],
                                ),
                                html.Div(
                                    [html.Img(src=image_src)],
                                    style=DASHBOARD_STYLE["image"]["style"],
                                ),
                            ]
                        ),
                        pandas_instruction_str,
                    ]
                else:
                    if llm_flag == "use_llm":
                        if not prompt.endswith("?"):
                            prompt += "?"

                        llm_tries = 0
                        while True:
                            results = data_and_model["llm_model"](
                                LOCAL_MODEL_SETUPS["llm"]["prompt_template"].format(
                                    prompt=prompt, response=response.response
                                ),
                                max_tokens=100,
                                stop=["\\n", "\n", "."],
                            )["choices"][0]["text"].strip()

                            if len(results) > 0:
                                results = replace_substrings(results, ['"'])
                                break

                            llm_tries += 1
                            print(f"LLM trials: {llm_tries} ...")
                            if llm_tries == 100:
                                break

                    elif llm_flag == "not_use_llm":
                        results = response.response

                    return [
                        html.Div(
                            [
                                current_output,
                                html.P(
                                    f"Q: {prompt}",
                                    style=DASHBOARD_STYLE["prompt"]["style"],
                                ),
                                html.Pre(
                                    results,
                                    style=DASHBOARD_STYLE["answer"]["style"],
                                ),
                            ]
                        ),
                        pandas_instruction_str,
                    ]
            else:
                return [html.Div("Please enter a prompt."), None]
        else:
            return [None, None]
    else:
        return [None, None]
