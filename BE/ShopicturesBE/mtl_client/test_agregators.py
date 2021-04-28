from .agregators import *
from .tasks import compute_stats_file_task
import os

def test_median_odd():
    assert median([5,6,-9,9,10,-90,60])[1] == 6

def test_median_even():
    assert median([5,6,-9,9,-90,60])[1] == 5.5

def test_stats_from_file():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "dummy_data.txt")
    expected = [('min', 0), ('max', 36346), ('avg', 3636.8), ('median', 0.0), ('total', 10)]
    assert compute_stats_file_task(path) == expected

