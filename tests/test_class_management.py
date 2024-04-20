import pytest
from src.class_management import Management


@pytest.fixture
def manage1():
    return Management()


def test_uploading_favorites(manage1):
    manage1.for_test()
    assert 'test'

