from prefect import flow, get_run_logger, context


@flow
def main_fit_file_ingestion_flow():
    logger = get_run_logger()

    athlete_id = context.get("athlete_id")
    logger.info(f"Starting main fit file ingestion flow for athlete {athlete_id}")

    # TODO: Implement the flow

    logger.info(f"Main fit file ingestion flow for athlete {athlete_id} completed")
