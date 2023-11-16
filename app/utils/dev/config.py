import os

from dotenv import load_dotenv

load_dotenv()

# SERVER
SERVER_IP = os.getenv("SERVER_IP")
SERVER_URL = os.getenv("SERVER_URL")

# DATABASE
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT"))
DB_DATABASE = os.getenv("DB_DATABASE")
DB_CHARSET = os.getenv("DB_CHARSET")
DB_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_DATABASE}"

# S3
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_REGION_NAME = os.getenv("S3_REGION_NAME")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")  # IAM 사용자의 액세스 키
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")  # IAM 사용자의 비밀 액세스 키
S3_PREFIX = os.getenv("S3_PREFIX")  # 시작 폴더 지정

QUEENSLAND_TIMEZONE = "Australia/Queensland"
