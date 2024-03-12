"""Anonymizer class"""

import os
import sys
from typing import NoReturn

import pandas as pd

from anonymisation.synthesis import Synthesis
from evaluations.anonymity_evaluation.anonymity_evaluator import AnonymityEvaluator
from evaluations.quality_evaluation.quality_evaluator import QualityEvaluator
from preprocessing.data_processor import DataProcessor


class Anonymizer:
    """
    A class that encapsulates the process of data anonymization through synthesis.
    It utilizes a data processor to load, split, and prepare data and then employs
    a synthesis mechanism to generate an anonymized (synthetic) version of the data.
    """

    def __init__(self, real_data: pd.DataFrame):
        """
        Initializes the Anonymizer with a path to the local data file.

        Args:
            real_data (pd.DataFrame): The dataframe containing the data to be anonymized.
        """
        self.real_data = real_data

    def generate(self) -> NoReturn:
        """
        Executes the anonymization process by first processing the original data to obtain
        real data, original and control datasets, and metadata. Then, it synthesizes
        a synthetic dataset based on the real data and metadata, and saves this synthetic
        dataset to a CSV file.

        The synthetic data is saved to '../data/synthetic_data.csv'.
        """
        # create the report folder
        if not os.path.exists("../report"):
            try:
                os.makedirs("../report")
            except FileExistsError:
                pass

        with open("../report/report.txt", "w", encoding="utf-8") as file:
            # Temporarily redirect stdout to the file
            sys.stdout = file

            # Get the datasets and metadata
            data_processor = DataProcessor(self.real_data)
            ori, control, metadata = data_processor.execute()

            # Generate the synthesized dataset
            synthesis = Synthesis(self.real_data, metadata)
            synthetic_data = synthesis.execute()

            # Synthesis data evaluation
            quality_evaluator = QualityEvaluator(self.real_data, synthetic_data, metadata)
            quality_evaluator.evaluate()

            # Anonymity evaluation
            anonymity_evaluator = AnonymityEvaluator(
                ori=ori, syn=synthetic_data, control=control
            )
            anonymity_evaluator.evaluate()

            # Save the synthetic dataset to a CSV file
            synthetic_data.to_csv("../report/synthetic_data.csv", index=False)

            # Restore stdout to its original state
            sys.stdout = sys.__stdout__


real_data = pd.read_csv("data/Housing.csv")
test = Anonymizer(real_data)
test.generate()
