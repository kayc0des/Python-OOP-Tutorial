# Classes

A class creates a new type where objects are instances of the class. Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields. Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class.

# The Self

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self.

# Methods

Methods in Python are essentially functions in accordance with Guido's saying "first-class everything". So a function belonging to a class is referred to as a method. In the main module, calculate_total_price and apply_discount are examples of methods. Methods are required to pass at least one argument, an object method will pass 'self - the object/instance' as it's first argument while a class method will pass 'cls - the class' as it's first argument.

# __init___ method

The __init__ method  runs as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object.