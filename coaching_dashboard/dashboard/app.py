import streamlit as st
import polars as pl
import os
from dotenv import load_dotenv


load_dotenv()

DATA_FOLDER_PATH = os.getenv("DATA_FOLDER_PATH")

# Set page config
st.set_page_config(page_title="Coaching Dashboard", page_icon="👋", layout="wide")

# Main title
st.title("Coaching Dashboard")
st.markdown("---")

# Add athlete ID input
athlete_id = st.text_input(
    "Enter Athlete ID",
    value="palaforcade",
    help="Enter the ID of the athlete whose data you want to view",
)

# Load the parquet file
df = pl.read_parquet(
    os.path.join(DATA_FOLDER_PATH, athlete_id, "processed", "fit_file_test.parquet")
)


# Calculate speed from distance

# Speed = change in distance / change in time
speed_df = df.with_columns(
    [
        pl.col("Distance_m").diff().alias("distance_change"),
        pl.col("Timestamp").diff().dt.total_seconds().alias("time_change"),
    ]
).with_columns([(pl.col("distance_change") / pl.col("time_change")).alias("Speed_mps")])

# Create speed over time plot
st.line_chart(
    speed_df,
    x="Timestamp",
    y="Speed_mps",
)

# Display as table
st.dataframe(df)
