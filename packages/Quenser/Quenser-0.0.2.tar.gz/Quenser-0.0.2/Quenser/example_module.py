# example_module.py
from robot.api.deco import keyword

class Quenser:
    @keyword("Say Hello")
    def say_hello(self, name="World"):
        return f"Hello, {name}!"
