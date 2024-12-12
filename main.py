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
    
    user_input = input('Enter a search term to query (Enter=Quit): ')
    while user_input != '':
        


if __name__ == '__main__':
    main()