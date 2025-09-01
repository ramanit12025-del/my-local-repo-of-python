q={1,3,9,5,2,8,4,7.11,33,44,88,77,55,44,22,45,76,54,33,23,67,59}
print(q.remove(2))#it remove element that which give you but not show element in output in this place show none
print(q)
# set.remove(x) method कुछ return नहीं करता.

# इसका काम सिर्फ set से element हटाना है।

# Python में ऐसे methods जो सिर्फ काम करते हैं लेकिन कोई value वापस नहीं देते, उनका return value None होता है।

# इसलिए जब आपने लिखा print(q.remove(2)),

# पहले 2 remove हो गया ✅

# फिर remove() ने कुछ return नहीं किया → default None

# और print() ने वही None दिखा दिया