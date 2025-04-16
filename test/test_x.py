from hub import hub

import pytest

def test_voltage():
    assert hub.battery.voltage()>8000
