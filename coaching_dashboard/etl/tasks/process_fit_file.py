import polars as pl
import math
import os
from fitparse import FitFile
from prefect import task


@task
def process_fit_file(
    fitfile: FitFile,
) -> pl.DataFrame:
    """
    Process FIT file data into a clean DataFrame with all records and lap information.

    Returns:
        Polars DataFrame with processed cycling data
    """

    # Process records
    records_data = _process_records(fitfile)

    # Create DataFrame
    df = pl.DataFrame(records_data).sort("Timestamp")

    return df


def _process_records(fitfile) -> list:
    """Process record messages into structured data."""
    records = []

    for record in fitfile.get_messages("record"):
        row = {}
        timestamp = None

        # Extract all fields
        for field in record:
            if field.name == "timestamp":
                timestamp = field.value
            elif field.name == "power":
                row["Power"] = field.value
            elif field.name == "cadence":
                row["Cadence"] = field.value
            elif field.name == "speed":
                row["Speed_mps"] = field.value
            elif field.name == "heart_rate":
                row["Heart_Rate"] = field.value
            elif field.name == "distance":
                row["Distance_m"] = field.value
            elif field.name == "altitude":
                row["Elevation"] = field.value
            elif field.name == "enhanced_altitude":
                row["Altitude"] = field.value
            elif field.name == "position_lat":
                row["Latitude"] = field.value
            elif field.name == "position_long":
                row["Longitude"] = field.value
            elif field.name == "temperature":
                row["Temperature"] = field.value

        if timestamp is None:
            continue

        row["Timestamp"] = timestamp
        records.append(row)

    return records
