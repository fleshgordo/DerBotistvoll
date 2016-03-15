import random

text = "IN THE BEGINNING WAS THE WORD"
text = text.split(" ")
random.shuffle(text)
print text
print ' '.join(text)