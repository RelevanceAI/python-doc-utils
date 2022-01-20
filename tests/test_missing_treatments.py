from doc_utils import DocUtils
from doc_utils.errors import InvalidTreatment, MissingFieldError

def test_return_empty_string(sample_document):
    assert DocUtils().get_field(
        "foo", sample_document, missing_treatment="return_empty_string"
    ) == "", "Not empty string"

def test_return_none(sample_document):
    assert DocUtils().get_field(
        "foo", sample_document, missing_treatment="return_none"
    ) == None, "Not None"

def test_replace(sample_document):
    assert DocUtils().get_field(
        "foo", 
        sample_document, 
        missing_treatment="replace", 
        replacement_value="bar"
    ) == "bar", "Not bar"

    assert DocUtils().get_field(
        "foo", 
        sample_document, 
        missing_treatment="replace",
        replacement_value=0
    ) == 0, "Not zero"
    
    assert DocUtils().get_field(
        "foo", 
        sample_document, 
        missing_treatment="replace", 
        replacement_value=4.0
    ) == 4.0, "Not four point zero"

def test_raise_error(sample_document):
    try:
        DocUtils().get_field(
            "foo", sample_document, missing_treatment="raise_error"
        )
    except MissingFieldError:
        assert True

def test_invalid_treatment(sample_document):
    try:
        DocUtils().get_field(
            "foo", sample_document, missing_treatment="bar"
        )
    except InvalidTreatment:
        assert True
