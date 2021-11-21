import pytest

from compliance_clock.models import Summary

def test_create():
    s = Summary(type='D',events=[])
    assert s is not None
    s = Summary(type='W',events=[])
    assert s is not None

def test_create_invalid():
    with pytest.raises(ValueError):
        Summary(type='not_registered_summary_type',events=[])
    

