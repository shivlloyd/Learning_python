# Object Oriented Programming in python

## Basic Class and Object

```python
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
```

This code defines a Python class called `Car`. Within this class, there's an `__init__` method, which serves as a constructor. This method initializes two attributes, `brand` and `model`, with values passed as parameters when creating a new instance of the class. When you create an instance of the `Car` class, like `my_car = Car("Toyota", "Corolla")`, it assigns "Toyota" to the `brand` attribute and "Corolla" to the `model` attribute. Similarly, for `my_new_car = Car("Tata", "Safari")`, it assigns "Tata" to `brand` and "Safari" to `model`. When you print `my_car.brand` and `my_car.model`, it outputs "Toyota" and "Corolla" respectively, and for `my_new_car.brand` and `my_new_car.model`, it prints "Tata" and "Safari". This output reflects the values assigned to the attributes of each instance of the `Car` class, demonstrating how each object holds its own unique data within the class template. The `self` parameter refers to the instance itself, allowing you to access and modify its attributes within the class methods.

## Class Method and Self

```python
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
```

A method called `full_name` is added to the `Car` class. This method combines the `brand` and `model` attributes of a car instance to create and return the full name of the car. When you call `my_car.full_name()` and `my_new_car.full_name()`, it executes the `full_name` method for each instance, concatenating the `brand` and `model` attributes with a space in between. This results in printing the full name of each car, like "Toyota Corolla" and "Tata Safari". This method enhances the functionality of the `Car` class by providing an easy way to retrieve the complete name of a car instance, encapsulating this behavior within the class itself.

## Inheritance

```python
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesala", "Model-S", "85kWh")
print(my_tesla.brand, my_tesla.model, my_tesla.battery_size)
print(my_tesla.full_name())
```

now a new class called `ElectricCar` is created, which inherits from the `Car` class. This means that `ElectricCar` inherits all the attributes and methods of the `Car` class. When you create an instance of `ElectricCar`, like `my_tesla = ElectricCar("Tesla", "Model-S", "85kWh")`, it calls the `__init__` method of the `Car` class through the `super()` function, passing the `brand` and `model` parameters to initialize these attributes inherited from the parent class. Additionally, it initializes the `battery_size` attribute specific to the `ElectricCar` class. Therefore, when you print `my_tesla.brand`, `my_tesla.model`, and `my_tesla.battery_size`, it outputs "Tesla", "Model-S", and "85kWh" respectively. Furthermore, when you call `my_tesla.full_name()`, it executes the `full_name` method inherited from the `Car` class, providing the complete name of the electric car. This demonstrates how inheritance allows for code reuse and extension, with `ElectricCar` inheriting functionality from `Car` while also having its own unique attributes.

## Encapsulation

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesala", "Model-S", "85kWh")
print(my_tesla.__brand)
print(my_tesla.get_brand())
```

in here the `Car` class is modified to encapsulate the `brand` attribute by making it private, denoted by the double underscore `__` prefix. This means that the `brand` attribute is not directly accessible from outside the class. To provide access to this private attribute, a getter method `get_brand` is implemented within the `Car` class. This method allows external code to retrieve the value of the private `brand` attribute indirectly. When you attempt to directly access `my_tesla.__brand`, it results in an AttributeError because the `__brand` attribute is private and cannot be accessed from outside the class. However, when you call `my_tesla.get_brand()`, it successfully returns the value of the `brand` attribute with an added exclamation mark, demonstrating how encapsulation restricts direct access to attributes while still providing a controlled way to retrieve their values through getter methods. This ensures data integrity and enables better control over access to class attributes.

## Polymorphism

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesala", "Model-S", "85kWh")
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
```

here polymorphism is demonstrated through the `fuel_type` method defined in both the `Car` and `ElectricCar` classes, but with different behaviors. Polymorphism allows objects of different classes to be treated as objects of a common superclass. Here, both `Car` and `ElectricCar` are subclasses of the `Car` class. When you call `my_tesla.fuel_type()`, it executes the `fuel_type` method defined in the `ElectricCar` class, returning "Electric Charge", which reflects the fact that electric cars are powered by an electric charge. Conversely, when you create an instance of the `Car` class, like `safari = Car("Tata", "Safari")`, and call `safari.fuel_type()`, it invokes the `fuel_type` method defined in the `Car` class, returning "Petrol or Diesel", indicating that traditional cars are typically powered by petrol or diesel. This demonstrates how different subclasses can have methods with the same name but behave differently, depending on the specific implementation within each subclass, showcasing the concept of polymorphism in object-oriented programming.

## Class Variables

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


Car("Tata", "Safari")
Car("Tata", "Nexon")

print(Car.total_car)
```

A class variable `total_car` is added to the `Car` class to keep track of the number of cars created. This variable is initialized to 0 outside of any methods, making it a class-level attribute rather than an instance-level one. Within the `__init__` method of the `Car` class, each time a new instance of `Car` is created, the `total_car` variable is incremented by 1. Therefore, every time the `Car` class is instantiated, the `total_car` count increases. In this specific example, two instances of the `Car` class are created with the lines `Car("Tata", "Safari")` and `Car("Tata", "Nexon")`. After these instances are created, the `print(Car.total_car)` statement outputs the total number of cars created, which is 2 in this case. This demonstrates how class variables can be used to maintain shared state among all instances of a class, in this case, keeping track of the total number of cars created throughout the program's execution.

## Static Method

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Tata", "Safari")
Car("Tata", "Nexon")

print(my_car.general_description())
print(Car.general_description())
```

in here a static method `general_description` is added to the `Car` class. Static methods in Python are defined using the `@staticmethod` decorator and do not operate on instances of the class, they are bound to the class itself rather than to instances of the class. Therefore, they do not have access to instance attributes or methods and do not require the `self` parameter in their definition. The `general_description` static method simply returns a general description of a car, stating that cars are means of transport. When you call `my_car.general_description()` or `Car.general_description()`, it executes the `general_description` static method of the `Car` class, providing the same output in both cases. This demonstrates how static methods can be used to define utility functions related to a class that do not require access to instance-specific data. Behind the scenes, static methods do not receive any implicit arguments when called, making them independent of the state of any particular instance or the class itself. They are primarily used to organize utility functions within a class's namespace.

## Property Decorators

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_car = Car("Tata", "Safari")
# my_car.model = "City"
Car("Tata", "Nexon")

print(my_car.model)
```

The `@property` decorator is used in the `Car` class to create a read-only property for the `model` attribute. By decorating the `model` method with `@property`, it allows accessing the `model` attribute as if it were a normal attribute, without the need for parentheses. However, attempts to modify the `model` attribute directly, such as `my_car.model = "City"`, will raise an AttributeError because the property is read-only. When you call `print(my_car.model)`, it invokes the `model` method defined in the `Car` class, returning the value of the `__model` attribute. This property decorator simplifies the syntax for accessing the `model` attribute while ensuring that it cannot be modified directly, providing a controlled way to interact with class attributes. This is useful for maintaining data integrity and encapsulation within the class.

## Class Inheritance and isinstance() Function

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesala", "Model-S", "85kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
```

The output of `isinstance(my_tesla, Car)` is `True` because `my_tesla` is an instance of the `Car` class. The output of `isinstance(my_tesla, ElectricCar)` is also `True` because `my_tesla` is an instance of the `ElectricCar` class. This demonstrates how `isinstance()` checks whether an object belongs to a specific class or its subclasses.

## Multiple Inheritance

```python
class Battery:
    def battery_info(self):
        return "This is Battery"


class Engine:
    def engine_info(self):
        return "This is engine"


class ElectricCarTwo(Battery, Engine, Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)


my_new_tesla = ElectricCarTwo("Tesla", "Model-X")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
```

here multiple inheritance is demonstrated by creating two separate classes, `Battery` and `Engine`, and then having the `ElectricCarTwo` class inherit from both of them, as well as from the `Car` class. When a class inherits from multiple parent classes, it inherits all their attributes and methods. In this case, `ElectricCarTwo` inherits the `battery_info` method from the `Battery` class and the `engine_info` method from the `Engine` class. Additionally, since `ElectricCarTwo` also inherits from the `Car` class, it has access to its attributes and methods as well. Therefore, when you create an instance of `ElectricCarTwo` and call `my_new_tesla.battery_info()`, it returns "This is Battery", and when you call `my_new_tesla.engine_info()`, it returns "This is engine". This demonstrates how multiple inheritance allows a class to inherit behavior from multiple parent classes, providing flexibility and code reuse in object-oriented programming.
