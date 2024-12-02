def get_input():
    list_stored = []
    while True:
        input_list=[]
        try:
            list_stored.append(input())
        except EOFError:
            break
    return list_stored

list_stored = get_input()

list_modified = []
for item in list_stored:
    list_buffer = item.split()
    list_modified.append(list_buffer)

safe_count = 0
for sublist in list_modified:
    safe_switch = True
    sublist_diffs = []
    for i in range(len(sublist)-1):
        adj_difference = int(sublist[i+1])-int(sublist[i])
        sublist_diffs.append(adj_difference)
        if abs(adj_difference) not in [1,2,3]:
            safe_switch = False
    cc_inc , cc_dec = 0 , 0
    for number in sublist_diffs:
        if number > 0:
            cc_inc += 1
        elif number < 0:
            cc_dec += 1
    if safe_switch == True:
        if cc_inc == 0:
            if cc_dec != 0:
                safe_count += 1
        elif cc_dec == 0:
            if cc_inc != 0:
                safe_count += 1
print(f"The number of safe cases are {safe_count}")
