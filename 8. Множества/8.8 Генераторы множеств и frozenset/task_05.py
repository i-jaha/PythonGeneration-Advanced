'''
Используя генератор множеств, 
дополните приведенный ниже код так, 
чтобы получить множество, 
содержащее уникальные слова 
(в нижнем регистре) 
строки sentence. 
Результат вывести на одной строке 
в алфавитном порядке, 
разделяя элементы одним символом пробела.

Примечание. 
Учтите, 
что знаки пунктуации 
не относятся к словам.
'''

# example
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

# review 1
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
for ch in ':,.!?();':
    sentence = sentence.replace(ch, "")
unique_words = {word.lower() for word in sentence.split()}
print(*sorted(unique_words))

# review 2
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
print(*sorted({w.lower() for w in ''.join(ch if ch.isalnum() or ch.isspace() else ' ' for ch in sentence).split()}))