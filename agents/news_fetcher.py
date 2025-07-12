from loguru import logger
import os
import requests
from dotenv import load_dotenv
from newspaper import Article

from utils.file_utils import write_to_csv

load_dotenv()




def extract_article(url):
    try:
        """
        Fetch top news stories using NewsAPI.

        TODO: Implement API call using the API key defined in .env file
        
        """
    except Exception as e:
        logger.error("Failed to extract article")
        return []


def run(output_path):

