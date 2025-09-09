
# HW5 - Search Engine

## Overview
**Origin:** This project was completed as an equivalent course to CSE 163 at UW.

**Learning objective:** Implement specialized data types with Python classes for tf-idf information retrieval.  

## Files and Tests
### Provided Files
* `search_engine.py` is the file representing the SearchEngine class as well as a command-line interface for using the SearchEngine.  
* `document.py` is the file representing a single document in the SearchEngine.  
* `hw5_test.py` is the file for you to put your own tests. The Run button executes this program.
* `cse163_utils.py` is a helper file that has code to help you test your code.   
* `test` is the folder for an initial sample of tests that will be run by the teacher. This shows another way you can write your tests that is more "industry standard". Do not add any tests to this folder, but if you want to follow this pattern you can add your own test folder with a different name instead of `hw5_test.py`

### Files to Submit

Submit the following Python files along with one or more "test corpus sub-directories":  
* `search_engine.py`  
* `document.py`  
* `hw5_test.py`
* `main.py`  
* `<my_test_corpus>`

You should create subdirectories with test files in them. Use these subdirectories in your tests. And, since your tests need to run on the teacher's machine, be sure to submit your new subdirectories.    

Please do **NOT** submit the following subdirectories. You may assume they exist on the teacher's machine:   
* small_text   
* test   
* test_corpus  

> You must submit your work as your teacher requires. Ask questions in class.   

### Test Tips
Try to break your search engine.  
Create test files that are target the type of tests you want to run. They should have content that is easy enough to verify.    

### Time Management

This assessment is very information-dense. Plan ahead by taking notes of what you need to do and where you will need to do it. It will probably help to get a global view of the entire assessment by reading **ALL** of the components before starting any coding—we expect students to spend at least 40 minutes reading, synthesizing, and planning before starting any coding.

### Video on TF-IDF
Watch the video of [Hunter Schafer](https://www.loom.com/share/118366e8ba1a427dad84870b869b660a?sid=d7353687-52cf-4ab3-a737-ed743bed0971).

## Deliverables
You are to create two different classes, `Document` and `SearchEngine`, that implement a Search Engine.  
You will create a `main.py` file that has console-based user interaction. It will prompt the user for a directory to use for the corpus of documents. The user may then enter any number of queries implemented by the `SearchEngine`. The results of the query will be output to the console. If the user enters an empty string, the program ends.  

`Document` will have an initializer and at least one public method:  
* `doc = Document(relative_path)` : Example code that creates a new `Document` initialized to an actual file.  
* `term_frequency(term)`: returns the TF value for the term for this document.  

`SearchEngine` will have an initializer and only one public method:  
* `se = SearchEngine(relative_path)` : Example code that creates a new `SearchEngine` initialized to a corpus of files found in the directory, `relative_path`.  
* `search(query)`: returns a list of document paths, relative to current working directory. The list is sorted by relevance (TF-IDF).  

## Main Output
Here is an example run of `main`. Note that your program will output only the first 10 document paths even while the `SearchEngine` returns a much longer list in its results.  

```
Please enter the name of a directory: small_text
Building Search Engine...

Enter a search term to query (Enter=Quit): Elvis
Displaying results for 'Elvis':
    1. small_text/Viacom - Wikipedia.txt
    2. small_text/Federal Bureau of Investigation - Wikipedia.txt
    3. small_text/Black or White - Wikipedia.txt
    4. small_text/List of songs recorded by The Jackson 5 - Wikipedia.txt
    5. small_text/Michael Jackson - Wikipedia.txt
    6. small_text/Game of Thrones - Wikipedia.txt

Enter a search term to query (Enter=Quit): Santa Claus 
Displaying results for 'Santa Claus':
    1. small_text/Jackson 5 Christmas Album - Wikipedia.txt
    2. small_text/ABC (The Jackson 5 album) - Wikipedia.txt
    3. small_text/Mountain View, California - Wikipedia.txt
    4. small_text/List of songs recorded by The Jackson 5 - Wikipedia.txt
    5. small_text/Mandalay Bay - Wikipedia.txt
    6. small_text/Michael Jackson - Wikipedia.txt
    7. small_text/Federal Bureau of Investigation - Wikipedia.txt
    8. small_text/Ubisoft - Wikipedia.txt
    9. small_text/Viacom - Wikipedia.txt
    10. small_text/Traditionalist conservatism - Wikipedia.txt

Enter a search term to query (Enter=Quit): notinanydocument
Displaying results for 'notinanydocument':
    No results :(
Enter a search term to query (Enter=Quit): Horrible Bosses in Schools
Displaying results for 'Horrible Bosses in Schools':
    1. small_text/Mountain View, California - Wikipedia.txt
    2. small_text/Hal Abelson - Wikipedia.txt
    3. small_text/Living with Michael Jackson - Wikipedia.txt
    4. small_text/Jeb Bush - Wikipedia.txt
    5. small_text/UNCF - Wikipedia.txt
    6. small_text/VH1 - Wikipedia.txt
    7. small_text/Hans-Hermann Hoppe - Wikipedia.txt
    8. small_text/William McKinley - Wikipedia.txt
    9. small_text/Steve Forbes - Wikipedia.txt
    10. small_text/Nintendo - Wikipedia.txt

Enter a search term to query (Enter=Quit): 
Thank you for searching.
```
## Context
A search engine is an algorithm that takes a query and retrieves the most relevant documents for that query. In order to identify the most relevant documents, our search engine will use term frequency–inverse document frequency (tf–idf), a text information statistic for determining the relevance of a term to each document from a corpus consisting of many documents.

The tf-idf statistic consists of two components: term frequency and inverse document frequency. Term frequency computes the number of times that a term appears in a document (such as a single Wikipedia page). If we were to use only the term frequency in determining the relevance of a term to each document, then our search result might not be helpful since most documents contain many common words such as “the” or “a”. In order to down-weight these common terms, the document frequency computes the number of times that a term appears across the corpus of all documents. The tf-idf statistic takes a term and a document and returns the term frequency divided by the document frequency.

In this assessment, we’ll implement two classes: a `Document` class to represent individual web pages and a `SearchEngine` class that aggregates the corpus of all `Document` objects. The `SearchEngine` builds on the `Document`, so be sure to fully complete the `Document` class before moving onto the `SearchEngine`.
  
## Normalizing Tokens
In this project we need to remove punctuation so that all tokens that are semantically
identical can be recognized as "_exactly_" identical. For example:
```
'Hello!' == 'hello'
```
`normalize_token` is a helper method found in the `cse163_utils.py` file.

Furthermore, in the handout it talks about
reading HTML files, only you'll discover that in this project there are no HTML files. Instead, I've already
stripped out all the `<tags>` and `<script>` for you. See below for a discussion on that.

The process of removing punctuation is called `normalization`. A quick an easy way to remove punctuation
is to use a [Regular Expression](https://docs.python.org/3/howto/regex.html) (more documentation [here](https://docs.python.org/3/library/re.html)). Regular
Expressions are used all over in Computer Science and you would benefit from learning
them. But, they can get complicated and they are out of scope for this class and project.
So, you get the code for free. [You're welcome!](https://youtu.be/79DijItQXMM)  

Just use the code that is found in `cse163_utils.py`.
```python
from cse163_utils import normalize_token
```

## Writing Tests
You need to write your own tests. The tests should be simple enough that you can calculate
expected values by hand. Do not assume your code is correct and use those values in your tests. 

Your tests need to be commented so that I can understand them. Describe what you're testing.
Develop "enough" tests that you feel confident that your code is working correctly. Your tests
cannot be a copy of the Unit Tests provided. Although, you can examine those to see what kinds
of things you might test. I'm not claiming that the Unit Tests in the `test` directory is
easy to read. I'm not saying those test exemplify good style. They are tests that UW provided
and I used them "out of the box."

**IMPORTANT**: `hw5_test.py` needs to follow the Main-Pattern.

### Test Methods
Write many smaller test methods. For example: do NOT write a single method for all of Document.
You should have at least one test method for each public method on the object. 
> For example, Document has: `get_path`, `get_words`, `term_frequency`.

And, there should be a test method for every "important" private method on the object.

> Example: SearchEngine has `_calculate_idf`

The system will run one large Unit Test. It actually runs a bunch of tests in the `test` directory using the files in the `test_corpus` directory. This is not the
preferred Unit Test to have. It is provided to you as a Safety Check only. You need to write your own tests. The provided tests do not test every case!

These tests are a gift to help you get extra verification that your code is working. More tests will be run during grading.

### Do Not Change...
Do not add, change or remove anything from the files in these directories.
Furthermore, do not add files to these directories:
* test
* test_corpus
* small_text

Do not change `cse163_utils.py`. Do NOT add any method to this file either!
