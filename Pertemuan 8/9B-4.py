jane = {"name": "Jane", "age": 25, "height": 1.75}
jane["age"] = 26              
jane["weight"] = 67          

from collections import namedtuple

Person = namedtuple("Person", "name age height")
jane = Person("Jane", 25, 1.75)
jane.age = 26                 
jane.weight = 67   
