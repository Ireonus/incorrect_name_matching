list_a = ['apple', 'bananna', 'lemon', 'strawberry', 'chocolate','popo']
list_b = ['bannana', 'aple','poppos', 'chococolate','strawberries', 'lenom']

dict_a = {list_a[i]: 0  for i in range(len(list_a))}

for item_a in dict_a:
    match_list_b = [0 for item_b in list_b]
    for letter_a in item_a:
        for index,item_b in enumerate(list_b):
            if letter_a in item_b:
                match_list_b[index] +=1
    max_counter = 0
    for index,counter in enumerate(match_list_b):
        if counter > max_counter :
            max_counter = counter
            matching_word = list_b[index]
    
    dict_a[item_a]=matching_word
    
print(dict_a)







