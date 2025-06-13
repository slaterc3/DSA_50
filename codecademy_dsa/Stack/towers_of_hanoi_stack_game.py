from codecademy_dsa.Stack.stack import Stack # Assuming your Stack class is in a file named stack.py

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game
num_disks = 0
while num_disks < 3: # Corrected loop for initial input
    try:
        num_disks = int(input("\nHow many disks do you want to play with? (minimum 3)\n"))
        if num_disks < 3:
            print("Please enter a number of disks greater than or equal to 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Push disks onto the left stack
for i in range(num_disks, 0, -1):
    left_stack.push(i)

# Display initial state (optional, but good for debugging)
print("\n--- Initial Stacks ---")
for stack in stacks:
    print(f"{stack.get_name()}:")
    stack.print_items()

num_optimal_moves = (2**num_disks) - 1
print(f"\nFastest way to solve is in {num_optimal_moves} moves")

# Get User Input
def get_input_stack(): # Renamed to avoid conflict with Python's input()
    choices = {} # Use a dictionary for easier lookup
    for stack in stacks:
        choices[stack.get_name()[0].upper()] = stack # Map first letter (uppercase) to stack object

    while True:
        print('\nHere are the Choices:')
        for key, stack_obj in choices.items():
            print(f'Enter "{key}" for {stack_obj.get_name()}')
        
        user_input = input("").upper()
        
        if user_input in choices:
            # print(f'You chose {choices[user_input].get_name()}') # Moved to main game loop
            return choices[user_input]
        else:
            print("Invalid choice. Please enter 'L', 'M', or 'R'.")


# Play the Game
num_user_moves = 0 

while right_stack.get_size() < num_disks: # Game continues until all disks are on the right stack
    print('\n\n\n...Current Stacks...')
    for stack in stacks:
        print(f"{stack.get_name()}:") # Print stack name before items
        stack.print_items()
    print("-" * 20) # Separator for readability

    from_stack = None
    to_stack = None

    while True: # Loop until a valid move selection is made
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input_stack() # Use the renamed function

        print('\nWhich stack do you want to move to?\n') # Corrected newline character
        to_stack = get_input_stack() # Use the renamed function

        # Move logic
        if from_stack.is_empty():
            print('\nInvalid move: The source stack is empty. Try again.')
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            # Valid move: either destination is empty, or disk on source is smaller
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1 
            break # Exit inner loop, valid move made
        else:
            print('\nInvalid move: Cannot place a larger disk on a smaller disk. Try again.')
            # No break here, as the move was invalid, so it prompts for input again.

print(f'\n\nCongratulations! You completed the game in {num_user_moves} moves.')
if num_user_moves == num_optimal_moves:
    print("You found the optimal solution!")
else:
    print(f"The optimal number of moves was {num_optimal_moves}. Keep practicing!")