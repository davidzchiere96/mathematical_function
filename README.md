# _Mathematical Function_


Simple python project simulating the behaviour of a mathematical function.

  </a>
  <a href="https://www.python.org/downloads/release/python-311">
    <img src="https://img.shields.io/badge/python-3.11-green.svg" lazyload />
  </a>

###
__________________________________________________________________
### Main Architecture


<p align="center">
  <img src="doc\img\MATHEMATICAL_FUNCTION_CODE_FLOW.png" />
</p>
<br>

__________________________________________________________________
#### MathFunction

Script that simulates the behavior of a mathematical function using the Object Oriented Paradigm

<p>

- Required modules 
    <br>
    - _abc_: Abstract Base Classes.
    - _logger_: Ad hoc module for managing logs in Python.

</p>

- Scope:
    <br>
    This script instantiates an abstract class MathFunction and a child class AverageFunction, which inherits the abstract calculation method and extends it by computing the average value based on the input parameters passed as a tuple in the input_arguements() function.
<br>
<br>

__________________________________________________________________
#### Logger

This script is a helper to create an ad hoc logger in Python.
<p>

- Required modules
    <br>
    - _uuid_: to generate a unique identifier (UUID).
    - _logging_: for managing logs in Python.

</p>

- Scope:
    <br>
    Defines a logger() function that creates and returns a configured logger.

<p>

- Details:
    <br>
    Inside the logger() function,
    generates a unique identifier (UUID) to track each logging transaction.
    Configure the logger using logging.basicConfig():
    Creates and returns a logger to the console using logging.getLogger() that contains the previously defined configurations.
    </p>


