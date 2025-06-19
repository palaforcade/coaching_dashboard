from prefect import flow, get_run_logger
from prefect.variables import Variable


@flow
def main_fit_file_ingestion_flow():
    logger = get_run_logger()

    athlete_id = Variable.get("athlete_id")
    data_folder_path = Variable.get("data_folder_path")
    logger.info(f"Starting main fit file ingestion flow for athlete {athlete_id}")

    # TODO: Implement the flow

    logger.info(f"Main fit file ingestion flow for athlete {athlete_id} completed")
