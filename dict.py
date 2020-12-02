dict1={'Python':'Python is an interpreted, high-level and general-purpose programming language.',
       'Immutable':'These are of in-built types like int, float, bool, string, unicode, tuple. In simple words, an immutable object can\'t be changed after it is created.',
       'Mutable':'These are of type list, dict, set. Custom classes are generally mutable.',
       'Datatype':'A particular kind of data item, as defined by the values it can take, the programming language used, or the operations that can be performed on it.'}

print("Enter the word you wan to knoow about: ")
what_you_wan_to_know=input()

if what_you_wan_to_know in dict1.keys():
       print(dict1.get(what_you_wan_to_know))
else:
       print("Still dictonary is in progressing")
