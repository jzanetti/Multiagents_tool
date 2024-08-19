from base64 import b64encode
from io import BytesIO

from matplotlib.pyplot import close as plt_close
from pandas import DataFrame


def create_img(df: DataFrame, pandas_instruction_str: str, verbose: bool = True) -> str:
    """Create image and show it on the dashboard

    Args:
        df (DataFrame): input dataframe
        pandas_instruction_str (str): Pandas instrudction
        verbose (bool, optional): debug flag. Defaults to True.

    Returns:
        str: saved data codes
    """
    if verbose:
        print(pandas_instruction_str)
    fig = eval(pandas_instruction_str)

    # Convert the figure to a Dash image using BytesIO
    output_buffer = BytesIO()
    fig.figure.savefig(output_buffer, format="png")  # Access the figure object
    plt_close(fig.figure)
    image_data = output_buffer.getvalue()

    # Convert the image_data to base64
    image_base64 = b64encode(image_data).decode("utf-8")

    # Construct the source URL for the image
    return f"data:image/png;base64,{image_base64}"


def replace_substrings(string, substrings):
    """Removes all occurrences of specified substrings from the given string.

    Args:
        string (str): The original string from which substrings will be removed.
        substrings (list of str): A list of substrings to be removed from the original string.

    Returns:
        str: The modified string with specified substrings removed.
    """
    for substr in substrings:
        string = string.replace(substr, "")
    return string
