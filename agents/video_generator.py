import os
import requests
from dotenv import load_dotenv
from utils.file_utils import read_from_csv, write_to_csv

load_dotenv()




def run(script_path: str, output_path: str):
    """
            Generate video using the script generated in previous step.

            TODO: Call Creatomate API

    """
