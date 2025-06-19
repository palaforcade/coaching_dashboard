from prefect import serve
from coaching_dashboard.etl.flows import main_fit_file_ingestion_flow


def run_deployments():
    main_fit_file_ingestion_deployment = main_fit_file_ingestion_flow.to_deployment(
        name="Main Fit File Ingestion",
    )

    serve(
        main_fit_file_ingestion_deployment,
    )


if __name__ == "__main__":
    run_deployments()
