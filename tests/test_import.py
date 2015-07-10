import time
import pytest
import sys
from mock import patch
from datetime import datetime

class TestOptionalFields:
    def setup(self):
        pass

    def test_import_before_five(self):
        if "beer" in sys.modules:
            del sys.modules["beer"]

        before_five = datetime(2015, 5, 30, 12, 10, 1, 0, None)
        with patch.object(time, 'localtime', return_value=before_five.timetuple()):
            with pytest.raises(Exception):
                import beer as b1

    def test_import_after_five(self):
        if "beer" in sys.modules:
            del sys.modules["beer"]

        after_five = datetime(2015, 5, 30, 18, 53, 30, 0, None)
        with patch.object(time, 'localtime', return_value=after_five.timetuple()):
            import beer as b2
