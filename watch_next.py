# importing the required module
import spacy
nlp = spacy.load('en_core_web_md')

# creating variable with movie description
planet_hulk = ["""Will he save their world or destroy it? When the hulk becomes
too dangerous for the Earth, the illuminati trick hulk into a shuttle and launch him
into space to a planet where he can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""]

def watch_next(watch_status):
    # preparing movie description for similarity calculation
    input_doc = nlp(planet_hulk[0])
    
    # reading movie descriptions from 'movies.txt'
    with open('movies.txt', 'r') as f:
        movies = f.readlines()
    
    # prepare the movie descriptions for similarity calculation using for loop
    movie_docs = []
    for movie in movies:
        title, description = movie.split(':')
        doc = nlp(description)
        movie_docs.append((doc, title))
        
    # finding the most similar movie
    max_similarity = -1
    most_similar_movie = None
    for doc, title in movie_docs:
        similarity = doc.similarity(input_doc)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = title
    if most_similar_movie:
        if watch_status.upper() == "NO":
            # if the user haven't watched Planet Hulk, suggest the most similar movie
            print("Planet Hulk is very similar to", most_similar_movie,", if you liked that, you should watch it!")
        else:
            # if the user has watched Planet Hulk, return the most similar movie
            print("The most similar movie to 'Planet Hulk' is: ", most_similar_movie)
    else:
        print("No similar movies found.")

# asking the user if they have watched Planet Hulk
watch_status = input("Hi there! Have you watched Planet Hulk? [Yes/No]")

# checking if the answer is valid, if not ask again
while True:
    if watch_status.upper() == "YES":
        # If the user has watched Planet Hulk, call the watch_next() function
        watch_next(watch_status)
        break
    elif watch_status.upper() == "NO":
        # if the user hasn't watched Planet Hulk, call the watch_next() function with the watch status as an argument
        watch_next(watch_status)
        break
    else:
        print("Please enter a valid answer")
        watch_status = input("Hi there! Have you watched Planet Hulk? [Yes/No]")
