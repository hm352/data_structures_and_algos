import pytest
from datetime import datetime

@pytest.fixture
def epoch_datetime():
    """
    A pytest fixture which returns a datetime object representing
    the epoch date (Jan 1, 1970 at 00:00:00 UTC).
    """
    return datetime.utcfromtimestamp(0)
