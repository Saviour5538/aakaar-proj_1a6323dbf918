from backend.api.v1.ai_ml import ai_ml_handler
from backend.api.v1.database import database_handler

def ingestion_handler(event, context):
    # implementation of ingestion_handler
    ai_ml_handler(event, context)
    database_handler(event, context)