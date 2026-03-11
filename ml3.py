import math

# 1. Sample Dataset (Petal Length, Petal Width, Label: 0=Setosa, 1=Versicolor)
# [Petal Length, Petal Width, Class]
data = [
    [1.4, 0.2, 0], [1.3, 0.2, 0], [1.5, 0.2, 0],
    [4.7, 1.4, 1], [4.5, 1.5, 1], [4.9, 1.5, 1]
]

# 2. Function to calculate Entropy: H(S) = -Σ p(x) log2 p(x)
def calculate_entropy(labels):
    if not labels:
        return 0
    total = len(labels)
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# 3. Calculate Information Gain
def information_gain(parent_labels, child_labels_list):
    parent_entropy = calculate_entropy(parent_labels)
    
    weighted_child_entropy = 0
    total_samples = len(parent_labels)
    
    for child_labels in child_labels_list:
        weight = len(child_labels) / total_samples
        weighted_child_entropy += weight * calculate_entropy(child_labels)
    
    return parent_entropy - weighted_child_entropy

# 4. A simple "Split" logic
# For this example, we split the data based on a threshold (length > 2.0)
labels = [row[2] for row in data]
left_split = [row[2] for row in data if row[0] <= 2.0]
right_split = [row[2] for row in data if row[0] > 2.0]

gain = information_gain(labels, [left_split, right_split])

print(f"Parent Entropy: {calculate_entropy(labels):.4f}")
print(f"Information Gain from splitting at 2.0: {gain:.4f}")

if gain > 0:
    print("Decision: Split here! This creates 'pure' nodes.")
	
