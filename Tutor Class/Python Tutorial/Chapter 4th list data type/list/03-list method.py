# its 1st method (append)
garden=["apple","banana",508,"raman","aman",5.7,True,False]
garden.append("mangal")
garden.extend(["sadhna","sonam",1512])
print(garden)
# its 2nd method (sort)
No=[1,7,9,3,5,7,9,5]
No.sort()
print(No)
# its 3rd method 
No.reverse()
garden.reverse()
print(No)
print(garden)
# its 4th method
garden.insert(4,"grain")
No.insert(2,1)
print(garden)
print(No)
# its 5th method
garden.pop(4)
No.pop(2)
print(garden)
print(No)
# its 6th method
garden.remove("banana")
No.remove(9)
print(No)
print(garden)