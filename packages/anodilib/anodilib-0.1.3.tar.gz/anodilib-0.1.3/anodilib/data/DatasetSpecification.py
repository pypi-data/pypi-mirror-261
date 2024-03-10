from typing import Callable, Tuple

import pandas as pd

class DatasetSpecification:
    """
    A class used to represent a Dataset and its parsing functionality

    Attributes
    ----------
    dataset_name : str
        the name of the dataset (can be used to load this dataset)
    location : str
        the location of the dataset, can be either an url to location where the dataset can be directly downloaded (e.g. nextcloud download link)
        or a path (which one is automatically detected); if None it will be derived from dataset_name
    delimiter : str
        how the features values are splitted in each line
    label_column : int
        the index of the label column
    is_data_column : Callable[[int], bool]
        a mapping from a columns index to whether this column is one of the data columns which should be used
    columns : list[str]
        a list of column names which are used when using parquet as file type
    skip_header : int
        how many header columns to skip
    skip_footer : int
        how many footer columns to skip
    label_realizations : Tuple[str, str]
        the type of labels for OK (no anomaly) and NOK (anomaly) in the format (OK, NOK); e.g. ("-1", "1") if -1 is no anomaly and 1 is anomaly
    decimal : str
        character for decimal point
    only_first_n_entries : int
        limits the items of the dataset to the first n entries
    predefined_dataset : Tuple[pd.Dataframe, pd.Dataframe]
        the dataset if it should not use the parsing framework (in case the datasets format cannot be captured by the mechanisms)
    """

    def __init__(
        self,
        dataset_name: str,
        location: str,
        delimiter: str,
        label_column: int,
        is_data_column: Callable[[int], bool],
        columns: list[str] = None,
        skip_header: int = 1,
        skip_footer: int = 0,
        label_realizations: Tuple[str, str] = (0, 1),
        decimal: str = ".",
        only_first_n_entries: int = -1,
        predefined_dataset: Tuple[pd.DataFrame, pd.DataFrame] = None,
    ):
        self.dataset_name = dataset_name
        self.location = location
        self.delimiter = delimiter
        self.label_column = label_column
        self.is_data_column = is_data_column
        self.columns = columns
        self.skip_header = skip_header
        self.skip_footer = skip_footer
        self.label_realizations = label_realizations
        self.decimal = decimal
        self.only_first_n_entries = only_first_n_entries
        self.predefined_dataset = predefined_dataset


ECG200_TRAIN = DatasetSpecification(
    dataset_name="ECG200_TRAIN.txt",
    location="https://cloud.fachschaften.org/s/czR7BBLtkrjL8bM/download/ECG200_TRAIN.txt",
    delimiter="  ",
    label_column=0,
    is_data_column=lambda c: c != 0,
    columns=None,
    skip_header=0,
    skip_footer=0,
    label_realizations=[1, -1],
    decimal=".",
    only_first_n_entries=-1,
    predefined_dataset=None,
)
ECG200_TEST = DatasetSpecification(
    dataset_name="ECG200_TEST.txt",
    location="https://cloud.fachschaften.org/s/qR4tc9GsnLG2Qk3/download/ECG200_TEST.txt",
    delimiter="  ",
    label_column=0,
    is_data_column=lambda c: c != 0,
    columns=None,
    skip_header=0,
    skip_footer=0,
    label_realizations=[1, -1],
    decimal=".",
    only_first_n_entries=-1,
    predefined_dataset=None,
)
