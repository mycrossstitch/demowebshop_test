import os
from dotenv import load_dotenv

load_dotenv()


class Data:

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    NEW_EMAIL = os.getenv("NEW_EMAIL")
    NEW_FIRST_NAME = os.getenv("NEW_FIRST_NAME")
    NEW_LAST_NAME = os.getenv("NEW_LAST_NAME")
    NEW_GENDER = os.getenv("NEW_GENDER")