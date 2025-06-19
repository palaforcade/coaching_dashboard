import os
from prefect import flow, get_run_logger
from prefect.variables import Variable
from fitparse import FitFile

from coaching_dashboard.etl.tasks.process_fit_file import process_fit_file
from coaching_dashboard.etl.constants.paths import (
    DATA_RAW_FOLDER,
    DATA_PROCESSED_FOLDER,
)


@flow
def main_fit_file_ingestion_flow():
    logger = get_run_logger()

    athlete_id = Variable.get("athlete_id")
    data_folder_path = Variable.get("data_folder_path")
    logger.info(f"Starting main fit file ingestion flow for athlete {athlete_id}")

    fit_file = FitFile(
        os.path.join(data_folder_path, athlete_id, DATA_RAW_FOLDER, "test.fit")
    )

    df = process_fit_file(fit_file)

    df.write_parquet(
        os.path.join(
            data_folder_path,
            athlete_id,
            DATA_PROCESSED_FOLDER,
            "fit_file_test.parquet",
        )
    )

    logger.info(f"Main fit file ingestion flow for athlete {athlete_id} completed")
