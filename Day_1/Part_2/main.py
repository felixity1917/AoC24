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
similarity_score = 0

for item in list_left:
    similar_count = list_right.count(item)
    similarity_score += item * similar_count

print("The Similarity Score is", similarity_score)
