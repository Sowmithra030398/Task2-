# Sample input lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 10, 11, 12]

 # Convert each list to a set to remove duplicates within each list
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
common_duplicates = set1 & set2 & set3 #Getting common duplicates using and function
# print(common_duplicates)
print(list(common_duplicates))#printing the common in list
