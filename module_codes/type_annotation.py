# Type annotations are optional in Python. They can be very helpful, 
# though, because they make code easier to read. Annotations make 
# the variable types clear to those reading the code. 
# They can also help you catch errors during compilation. 
# In the example below, we are using the typing module to 
# annotate the different types of variables.

import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}
# Define a variable of type bool
is_true: bool = True