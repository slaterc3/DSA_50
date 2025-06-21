def move_to_end(lst, val):
  result = [] # Initialize an empty list for the current call's result

  # Base Case 1: If the input list is empty, there's nothing to move.
  # This is crucial to stop the recursion.
  if len(lst) == 0:
    return []

  # Recursive Step: Check the first element of the current list (lst[0])

  # Case 1: The first element IS the value we want to move
  if lst[0] == val:
    # 1. Recursively call move_to_end on the REST of the list (lst[1:])
    #    This call will handle moving 'val' to the end in the *remainder* of the list.
    result += move_to_end(lst[1:], val)
    # 2. AFTER the recursive call returns, append the current element (lst[0])
    #    to the end of the 'result' list. This ensures it ends up at the end.
    result.append(lst[0])

  # Case 2: The first element IS NOT the value we want to move
  else:
    # 1. Append the current element (lst[0]) to the 'result' list immediately.
    #    This element should retain its relative order at the beginning.
    result.append(lst[0])
    # 2. Recursively call move_to_end on the REST of the list (lst[1:])
    #    and extend the 'result' with whatever that call returns.
    #    This ensures the rest of the list is processed and appended.
    result += move_to_end(lst[1:], val)

  return result