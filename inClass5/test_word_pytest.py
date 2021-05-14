import pytest
import wordcount

def test_count():
    result = wordcount.count()
    assert result != 0