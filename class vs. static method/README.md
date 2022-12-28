# Class Vs. Static Method

The class method in Python is a method, which is bound to the class but not the object of that class. The static methods are also same but there are some basic differences. For class methods, we need to specify @classmethod decorator, and for static method @staticmethod decorator is used.

The class method takes cls (class) as first argument and can access and modify the class state while the static method does not take any specific parameter and cannnot access nor modify the class state. 