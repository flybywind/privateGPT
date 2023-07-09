"""Load from SQLite3 object"""
from langchain.document_loaders import DataFrameLoader

class SQLite3Loader(DataFrameLoader):
    """Initialize with db path and table name specified by user."""
    def __init__(self, db_path: str, table_name:str, page_content_column: str = "text"):
        import sqlite3
        import pandas as pd
        cnx = sqlite3.connect(db_path)

        data_frame = pd.read_sql_query(f"SELECT * FROM {table_name}", cnx)
        super().__init__(data_frame, page_content_column)