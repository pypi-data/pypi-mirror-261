import os
import tantivy
from fuzztypes import Fuzzmoji, const


def test_tantivy():
    # make sure the index is built
    assert Fuzzmoji.get_value("balloon") == "🎈"

    # standard schema
    schema_builder = tantivy.SchemaBuilder()
    schema_builder.add_integer_field("doc_id", stored=True)
    schema_builder.add_text_field("term", stored=True)
    schema = schema_builder.build()

    path = os.path.join(const.FuzzOnDisk, "Fuzzmoji.lance/_indices/tantivy")
    index = tantivy.Index(schema, path=path)
    searcher = index.searcher()

    query = index.parse_query("thought bubble")
    result = searcher.search(query, 5)
    for score, address in result.hits:
        doc = searcher.doc(address)
        print(doc, score)


def test_fuzzmoji():
    assert Fuzzmoji.get_value("thought bubble") == "🤔"