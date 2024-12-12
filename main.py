"""
Yeehahn Wang-Liu
Intermediate Data Programming

Description:
    This program runs the search engine, taking user input
    from search_engine import SearchEngine
"""
from search_engine import SearchEngine


def main():
    path = input('Please enter the name of a directory: ')
    print('Building Search Engine...')
    engine = SearchEngine(path)

    search = input('Enter a search term to query (Enter=Quit): ')
    while search != '':
        results = engine.search(search)
        print('Displaying results for \'' + search + '\':')
        for i in range(min(len(results), 10)):
            print(f'    {i + 1}. {results[i]}')
        print()
        search = input('Enter a search term to query (Enter=Quit): ')


if __name__ == '__main__':
    main()