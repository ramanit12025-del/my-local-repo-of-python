shope={"shop":"50",
       "shampo":"200",
       "ingrdients":"20",
       "list":[1,2,3,4,],
       "tuple":("raman","aman","chaman")
       }
#third example
# here we can change data in list by list function method 
shope["list"].insert(5,"raman")# it is way to insert data in dictionary list by insert method
print(shope["list"])
shope["tuple"] = (shope["tuple"][0],"Raman",shope["tuple"][1],"Aman",shope["tuple"][2])
print(shope["tuple"])#it is way to insert data in dictionary tuple by tuple list indexing method
