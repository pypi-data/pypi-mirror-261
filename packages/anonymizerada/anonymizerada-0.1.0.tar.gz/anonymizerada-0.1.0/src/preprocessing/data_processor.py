"""Data preprocessor class"""

from typing import Tuple

import pandas as pd
from sdv.metadata import SingleTableMetadata
from sklearn.model_selection import train_test_split

from preprocessing.get_metadata import generate_metadata


class DataProcessor:
    """
    A class designed to facilitate the processing of data. It automates the tasks of
    loading data from a CSV file, splitting the data into original and control datasets,
    and generating metadata for the original dataset. This class aims to streamline
    the initial steps of data analysis and preparation.
    """

    def __init__(self, real_data: pd.DataFrame):
        """
        Initializes the DataProcessor with a path to the local CSV file.

        Args:
            real_data (pd.DataFrame): The file path to the CSV file containing the data to be processed.
        """
        self.real_data = real_data

    def _load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Loads data from a CSV file, splits it into original and control datasets,
        and generates metadata for the original dataset.

        Args:
            self

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
            A tuple containing the loaded real data, original data, control and data.
        """
        ori, control = train_test_split(self.real_data, test_size=0.20, random_state=42)

        return ori, control

    def execute(
        self,
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, SingleTableMetadata]:
        """
        Executes the data processing workflow. It loads data from a specified CSV file,
        splits this data into original and control datasets, and generates metadata for
        the original dataset.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, SingleTableMetadata]:
            A tuple containing the loaded real data DataFrame,
            the original dataset DataFrame, the control dataset
            DataFrame, and the metadata for the original dataset.
        """
        ori, control = self._load_data()
        metadata = generate_metadata(ori)

        return ori, control, metadata
