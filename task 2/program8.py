input_list = [4, 5,1, 2, 2, 5, 4, 3]
length=len(input_list)
min_el=input_list[0]
mindex=0

for i in range(1,length):
    if input_list[i]<min_el:
        min_el=input_list[i]
        mindex=i
print("minimum element", min_el)
