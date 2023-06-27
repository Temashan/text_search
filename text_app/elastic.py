from elasticsearch import Elasticsearch

from config import ES_HOST, ES_PORT

MAPPING = {
            "properties": {
                "id": {
                    "type": "long",
                },
                "text": {
                    "type": "text"
                }
            },
        }


index = "docs"
ls: Elasticsearch = Elasticsearch(f"http://{ES_HOST}:{ES_PORT}")


def create_indexes():
    try:
        ls.indices.create(index=index, mappings=MAPPING)
    except Exception:
        print(f"index already exist")


if __name__ == "__main__":
    create_indexes()
