# Min_max Algorithm in Python

def min_max(depth, node_index, is_max, scores, height):

    # If we reach a leaf node
    if depth == height:
        return scores[node_index]

    if is_max:
        # MAX player chooses maximum value
        left = min_max(depth + 1, node_index * 2,
                       False, scores, height)

        right = min_max(depth + 1, node_index * 2 + 1,
                        False, scores, height)

        return max(left, right)

    else:
        # MIN player chooses minimum value
        left = min_max(depth + 1, node_index * 2,
                       True, scores, height)

        right = min_max(depth + 1, node_index * 2 + 1,
                        True, scores, height)

        return min(left, right)


# ---------------- USER INPUT ----------------

n = int(input("Enter number of leaf nodes: "))

scores = []

print("\nEnter the values of leaf nodes:")

for i in range(n):
    value = int(input(f"Value {i + 1}: "))
    scores.append(value)


# Calculate height of the binary tree
height = 0
temp = n

while temp > 1:
    temp = temp // 2
    height += 1


# Run Min_max Algorithm
result = min_max(0, 0, True, scores, height)

print("\nBest value using Min_max:", result)
