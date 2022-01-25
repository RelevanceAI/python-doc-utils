from typing import Dict, List

from .chunk_doc_utils import ChunkDocUtils


class DocUtils(ChunkDocUtils):
    """Class for all document utilities.
    Primarily should be used as a mixin for future functions
    but can be a standalone.
    # TODO: Extend to Chunk Doc Reading and Chunk Doc Writing
    """


class Document(DocUtils):
    """
    A Class for handling json like arrays of dictionaries
    
    Example:
    >>> doc = Document({"value": 3"})
    >>> doc['value'] # returns 3
    >>> doc['value'] = 3 # should set the value     
    """
    def __init__(self, document: Dict):
        super().__init__()

        self.document = document

    def __getitem__(self, key: str):
        return self.document[key]

    def __setitem__(self, key: str, value: str):
        self.document[key] = value


class DocumentList(DocUtils):
    """
    A Class for handling json like arrays of dictionaries
    
    Example:
    >>> docs = DocumentList([{"value": 2}, {"value": 10}])
    """
    def __init__(self, documents: List):
        super().__init__()

        self.documents = [Document(document) for document in documents]

    def __getitem__(self, index):
        return self.documents[index]
