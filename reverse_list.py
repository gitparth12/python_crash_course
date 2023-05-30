def reverse_list(original_list):
    # Base case
    if (original_list is None or len(original_list) <= 0):
        return []
    
    # Recursive case
    recurse_result = reverse_list(original_list[1:])
    # Combine
    recurse_result.append(original_list[0])
    
    return recurse_result

if "__main__" == __name__:
    original_list = [i for i in range(10)]
    print(original_list)

    print(reverse_list(original_list))