"""_summary_
    Store values in key-value pairs
    It is ordered, changeable and doesn't allow duplicates
    They're created with curly brackets and come in key:value pairs which are separated by commas. 
    You can find the value of something using the key and vice versa 
"""

car_dict = {"brand": "BMW", "model": "M5", "year": 2024}
print(car_dict)
print(car_dict["brand"])
print(car_dict.get("model"))
#keys have to be unique, can be numbers as well as long as they're unique
#you can put in a key that is non-existent and it would print out none
#can use the .get to assign a default value
print(car_dict.get("type", "Not a valid key")) #not a valid key becomes a default value

