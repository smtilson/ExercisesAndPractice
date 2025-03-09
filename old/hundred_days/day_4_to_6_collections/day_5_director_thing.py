from collections import namedtuple, defaultdict
import csv



MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
Director = namedtuple('Director', 'movies num_of_films avg_score')
from pprint import pprint

def get_movies_by_director():
    directors = defaultdict(list)
    with open(MOVIE_DATA) as fd:
        for row in csv.DictReader(fd):
            movie = Movie(title= row['movie_title'], year= row['title_year'], score=row['imdb_score'])
            directors[row['director_name']].append(movie)

    return directors

def filter_dict(directors: dict):
    print('filtering dict now')
    filtered_directors=defaultdict(list)
    for director, movies in directors.items():
        filtered_movies = []
        for movie in movies:
            if director == '':
                continue
            elif movie in filtered_movies:
                continue
            elif movie.year == '':
                filtered_movies.append(movie)
            elif int(movie.year) >= MIN_YEAR:
                filtered_movies.append(movie)
            else:
                continue
        if len(filtered_movies)>= 4:
            filtered_directors[director] = filtered_movies
    return filtered_directors

def get_average_scores(directors):
    for director, movies in directors.items():
        directors[director] = Director(movies=movies, avg_score= _calc_mean(movies),
                                     num_of_films= len(movies))
    return directors


def _calc_mean(movies):
    sum = 0

    for movie in movies:
        sum+=float(movie.score)

    return str(round(sum/len(movies), 1))

def sort_by_avg(dict):
    dict = sorted(dict.items(), key=lambda x: x[1].num_of_films, reverse = True)
    return dict

def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    sep_line = '-' * 60
    directors_list = sort_by_avg(directors)
    for i in range(20):
        director = directors_list[i]
        total_dead_space = 60-len(str(i+1)+'. '+director[0]+director[1].avg_score)
        print(str(i+1)+'. '+director[0]+' '*total_dead_space+director[1].avg_score)
        print(sep_line)
        for movies in director[1]:
            if type(movies) == list:
                movies.sort(key= lambda x: x.score, reverse = True)
                for movie in movies:
                    total_dead_space_per_movie = 60-len(movie.year+movie.title+movie.score)-1
                    print(movie.year+'-'+movie.title+' '*total_dead_space_per_movie+movie.score)
        print()
        print()



def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    #directors = get_average_scores(directors)
    #print_results(directors)
    directors = filter_dict(directors)
    directors = get_average_scores(directors)
    print_results(directors)

if __name__ == '__main__':
    main()