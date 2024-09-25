import pytest
from core.libs.exceptions import FyleError
from core.libs.assertions import assert_auth, assert_true, assert_valid, assert_found

def test_assert_auth_raises_401():
    with pytest.raises(FyleError) as exc_info:
        assert_auth(False)  # This should trigger the assertion
    assert exc_info.value.status_code == 401
    assert exc_info.value.message == 'UNAUTHORIZED'

def test_assert_auth_custom_message():
    with pytest.raises(FyleError) as exc_info:
        assert_auth(False, 'Custom Unauthorized Message')
    assert exc_info.value.status_code == 401
    assert exc_info.value.message == 'Custom Unauthorized Message'


def test_assert_true_raises_403():
    with pytest.raises(FyleError) as exc_info:
        assert_true(False)  # This should trigger the assertion
    assert exc_info.value.status_code == 403
    assert exc_info.value.message == 'FORBIDDEN'


def test_assert_true_custom_message():
    with pytest.raises(FyleError) as exc_info:
        assert_true(False, 'Custom Forbidden Message')
    assert exc_info.value.status_code == 403
    assert exc_info.value.message == 'Custom Forbidden Message'


def test_assert_valid_raises_400():
    with pytest.raises(FyleError) as exc_info:
        assert_valid(False)  # This should trigger the assertion
    assert exc_info.value.status_code == 400
    assert exc_info.value.message == 'BAD_REQUEST'


def test_assert_valid_custom_message():
    with pytest.raises(FyleError) as exc_info:
        assert_valid(False, 'Custom Bad Request Message')
    assert exc_info.value.status_code == 400
    assert exc_info.value.message == 'Custom Bad Request Message'


def test_assert_found_raises_404():
    with pytest.raises(FyleError) as exc_info:
        assert_found(None)  # This should trigger the assertion
    assert exc_info.value.status_code == 404
    assert exc_info.value.message == 'NOT_FOUND'


def test_assert_found_custom_message():
    with pytest.raises(FyleError) as exc_info:
        assert_found(None, 'Custom Not Found Message')
    assert exc_info.value.status_code == 404
    assert exc_info.value.message == 'Custom Not Found Message'
