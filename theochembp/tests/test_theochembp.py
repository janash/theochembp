"""
Unit and regression test for the theochembp package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy as np

import theochembp


def test_theochembp_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "theochembp" in sys.modules

@pytest.mark.skip
def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 0.1, 0])

    expected_distance = 0.1

    calculated_distance = theochembp.calculate_distance(r1, r2)

    assert pytest.approx(expected_distance) == calculated_distance