def single_root_words(root_words, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_words.upper() in other_words[i].upper() :
            same_words.append(other_words[i])

        elif other_words[i].upper() in root_words.upper():
            same_words.append(other_words[i])



    return same_words

result_1 = single_root_words('rich', 'richiest','orichalcum','cheers','richies')
result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result_1)
print(result_2)
