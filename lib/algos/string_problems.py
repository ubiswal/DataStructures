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