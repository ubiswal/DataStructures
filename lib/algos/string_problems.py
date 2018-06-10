# Split  string into possible substrings from a dictionary
def split_string(input_str, my_dict):
    num_ways = 0
    if input_str in my_dict:
        num_ways = 1
    my_str = ""
    for i in range(0, len(input_str)):
        my_str = my_str+input_str[i]
        if my_str in my_dict:
            num_ways = num_ways + split_string(input_str[i+1:], my_dict)
    return num_ways


def split_string_memoized(input_str, my_dict, memo):
    if input_str in memo:
        return memo[input_str]
    num_ways = 0
    if input_str in my_dict:
        num_ways = 1
    my_str = ""
    for i in range(0, len(input_str)):
        my_str = my_str+input_str[i]
        if my_str in my_dict:
            num_ways = num_ways + split_string_memoized(input_str[i+1:], my_dict, memo)
    memo[input_str] = num_ways
    return num_ways


# Check for balanced paratheses in an expresssion; it should exmamine whether the paors ad orders are correct
# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
def check_balanced_parantheses(input_str):
    brace1 = 0
    brace2 = 0
    brace3 = 0

    for i in range(0, len(input_str)):
        if input_str[i] == "{":
            brace1 = brace1+1
        elif input_str[i] == "[":
            brace2 = brace2+1
        elif input_str[i] == "(":
            brace3 = brace3+1

        if input_str[i] == "}":
            brace1 = brace1 - 1
        elif input_str[i] == "]":
            brace2 = brace2 - 1
        elif input_str[i] == ")":
            brace3 = brace3 - 1
        if brace1 < 0:
            return False
        if brace2 < 0:
            return False
        if brace3 < 0:
            return False

    return brace1 == 0 and brace2 == 0 and brace3 == 0

