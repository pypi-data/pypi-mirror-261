""" Quality Evaluator Module"""

import os

import pandas as pd
from sdv.evaluation.single_table import evaluate_quality, run_diagnostic


class QualityEvaluator:
    """
    A class to evaluate the quality of synthetic data compared to real data
    using SDV's evaluation metrics. It generates diagnostic and quality reports
    for the data.
    """

    def __init__(
        self,
        real_data: pd.DataFrame,
        synthetic_data: pd.DataFrame,
        metadata: pd.DataFrame,
    ) -> None:
        """
        Initializes the QualityEvaluator with real and synthetic datasets and metadata.

        Parameters:
        - real_data: The original dataset used for comparison.
        - synthetic_data: The synthetic dataset generated to mimic the real dataset.
        - metadata: Metadata related to the datasets, used for evaluation.
        """
        self.real_data = real_data
        self.synthetic_data = synthetic_data
        self.metadata = metadata

    def diagnostic_report(self) -> None:
        """
        Generates and saves a diagnostic report comparing real and synthetic data,
        focusing on data validity and structure.
        """
        print("// Diagnostic report // \n")

        diagnostic_report = run_diagnostic(
            real_data=self.real_data,
            synthetic_data=self.synthetic_data,
            metadata=self.metadata,
        )

        # Data Validity
        diagnostic_report.get_details(property_name="Data Validity")
        fig_data_validity = diagnostic_report.get_visualization(
            property_name="Data Validity"
        )
        fig_data_validity.write_image(
            os.path.join("..", "report", "data_quality_evaluation", "data_validity.png")
        )

        # Data Structure
        diagnostic_report.get_details(property_name="Data Structure")

        diagnostic_report.save(
            filepath=os.path.join(
                "..", "report", "data_quality_evaluation", "diagnostic_report.pkl"
            )
        )

        print("\n\n")

    def quality_report(self) -> None:
        """
        Generates and saves a quality report assessing the synthetic data's quality
        in terms of column shapes and column pair trends.
        """
        print("// Quality report // \n")

        quality_report = evaluate_quality(
            real_data=self.real_data,
            synthetic_data=self.synthetic_data,
            metadata=self.metadata,
        )

        # Column Shapes
        quality_report.get_details(property_name="Column Shapes")
        fig_column_shapes = quality_report.get_visualization(
            property_name="Column Shapes"
        )
        fig_column_shapes.write_image(
            os.path.join("..", "report", "data_quality_evaluation", "column_shapes.png")
        )

        # Column Pair Trends
        quality_report.get_details(property_name="Column Pair Trends")
        fig_column_pair_trends = quality_report.get_visualization(
            property_name="Column Pair Trends"
        )
        fig_column_pair_trends.write_image(
            os.path.join(
                "..", "report", "data_quality_evaluation", "column_pair_trends.png"
            )
        )

        quality_report.save(
            filepath=os.path.join(
                "..", "report", "data_quality_evaluation", "quality_report.pkl"
            )
        )

        print("\n\n")

    def evaluate(self) -> None:
        """
        Evaluates the quality of synthetic data by generating diagnostic and quality reports,
        ensuring the report directory exists or is created.
        """
        report_path = os.path.join("..", "report", "data_quality_evaluation")
        if not os.path.exists(report_path):
            try:
                os.makedirs(report_path)
            except FileExistsError:
                pass

        print("//// Data quality evaluation //// \n")

        self.diagnostic_report()
        self.quality_report()
