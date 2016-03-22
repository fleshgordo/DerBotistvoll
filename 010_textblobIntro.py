from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

text = '''
The sky is bright.
The sky is dark.
'''


blob = TextBlob(text)
print blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]
print '-----------'
print blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])
print '-----------'
print blob.sentences
print '-----------'
print blob.words
print '-----------'

for sentence in blob.sentences:
    print(sentence.sentiment)
# 0.060
# -0.341
print '-----------'

print blob.translate(to="es")  # 'La amenaza titular de The Blob...'