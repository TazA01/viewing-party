from statistics import mode 


# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.



# ### Wave 4

# 1. Create a function named `get_available_recs`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies

# ### Wave 5

# 1. Create a function named  `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

# 2. Create a function named  `get_rec_from_favorites`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies



# ------------- WAVE 1 --------------------

from itertools import count


def create_movie(title, genre, rating):
    movie_dict={}
    if not title or not genre or not rating:
        return None
    else: 
        movie_dict["title"]=title
        movie_dict["genre"]=genre
        movie_dict["rating"]=rating
    print(movie_dict)
    return movie_dict


def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data,title):
    
    for val in user_data["watchlist"]:
        for i in val.values():
            if i==title:
                user_data["watchlist"].remove(val)
                user_data["watched"]=[val]
            
    return user_data

watch_movie({
        "watchlist": [{
            "title": "It Came from the Stack Trace",
            "genre": "Horror",
            "rating": 3.5
        }],
        "watched": []
    },"It Came from the Stack Trace")




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    count_of_ratings=0
    sum_of_ratings=0
    for list in user_data["watched"]:
        for rate,score in list.items():
            if rate=="rating":
                count_of_ratings+=1
                sum_of_ratings+=score
    if count_of_ratings==0:
        average=0
    else:
        average=sum_of_ratings/count_of_ratings
    return average



def get_most_watched_genre(user_data):
    genre_data=[]
   
    for list in user_data.values():
        for movie in list:
            if "genre" in movie:
                genre_data.append(movie["genre"])
    if len(genre_data)==0:
        most_often=None
    else: 
        most_often=mode(genre_data)
    return(most_often)

get_most_watched_genre({"watched":[{
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
},{
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}, {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
},{
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
}]})



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# 1. Create a function named `get_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies

def get_unique_watched(user_data):
    


# 2. Create a function named `get_friends_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------