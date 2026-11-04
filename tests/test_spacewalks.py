from eva_data_analysis import text_to_duration

# def test_text_to_duration_no_minutes():
#     actual = text_to_duration("10:00")
#     expected = 10.00

#     if (actual == expected):
#         print("Pass")
#     else:
#         print("Fail")

# def test_text_to_duration_minutes():
#     actual = text_to_duration("10:30")
#     expected = 10.50

#     if (actual == expected):
#         print("Pass")
#     else:
#         print("Fail")

## use python

# only gives results for failing tests

def test_text_to_duration_no_minutes():
    actual = text_to_duration("10:00")
    expected = 10.00
    assert(actual == expected)

def test_text_to_duration_minutes():
    actual = text_to_duration("10:30")
    expected = 10.50
    assert(actual == expected)

# test_text_to_duration_no_minutes()
# test_text_to_duration_minutes()

# the calls are not usually used, as it gives very hard to interpret messages

# use python tool - pytest
# Convention over configuration
# all files must start with test_
# all test functions must start with test_