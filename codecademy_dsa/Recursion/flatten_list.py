def flatten_verbose(my_list):
    """
    The main function that starts the process. It calls the helper
    with an initial depth of 0 for clean printing.
    """
    print("=====================================================")
    print(f"Starting flatten_verbose for input: {my_list}")
    print("=====================================================\n")
    return _flatten_helper(my_list, depth=0)

def _flatten_helper(my_list, depth):
    """
    The internal recursive function that does the work and prints
    detailed trace information at each step.
    """
    # Create an indentation string based on the current depth
    indent = "  " * depth

    # --- On Function Entry ---
    print(f"{indent}---> Entering flatten() for my_list = {my_list} at depth {depth}")
    
    # Each function call has its OWN local result list
    result = []
    print(f"{indent}    Local `result` list created: []")

    # --- Loop Through Elements ---
    for element in my_list:
        print(f"{indent}    - Processing element: {element}")

        # --- Check if the element is a list ---
        if isinstance(element, list):
            print(f"{indent}      - Element is a LIST. Making a recursive call.")
            
            # --- Recursive Step ---
            flat_list = _flatten_helper(element, depth + 1)
            
            print(f"{indent}      ...Back at depth {depth}. Recursive call returned: {flat_list}")
            print(f"{indent}      - Adding these elements to my local `result`.")
            result += flat_list
            print(f"{indent}      - `result` is now: {result}")
        else:
            print(f"{indent}      - Element is NOT a list. Appending it directly.")
            
            # --- Base Case Action ---
            result.append(element)
            print(f"{indent}      - `result` is now: {result}")

    # --- On Function Exit ---
    print(f"{indent}<--- Loop finished for this level. Exiting at depth {depth}, returning: {result}")
    return result

# --- Let's run it with the planets list ---
nested_planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus']
flattened_planets = flatten_verbose(nested_planets)

print("\n=====================================================")
print("Final result returned to the main script:")
print(flattened_planets)
print("=====================================================")