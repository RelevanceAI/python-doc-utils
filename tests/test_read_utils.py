from doc_utils import DocUtils

def test_is_field(sample_document):
    assert DocUtils().is_field("fehugieh", sample_document) is False
    key = list(sample_document.keys())[0]
    assert DocUtils().is_field(key, sample_document) is True
