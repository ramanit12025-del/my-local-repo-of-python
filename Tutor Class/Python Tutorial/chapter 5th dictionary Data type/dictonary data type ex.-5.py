# this method used to"update"elements of key value or add key value
shope={"shop":"50",
       "shampo":"200",
       "ingrdients":"20",
       "list":[1,2,3,4,],
       "tuple":("raman","aman","chaman")
       }
shope.update({"shampo":100})
print (shope)
print(shope.values())
shope.update({"shop":100,"biskiut":100})
print(shope)
