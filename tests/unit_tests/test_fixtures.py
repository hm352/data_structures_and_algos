from datetime import datetime

from tests.utils.fixtures.dates import epoch_datetime

def test_epoch_datetime(epoch_datetime):
    """
    A unitest which tests the epoch_datetime fixture.
    """
    assert epoch_datetime == datetime.utcfromtimestamp(0)
