input_list=[4,2,-3,1,6]
zero_sum_sublists = []
for start in range(0,len(input_list)):
        current_sum = 0
        for end in range(start, len(input_list)):
            current_sum += input_list[end]
            # Check if the current sum is zero
            if current_sum == 0:
                   zero_sum_sublists.append(input_list[start:end + 1])

print(zero_sum_sublists)
