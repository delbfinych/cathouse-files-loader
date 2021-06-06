import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_github_access_token():
    return os.environ.get("GITHUB_ACCESS_TOKEN", "")





def get_ftp_host():
    return os.environ.get("FTP_HOST", "")


def get_ftp_username():
    return os.environ.get("FTP_USERNAME", "")


def get_ftp_password():
    return os.environ.get("FTP_PASSWORD", "")
