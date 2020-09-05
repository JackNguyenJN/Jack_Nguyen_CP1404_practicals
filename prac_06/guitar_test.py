from prac_06.guitar import Guitar

"""Test Guitar class to make sure string method and is_vintage() method work."""

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
other_guitar = Guitar("Another Guitar", 2012, 1512.9)
print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98, guitar.get_age()))
print("{} get_age() - Expected {}. Got {}".format(other_guitar.name, 10, other_guitar.get_age()))
print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
print("{} is_vintage() - Expected {}. Got {}".format(other_guitar.name, False, other_guitar.is_vintage()))

