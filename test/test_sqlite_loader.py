from ..Sqlite3Loader import SQLite3Loader

db_path = "/Users/flybywindwen/Projects/spiders/Ahospital/sqlite/HospitalSpider.db"
table_name = 'hospitalspider'
def test_sqlite_loader():
    loader = SQLite3Loader(db_path, table_name, page_content_column='paragragh')
    doc_list = loader.load()
    assert len(doc_list) > 0
    doc = doc_list[0]
    assert len(doc.page_content) > 0
    assert 'url' in doc.metadata