from doc_utils import DocUtils

def test_is_field(sample_document):
    assert DocUtils().is_field("fehugieh", sample_document) is False
    key = list(sample_document.keys())[0]
    assert DocUtils().is_field(key, sample_document) is True

def test_get_field_across_documents(sample_document, sample_2_document):
    """Test to ensure you can get field across documents
    """
    sample_docs = [sample_document] * 20 + [sample_2_document] * 100
    new_docs = DocUtils().get_field_across_documents("value", sample_docs, missing_treatment="skip")
    assert len(new_docs) == 20, "Not skipping"

def test_get_field_across_documents_for_skip_if_any_missing(sample_document, sample_2_document):
    """Test to ensure you can get field across documents
    """
    new_document = sample_document.update(sample_2_document)
    sample_docs = [sample_document] * 20 + [sample_2_document] * 100 + [new_document] * 5
    new_docs = DocUtils().get_fields_across_documents(
        ["value", "check_value"], sample_docs,
        missing_treatment="skip_if_any_missing")
    assert len(new_docs) == 5, "Not skipping"
