def power_set_verbose(my_set):
    print(f"--- Starting power_set for {my_set} ---")
    n = len(my_set)
    power_set_size = 2**n
    print(f"Input set has {n} elements. Power set will have 2^{n} = {power_set_size} subsets.\n")
    
    result = []

    # The outer loop iterates from 0 to 2^n - 1. Each number represents a subset.
    for bit_counter in range(power_set_size):
        # Format the number as a binary string with leading zeros for clarity
        binary_representation = f"{bit_counter:0{n}b}"
        print(f"--- Outer Loop: Processing counter = {bit_counter} (binary: {binary_representation}) ---")
        
        sub_set = []    

        # The inner loop checks which elements to include for the current 'bit_counter'.
        for element_index in range(n):
            element = my_set[element_index]
            print(f"  > Inner Loop: Checking element '{element}' at index {element_index}")

            # This is the bitwise check
            mask = 1 << element_index
            binary_mask = f"{mask:0{n}b}"
            print(f"    - Creating mask for index {element_index}: 1 << {element_index} = {mask} (binary: {binary_mask})")
            
            # Perform the bitwise AND
            check_result = bit_counter & mask
            
            print(f"    - Checking if bit is set: ({bit_counter}) & ({mask})  -->  ({binary_representation}) & ({binary_mask})  =  {check_result}")

            if check_result > 0:
                print(f"    - YES. Bit is set. Adding '{element}' to the subset.")
                sub_set.append(element)
            else:
                print(f"    - NO. Bit is not set. Skipping '{element}'.")

        # After checking all elements for the current counter, add the new subset to the result
        print(f"  > Finished inner loop. Subset for counter {bit_counter} is: {sub_set}")
        result.append(sub_set)
        print(f"  Current Result list: {result}\n")

    print(f"--- Function Finished ---")
    return result

# Let's run it with a simple example ['a', 'b']
final_power_set = power_set_verbose(['a1', 'b2', 'c3'])
print(f"\nFINAL RETURNED VALUE: {final_power_set}")