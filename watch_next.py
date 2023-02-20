# ===== IMPORT SECTION =====
import spacy

nlp = spacy.load('en_core_web_md')  # a model to use


# ===== GLOBAL VARIABLES =====

# description of the Planet Hulk movie
planet_hulk = ["Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, "
               "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk "
               "can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery "
               "and trained as a gladiator."]

movies_list = []  # create a list for movies descriptions
movies_titles = []  # create a list of movies titles
similarities_list = []  # create a list of similarity results

YELLOW = '\033[93m'
WHITE = '\033[0m'


# ===== FUNCTIONS =====

# create a function that returns a title of the most similar movie
def similarities(descr):
    descr = planet_hulk  # Planet Hulk taken as input

    for token in descr:
        token = nlp(token)
        for token_ in movies_list:
            token_ = nlp(token_)
            similarities_list.append(token.similarity(token_))

    max_index = similarities_list.index(max(similarities_list))  # index of the highest similarity number

    the_most_similar = movies_titles[max_index]  # title index corresponding to the highest similarity number

    return the_most_similar


# ===== MAIN CODING SECTION =====

# import movies descriptions from external file and place in the list
with open("movies.txt", "r", encoding="utf-8") as movies_file:

    for lines in movies_file:
        temp = lines.strip("\n")
        movies_list.append(temp[9:])
        movies_titles.append(temp[0:7])

print(f"The most similar movie is {YELLOW}{similarities(planet_hulk)}")
