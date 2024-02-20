import requests
from bs4 import BeautifulSoup

# Parameters that can be subject to change
usernames = ["username1", "username2"] # Replace with your friends' usernames
N = 100  # Number of results to return

def get_watchlist(username):
    page = 1
    movie_names = []

    while True:
        url = f"https://letterboxd.com/{username}/watchlist/page/{page}/"
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')
        movie_elements = soup.select("img.image")  # Select img tags with class 'image'

        if not movie_elements:
            break

        movie_names += [element.get('alt') for element in movie_elements]

        # Check if there is a next page
        next_page = soup.select_one('a.next')
        if not next_page:
            break

        page += 1

    print(f"Number of items in {username}'s watchlist: {len(movie_names)}")
    return movie_names

def get_seen_films(username):
    page = 1
    movie_names = []

    while True:
        url = f"https://letterboxd.com/{username}/films/page/{page}/"
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, "html.parser")
        movie_elements = soup.select("img.image")  # Select img tags with class 'image'

        if not movie_elements:
            break

        movie_names += [element.get('alt') for element in movie_elements]

        # Check if there is a next page
        next_page = soup.select_one('a.next')
        if not next_page:
            break

        page += 1

    print(f"Number of movies {username} has seen: {len(movie_names)}","\n")
    return movie_names

def find_common_movies(usernames):
    movie_counts = {}
    seen_movies = {}
    for username in usernames:
        watchlist = get_watchlist(username)
        seen_movies[username] = get_seen_films(username)
        for movie in watchlist:
            if movie in movie_counts:
                movie_counts[movie] += 1
            else:
                movie_counts[movie] = 1

    # Calculate the score for each movie
    movie_scores = {}
    for movie, count in movie_counts.items():
        seen_by = len([username for username in usernames if movie in seen_movies[username]])
        movie_scores[movie] = count - seen_by

    return movie_scores, seen_movies

# Example usage
movie_scores, seen_movies = find_common_movies(usernames)

# Sort the movies by their score in descending order
sorted_movies = sorted(movie_scores.items(), key=lambda item: item[1], reverse=True)

# Print the top N results
for movie, score in sorted_movies[:N]:
    watchlist_count = score + len([username for username in usernames if movie in seen_movies[username]])
    seen_by = [username for username in usernames if movie in seen_movies[username]]
    watchlist_str = "" if watchlist_count == 1 else "s"
    if len(seen_by) == 1:
        print(f"{movie} appears in {watchlist_count} watchlist{watchlist_str}, but {seen_by[0]} has seen it")
    elif len(seen_by) > 1:
        last_person = seen_by.pop()
        print(f"{movie} appears in {watchlist_count} watchlist{watchlist_str}, but {', '.join(seen_by)} and {last_person} have seen it")
    else:
        print(f"{movie} appears in {watchlist_count} watchlist{watchlist_str}, and nobody has seen it!")