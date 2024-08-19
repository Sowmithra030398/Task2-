input_list = [4, 5, 1, 2, 2, 5, 4, 3]
 # Dictionary to keep track of the count of each element
element_count = {}
    
#count the occurance of the element
for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
#To determine which element has only one occurance
for element in input_list:
        if element_count[element] == 1:
              print(element)
              break#since we need only first element so break will break the loop of further occurance
