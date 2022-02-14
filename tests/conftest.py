import pytest
import random


@pytest.fixture
def sample_document():
    return {"value": random.randint(0, 100), "value.32": random.randint(0, 100)}


@pytest.fixture
def sample_2_document():
    return {"check_value": random.randint(0, 100)}


@pytest.fixture
def combined_sample_document():
    return {
        "value": random.randint(0, 99999),
        "check_value": random.randint(0, 9999999),
    }


@pytest.fixture
def sample_3_document():
    return {"check": random.randint(0, 100)}


@pytest.fixture
def sample_documents(sample_document):
    return sample_document * 100
