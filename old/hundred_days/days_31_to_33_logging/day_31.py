import api
import requests.exceptions
import logbook
import sys


app_log = logbook.Logger('app')

def main():
    keyword = input('Keyword of title search: ')

    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        results.sort(key= lambda x: x.imdb_score, reverse = True)
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
        app_log.trace(f'Search Successful: keyword: {keyword}, {len(results)} results.')
    except requests.exceptions.ConnectionError:
        msg = "There is an error with your connection."
        print(msg)
        app_log.warn(msg)
    except ValueError as x:
        print(x)
        app_log.warn(x)

    except Exception as x:
        print(type(x))
        print(f"There is a {x}.")
        app_log.exception(x)


def init_logging(filename: str = None):
    level = logbook.TRACE
    if filename:
        logbook.TimedRotatingFileHandler(filename, level = level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level = level).push_application()

    msg = f'Logging initialized, level: {level}, mode: {"stdout mode" if not filename else "file mode: " + filename}'
    logger = logbook.Logger('startup')
    logger.notice(msg)
if __name__ == '__main__':
    init_logging('movie_app.log')
    main()