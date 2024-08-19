from os.path import join

from pandas import DataFrame, read_excel, read_parquet

from process import DATA_PATH


def read_data(
        data_type: str = "leaft") -> DataFrame:
    """Read input data

    Args:
        data_type (str, optional): data to be used. Defaults to "leaft".

    Returns:
        DataFrame: decoded data
    """
    if data_type == "leaft":
        return read_leaft_data(DATA_PATH["leaft"])

    raise Exception(f"Data type {data_type} is not supported ...")




def read_leaft_data(
    data_path: str,
    data_type: str = "Full. Crop -> Juice -> Final",
    excludes: list = [
        "Water flux",
        "Notes",
        "Flux during concentration",
        "Flux during diafiltration",
        "R.FW.Sep",
        "Membrane",
    ],
    remove_nan: bool = True,
) -> DataFrame:
    """Read data from Leaft

    Args:
        data_path (str): Data path to be read
        data_type (str): e.g., Full. Crop -> Juice -> Final
        excludes (list): e.g.,
        ["Water flux", "Notes", "Flux during concentration", "Flux during diafiltration", "R.FW.Sep", "Membrane]


    Returns:
        DataFrame: Data in pandas format
    """

    df = read_excel(data_path, sheet_name=None, skiprows=0)
    df = {key.rstrip(): value for key, value in df.items()}

    all_df_keys = list(df.keys())

    if data_type not in all_df_keys:
        raise Exception(f"Not able to recognize {data_type} ... from {all_df_keys}")

    df = df[data_type]

    if "Trial" not in df.columns:
        df.columns = df.iloc[0]
        df = df[1:]

    if excludes is not None:
        try:
            df = df.drop(columns=excludes)
        except:
            print(excludes, "not in dataframe")
            print(df.keys())

    if remove_nan:
        df = df.dropna()

    df = df.reset_index(drop=True)

    return df
