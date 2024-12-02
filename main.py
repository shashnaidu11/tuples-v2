#tuples

fruits=("apple","orange","pineapple","mango")
print(fruits)

#acsess value of a tuple
print(fruits[1])
#packing in tuple
tuple=("My","Name","is","Shashwat")
for item in tuple:
    print(item,end=" ")

#unpacking in tuples
adress=("303","turpington lane","London")
print()
street_number , street , place=adress
print("streetnumber : "+ street_number)
print("street : "+ street)
print("place : "+ place)

#crating a tuple without brackets
flowers = "sunflower", "roses","lily","tulip"
print(flowers)

#creating a nested tuple
cars = ("buggati","mclaren",("nissan","rolls royce","bmw"))
car_name=cars[2][1]
print("My favourite car is ",car_name)
bmw=cars[2][2]
print("I want to buy a m4",bmw)


