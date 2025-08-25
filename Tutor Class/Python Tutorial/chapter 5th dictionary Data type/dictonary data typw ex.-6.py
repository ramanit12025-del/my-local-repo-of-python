# this method use to "get" values of key element
shope={"shop":"50",
       "shampo":"200",
       "ingrdients":"20",
       "list":[1,2,3,4,],
       "tuple":("raman","aman","chaman")
       }
b=shope.get("shop")
print(b)
print(shope.get("shop"))
#same thing we get by normal print indexing commond
print(shope["shop"])
#but when do like this thing then get commond show none and if we use indexing commond then show error
print(shope.get("shop2"))
print(shope("shop2"))

