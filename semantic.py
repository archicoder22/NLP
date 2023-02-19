import spacy

# ===== SIMILARITY =====
print("WORKING WITH SIMILARITY:")
nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""
It is interesting to see that 2 animals are more similar than an animal and a fruit.
However, "banana" is more similar to monkey than to a cat, probably because monkeys eat bananas.
"""

# ===== VECTORS =====
print("\nWORKING WITH VECTORS:")
tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# another example of similarity
print("\ntrying different words:")
tokens_2 = nlp("yellow work bridge house")

for token1 in tokens_2:
    for token2 in tokens_2:
        print(token1.text, token2.text, token1.similarity(token2))

# ===== WORKING WITH SENTENCES =====
print("\nWORKING WITH SENTENCES:")
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car",
             "I\'d like my boat back", "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# ===== MODELS COMPARISON =====
"""
Model en_core_web_sm has no word vectors loaded so similarity judgements are not useful.
Similarity results come up generally lower using this model.
"""