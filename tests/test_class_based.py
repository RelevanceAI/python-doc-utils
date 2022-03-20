import pytest

from doc_utils import Document
from doc_utils import DocumentList


def test_document(sample_document):
    document = Document(sample_document)

    label_val = sample_document["value"]

    target_value = document["value"]
    assert label_val == target_value

    document["value"] = 3
    assert document["value"] == 3


def test_nested_document(sample_nested_document):
    document = Document(sample_nested_document)

    label_val = sample_nested_document["value1"]["value2"]

    target_value = document["value1.value2"]
    assert label_val == target_value

    document["value"] = 3
    assert document["value"] == 3


def test_documents(sample_documents):
    documents = DocumentList(sample_documents)
