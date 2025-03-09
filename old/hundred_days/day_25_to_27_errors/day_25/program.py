import api
import requests.exceptions

def main():
    keyword = input('Keyword of title search: ')

    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        results.sort(key= lambda x: x.imdb_score, reverse = True)
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("There is an error with your connection.")
    except ValueError as x:
        print(x)
    except Exception as x:
        print(type(x))
        print(f"There is a {x}.")

if __name__ == '__main__':
    main()