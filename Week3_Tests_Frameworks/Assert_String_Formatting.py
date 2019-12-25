'''
Create a function using f-Strings Style to compare expected and actual results within assert operator
'''

########### My resolution ###############

def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, f"expected {expected_result}, got {actual_result}"

test_input_text(11, -11)