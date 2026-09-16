# ============================================================
# MINIMAX ALGORITHM WITH USER INPUT
# ============================================================

def get_children(state):
    """Return the successor states associated with a state."""
    return state.get("children", [])


def is_terminal(state):
    """Return whether a state has no possible successor states."""
    return not get_children(state)


def evaluate(state):
    """Return the heuristic value of a terminal state."""
    return state.get("value", 0)


def minimax(state, depth, maximizing_player):

    # Base condition
    if depth == 0 or is_terminal(state):
        return evaluate(state)

    # Maximizing player
    if maximizing_player:

        max_eval = float('-inf')

        for child in get_children(state):

            eval_value = minimax(
                child,
                depth - 1,
                False
            )

            max_eval = max(
                max_eval,
                eval_value
            )

        return max_eval

    # Minimizing player
    else:

        min_eval = float('inf')

        for child in get_children(state):

            eval_value = minimax(
                child,
                depth - 1,
                True
            )

            min_eval = min(
                min_eval,
                eval_value
            )

        return min_eval


# ============================================================
# CREATE GAME TREE USING USER INPUT
# ============================================================

def create_tree(depth, current_depth=0):

    # If we have reached the leaf level,
    # ask the user for the value
    if current_depth == depth:

        value = int
            input(
                f"Enter value for leaf node "
                f"{current_depth}: "
            )
        )

        return {
            "value": value,
            "children": []
        }

    # Ask number of children
    number_of_children = int(
        input(
            f"Enter number of children for "
            f"level {current_depth}: "
        )
    )

    children = []

    for i in range(number_of_children):

        print(
            f"\nCreating child {i + 1} "
            f"of level {current_depth}"
        )

        child = create_tree(
            depth,
            current_depth + 1
        )

        children.append(child)

    return {
        "children": children
    }


# ============================================================
# MAIN PROGRAM
# ============================================================

print("=" * 60)
print("              MINIMAX ALGORITHM")
print("=" * 60)

# Get depth from user
depth = int(
    input("Enter depth of the game tree: ")
)

print()

print(
    "Enter the number of children at each level."
)

print(
    "At the last level, enter the leaf values."
)

print()

# Create tree
root = create_tree(depth)


# ============================================================
# CHOOSE STARTING PLAYER
# ============================================================

print()

choice = input(
    "Who starts? Enter MAX or MIN: "
).upper()

if choice == "MAX":

    maximizing_player = True

elif choice == "MIN":

    maximizing_player = False

else:

    print("Invalid choice!")

    exit()


# ============================================================
# APPLY MINIMAX
# ============================================================

result = minimax(
    root,
    depth,
    maximizing_player
)


# ============================================================
# DISPLAY RESULT
# ============================================================

print()
print("=" * 60)

print("MINIMAX RESULT")

print("=" * 60)

print(
    "Starting Player :",
    choice
)

print(
    "Tree Depth      :",
    depth
)

print(
    "Optimal Value   :",
    result
)

print("=" * 60)