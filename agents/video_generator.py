import os
import requests
from dotenv import load_dotenv
from utils.file_utils import read_from_csv, write_to_csv

load_dotenv()

CREATOMATE_API_URL = "https://api.creatomate.com/v1/renders"
TEMPLATE_ID = ""
API_KEY = os.getenv("CREATOMATE_API_KEY")


def run(script_path: str, output_path: str):
    """
            Generate video using the script generated in previous step.

            TODO: Call Creatomate API

    """
