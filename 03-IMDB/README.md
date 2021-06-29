# Challenge - IMDB

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/1200px-IMDB_Logo_2016.svg.png?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80)

## Objectives

Web scrapping on the Internet Movie Database

## Guidelines

Write a Python script to download [IMDB 250 Top Rated Movies](https://www.imdb.com/chart/top). For each movie, you'll need to retrieve the movie title, the ranking, the initial release year, the casting and the rating.

Your data must be stored in a proper `imdb_top_250.csv` file in the `output` folder. The content of the file shoul look like this:
```
1 - The Shawshank Redemption (1994) - Starring: Frank Darabont (dir.), Tim Robbins, Morgan Freeman
2 - The Godfather (1972) - Starring: Francis Ford Coppola (dir.), Marlon Brando, Al Pacino
3 - The Godfather: Part II (1974) - Starring: Francis Ford Coppola (dir.), Al Pacino, Robert De Niro
4 - The Dark Knight (2008) - Starring: Christopher Nolan (dir.), Christian Bale, Heath Ledger
5 - 12 Angry Men (1957) - Starring: Sidney Lumet (dir.), Henry Fonda, Lee J. Cobb
6 - Schindler's List (1993) - Starring: Steven Spielberg (dir.), Liam Neeson, Ralph Fiennes
```

Your code must be written in `src/imdb.py`.

### Bonus

Immplement a Movie class with the appropriate attributes and methods to store your movie informations.
