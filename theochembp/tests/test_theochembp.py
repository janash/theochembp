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

def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 0.1, 0])

    expected_distance = 0.1

    calculated_distance = theochembp.calculate_distance(r1, r2)

    assert pytest.approx(expected_distance) == calculated_distance
    
# Exercise - write a test for the calculate_angle function.

def test_calculate_angle():
    """Test the calculate angle function"""

    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_value = 90

    calculated_value = theochembp.calculate_angle(r1, r2, r3, degrees=True)

    assert pytest.approx(expected_value) == calculated_value

@pytest.mark.parametrize("p1, p2, p3, expected_angle",[
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60)
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = theochembp.calculate_angle(p1, p2, p3, degrees=True)

    assert pytest.approx(expected_angle) == calculated_angle


