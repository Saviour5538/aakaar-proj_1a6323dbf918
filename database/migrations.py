import os
from datetime import datetime


def migrate():
    # Create database schema
    with open('schema.sql', 'r') as f:
        schema = f.read()

    # Apply schema to database
    os.system(f'milvus db apply {schema}')


def rollback():
    # Rollback database schema
    os.system('milvus db rollback')