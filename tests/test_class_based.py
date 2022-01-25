import pytest

from doc_utils import Document


def test_document(sample_document):
    document = Document(sample_document)

    label_val = sample_document["value"]

    target_value = document["value"]
    assert label_val == target_value

    document["value"] = 3
    assert target_value == 3
