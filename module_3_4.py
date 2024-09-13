def single_root_words(root_word, *other_words):
    same_words=[]
    root_word = root_word.lower()
    for i in other_words:
        i=i.lower()
        if  i.count('rich'):
            same_words.append(i)
        elif root_word.count(i):
            same_words.append(i.capitalize())
    print(same_words)
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')





