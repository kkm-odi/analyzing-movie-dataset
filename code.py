# --------------
from csv import reader

def explore_data(dataset, start, end, rows_and_columns=False):

    
    
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
     


def duplicate_and_unique_movies(dataset, index_):
    
    duplicate = []
    unique = []

    for movie in dataset:
        name = movie[index_]
        if name in unique:
            duplicate.append(name)
        else:
            unique.append(name)

    print('Number of duplicate Movies:', len(duplicate))
    print('\n')
    print('Examples of duplicate Movies:', duplicate[:15])
    



def movies_lang(dataset, index_, lang_):
   
    movies_ = []

    for movie in movies:
        lang = movie[index_]
        if lang == lang_:
            movies_.append(movie)

    print("Examples of Movies in English Language:")    
    explore_data(movies_, 0, 3, True)
    return movies_
    


def rate_bucket(dataset, rate_low, rate_high):


    rated_movies = []

    for movie in dataset:
        vote_avg = float(movie[-4])
        if ((vote_avg >= rate_low) & (vote_avg <= rate_high)):
            rated_movies.append(movie)

    print("Examples of Movies in required rating bucket:")    
    explore_data(rated_movies, 0, 3, True)
    return rated_movies


# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)

# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies[0]
print("Movies Header:\n", movies_header)

# Subset the movies dataset such that the header is removed from the list and store it back in movies
movies = movies[1:]



# Delete wrong data
# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.

print("Entry at index 4553:")
explore_data(movies, 4553, 4554)

del movies[4553]




# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
print("First 5 Entries:")
explore_data(movies, 0, 5, True)



# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.

duplicate_and_unique_movies(movies, 13)


# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.

reviews_max = {}

for movie in movies:
    name = movie[13]
    n_reviews = float(movie[12])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews
        
len(reviews_max)

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 

movies_clean = []
already_added = []

for movie in movies:
    name = movie[13]
    n_reviews = float(movie[12])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        movies_clean.append(movie)
        already_added.append(name)
        
len(movies_clean)



# Calling movies_lang(), extract all the english movies and store it in movies_en.

movies_en = movies_lang(movies_clean, 3, 'en')



# Call the rate_bucket function to see the movies with rating higher than 8.

high_rated_movies = rate_bucket(movies_en, 8, 10)




