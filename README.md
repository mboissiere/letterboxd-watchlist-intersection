# Letterboxd Common Movies Finder

This Python script finds common movies in the watchlists of a group of Letterboxd users. It uses web scraping to fetch the watchlists and seen movies of each user.

## Inputs

The script takes the following inputs:

1. `usernames`: A list of Letterboxd usernames. Replace the placeholder usernames in the list with the usernames of your friends.

2. `N`: The number of top results to return. This is set to 100 by default, but you can change it to any number you like.

## Outputs

The script prints the following outputs:

1. The number of items in each user's watchlist.

2. The number of movies each user has seen.

3. The top `N` movies that appear most frequently in the users' watchlists, but have been seen by the fewest number of users. For each movie, it prints the movie's name, the number of watchlists it appears in, and the usernames of the users who have seen it.

## Goal

The goal of this script is to find movies that are of interest to a group of users, but have not been seen by most of them. This can be useful for planning movie nights or for finding movie recommendations.

## How to Run

To run the script, simply replace the placeholder usernames in the `usernames` list with the usernames of your friends, set the `N` variable to the number of results you want to return, and run the script. You will need to have the `requests` and `beautifulsoup4` libraries installed.
