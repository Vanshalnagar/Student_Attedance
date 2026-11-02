import pytest

def calculate_attendance(attended, total):
    if total <= 0 or attended < 0:
        raise ValueError("Invalid values")
    return (attended / total) * 100

@pytest.mark.parametrize("attended, total, expected", [
    (40, 40, 100.0),   
    (20, 40, 50.0),    
    (0,  40, 0.0),     
])
def test_attendance(attended, total, expected):
    assert calculate_attendance(attended, total) == expected

def test_invalid_values():
    with pytest.raises(ValueError):
        calculate_attendance(10, 0)  




















