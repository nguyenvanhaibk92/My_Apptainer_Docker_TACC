import pytest
from ml_data_analysis import compute_average_mass


def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}], 'a') == 1
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2
    assert compute_average_mass([{'a': 10}, {'a': 1}, {'a': 1}], 'a') == 4
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True

def test_compute_average_mass_exceptions():
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')                               # send an empty list
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')             # dictionaries not uniform
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a')           # value not a float
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a': 2}], 'b')             # key not in dicts
        
# %%
# Basic syntax:
# assert condition, message (optional)

# Example 1: Simple assertion
def process_number(a):
    assert a < 10, "Number must be less than 10"
    print(f"Processing number: {a}")

# Try it:
try:
    process_number(15)  # This will raise AssertionError
except AssertionError as e:
    print(f"Error: {e}")  # Prints: Error: Number must be less than 10
    
# %%
#!/usr/bin/python

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))


# %%
