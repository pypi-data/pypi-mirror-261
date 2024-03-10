"""Configuration files for the project."""
import os

# Path to the vector store
APP_ENV = os.getenv("APP_ENV", 'development')
APP_NAME = os.getenv("APP_NAME", 'Prompt Engineers AI - API Server')
APP_SECRET = os.getenv("APP_SECRET", '')
APP_VERSION = os.getenv("APP_VERSION", '')
APP_ORIGINS = os.getenv("APP_ORIGINS", '*')

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", '')
## Ollama URL
OLLAMA_BASE_URL= os.getenv("OLLAMA_BASE_URL", 'http://localhost:11434')

# Mongo
DB_NAME= os.getenv('DB_NAME', 'promptengineers')
DB_COLLECTION = os.getenv('DB_COLLECTION', 'history')
MONGO_CONNECTION = os.getenv("MONGO_CONNECTION", f'mongodb://localhost:27017')
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", f'llm-server')

# Redis
REDIS_URL = os.getenv("REDIS_URL", 'redis://localhost:6379/0')

# S3 Bucket Credentials
BUCKET = os.getenv("BUCKET", 'precision-x')
S3_REGION = os.getenv("S3_REGION", 'us-east-1')
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID", '')
ACCESS_SECRET_KEY = os.getenv("ACCESS_SECRET_KEY", '')
MINIO_SERVER = os.getenv("MINIO_SERVER", '')

# Pinecone Credentials
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", '')
PINECONE_ENV = os.getenv("PINECONE_ENV", '')
PINECONE_INDEX = os.getenv("PINECONE_INDEX", '')

# Blockchain Credentials
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY", '')
