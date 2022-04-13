"""
Unit and regression test for the theochembp package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import theochembp


def test_theochembp_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "theochembp" in sys.modules
