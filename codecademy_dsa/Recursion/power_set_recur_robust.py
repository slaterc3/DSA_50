def power_set_robust(my_list):
    """
    The main function that the user calls. It starts the recursive
    process by calling the helper function with an initial depth of 0.
    """
    print("=====================================================")
    print(f"Starting power_set_robust for input: {my_list}")
    print("=====================================================\n")
    return _power_set_helper(my_list, depth=0)

def _power_set_helper(my_list, depth):
    """
    The internal helper function that does the real work and tracks
    the recursion depth for clear print statements.
    """
    # Create an indentation string based on the current depth
    indent = "  " * depth

    # --- On Function Entry ---
    print(f"{indent}---> Entering power_set for my_list = {my_list} at depth {depth}")

    # --- Base Case ---
    if len(my_list) == 0:
        print(f"{indent}    ** BASE CASE HIT **")
        print(f"{indent}<--- Exiting at depth {depth}, returning: [[]]")
        return [[]]

    # --- Recursive Step ---
    first_element = my_list[0]
    rest_of_list = my_list[1:]
    print(f"{indent}    First element: '{first_element}'")
    print(f"{indent}    Rest of list: {rest_of_list}")
    print(f"{indent}    RECURSIVE CALL: Calling power_set for {rest_of_list}")

    # The recursive call, passing the rest of the list and incrementing the depth
    power_set_without_first = _power_set_helper(rest_of_list, depth + 1)
    
    print(f"{indent}    ...Back at depth {depth}. Recursive call has returned.")
    print(f"{indent}    `power_set_without_first` is now: {power_set_without_first}")

    # --- Deconstructing the List Comprehension ---
    print(f"{indent}    Now, building the 'with_first' list by adding '{first_element}' to each of those subsets...")
    with_first = []
    # This is the equivalent of: `[ [first_element] + rest for rest in power_set_without_first ]`
    for rest in power_set_without_first:
        print(f"{indent}      - Processing subset: {rest}")
        new_subset = [first_element] + rest
        print(f"{indent}        - Creating new subset: {new_subset}")
        with_first.append(new_subset)
    
    print(f"{indent}    Finished building. `with_first` is now: {with_first}")

    # --- The Final Combination ---
    print(f"{indent}    Combining `with_first` and `power_set_without_first`...")
    print(f'with_first: {with_first}')
    print(f'ps_without_first: {power_set_without_first}')
    final_result = with_first + power_set_without_first

    # --- On Function Exit ---
    print(f"{indent}<--- Exiting at depth {depth}, returning: {final_result}")
    return final_result

# --- Let's run it with a smaller list to keep the output manageable ---
universities = ['a', 'b']
power_set_robust(universities)