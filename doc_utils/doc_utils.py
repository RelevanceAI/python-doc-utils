from .chunk_doc_utils import ChunkDocUtils


class DocUtils(ChunkDocUtils):
    """Class for all document utilities.
    Primarily should be used as a mixin for future functions
    but can be a standalone.
    # TODO: Extend to Chunk Doc Reading and Chunk Doc Writing
    """


class Document(DocUtils):
    def __init__(self, document):
        super().__init__()

        self.document = document

    def __setitem__(self, key):
        return self.document[key]

    def __getitem__(self, key, value):
        self.document[key] = value


class DocumentList(DocUtils):
    def __init__(self, documents):
        super().__init__()

        self.documents = [Document(document) for document in documents]
