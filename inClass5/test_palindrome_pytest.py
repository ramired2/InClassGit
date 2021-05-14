import pytest
import palindrome

def test_palindrome():
    result = palindrome.palin()
    assert result != -1

    assert result == True

    assert result != ""