from openai import OpenAI
import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def call_ai(system_prompt: str, user_prompt: str, max_tokens: int = 150, temperature: float = 0.3):
    """
        TODO: Check documentation of OpenAI API - https://platform.openai.com/docs/api-reference/responses?lang=python. Use the function parameters. Use the API key defined in .env file

    """


if __name__ == "__main__":
    """
        TODO: Use this for standalone testing.

    """
