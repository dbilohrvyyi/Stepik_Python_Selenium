'''
Create a function using f-Strings Style and assert mechanism to find substring in string
'''

########### My resolution ###############


def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

test_substring('fulltext', 'text')
