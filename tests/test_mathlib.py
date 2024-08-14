import mathlib
import pytest
import sys

# to run test python3 -m pytest
# or py.test
# -v to verbose


@pytest.mark.skip(reason="Skip this test")
def test_calc_total():
  total = mathlib.calc_total(4, 5)
  assert total == 9

@pytest.mark.skipif(sys.version_info > (3,5), reason="Skip this test if python is greater than 3.5")
def test_calc_total2():
  total = mathlib.calc_total(4, 5)
  assert total == 9

# to run test by name can run pytest -k multiply and will run all tests that contain the word multiply
def test_calc_multiply():
  result = mathlib.calc_multiply(10, 3)
  assert result == 30

# custom test for windows (custom category)
# to run pytest -m windows -v
# to not windows tests run pytest -m "not windows" -v
@pytest.mark.windows
def test_windows():
  assert True