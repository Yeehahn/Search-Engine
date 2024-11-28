import math
import re


def normalize_token(token):
    """
    This will normalize a token to all lower case and eliminate all
    punctuation and numbers. However, if a token is only numbers, then
    we eliminate everything except for numbers.
    """
    token = token.lower()
    # try eliminating everything except a-z
    term = re.sub(r"[^a-z]+", "", token)
    # if we removed everything, try keeping only numbers
    if len(term) == 0:
        # replace everything that is not 0-9 and not .
        term = re.sub(r"[^0-9\\.]+", "", token)
    return term


def normalize_paths(paths):
    """
    paths is a list of relative paths to documents.
    return a normalized list of relatie paths.

    Replace all whacks with slashes so that the results we
    get on Windows or Macs can be compared to the same
    string literals.
    """
    # allow this method to work with a list of paths
    # and just a single path
    if paths is list:
        return [re.sub(r'\\+', '/', file) for file in paths]
    return re.sub(r'\\+', '/', paths)


def check_approx_equals(expected, received):
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    try:
        if isinstance(expected, dict):
            # first check that keys match, then check that the
            # values approximately match
            return expected.keys() == received.keys() and \
                all([check_approx_equals(expected[k], received[k])
                    for k in expected.keys()])
        elif isinstance(expected, list):
            # Checks that lists contain the same values and same order
            return len(expected) == len(received) and \
                all([check_approx_equals(v1, v2)
                    for v1, v2 in zip(expected, received)])
        elif isinstance(expected, float):
            return math.isclose(expected, received, abs_tol=0.001)
        else:
            return expected == received
    except Exception as e:
        print(f'EXCEPTION: Raised when checking check_approx_equals {e}')
        return False


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    assert check_approx_equals(expected, received), \
        f'Failed: Expected {expected}, but received {received}'
