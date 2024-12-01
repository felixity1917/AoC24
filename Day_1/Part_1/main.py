def get_input():
    list_left , list_right = [] , []
    while True:
        input_list=[]
        try:
            input_list=input().split('   ')
            list_left.append(int(input_list[0]))
            list_right.append(int(input_list[1]))
        except EOFError:
            break
    return list_left , list_right
list_left , list_right = get_input()
list_left.sort()
list_right.sort()
list_calculated = []
for i in range(len(list_left)):
    list_calculated.append(abs(list_left[i] - list_right[i]))
sum_of_distances = 0
for j in list_calculated:
    sum_of_distances += j
print('The final output is', sum_of_distances)
