def fibonacci_memo(n):
    """
    The wrapper function that the user calls. It sets up the cache
    and calls the recursive helper function.
    """
    cache = {}  # 1. Create the cache for this specific run

    def fib_helper(n):
        """The internal recursive function that uses the cache."""

        # 2. Check the cache first! This is the "memoization" step.
        if n in cache:
            return cache[n]

        # Base case is the same as before
        if n == 1 or n == 0:
            return n

        # Recursive step is the same, but we use the helper function
        result = fib_helper(n - 1) + fib_helper(n - 2)

        # 3. Save the newly computed result to the cache before returning
        cache[n] = result
        return result

    return fib_helper(n)

# --- Let's run it ---
print(f"fibonacci_memo(10) = {fibonacci_memo(10)}")
print(f"fibonacci_memo(35) = {fibonacci_memo(35)}") # This would be very slow without memoization