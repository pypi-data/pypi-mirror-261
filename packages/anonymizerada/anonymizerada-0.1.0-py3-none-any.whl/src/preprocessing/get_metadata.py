"""Metadata Module"""

import pandas as pd
from sdv.metadata import SingleTableMetadata


def generate_metadata(ori: pd.DataFrame) -> SingleTableMetadata:
    """
    Generates metadata from the original dataframe.

    Args:
        ori (pd.DataFrame): The original dataframe.

    Returns:
        SingleTableMetadata: Metadata object for the dataframe.
    """
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(ori)
    # metadata.visualize(show_table_details="summarized", output_filepath="metadata.png")
    metadata.validate()
    metadata.validate_data(data=ori)

    # metadata.save_to_json(filepath="../report/metadata_v1.json")

    # python_dict = metadata.to_dict()

    return metadata
