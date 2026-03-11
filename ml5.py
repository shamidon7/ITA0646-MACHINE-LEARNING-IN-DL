import math

# 1. Sample Dataset (Petal Length, Petal Width, Label)
# 0 = Setosa, 1 = Versicolor
train_data = [
    [1.4, 0.2, 0], [1.3, 0.2, 0], [1.5, 0.2, 0], # Setosa
    [4.7, 1.4, 1], [4.5, 1.5, 1], [4.9, 1.5, 1]  # Versicolor
]

# New data point we want to classify
new_point = [4.6, 1.4] 
k = 3

# 2. Calculate Euclidean Distance
def euclidean_distance(p1, p2):
    distance = 0
    for i in range(len(p1)):
        distance += (p1[i] - p2[i]) ** 2
    return math.sqrt(distance)

# 3. Find the 'K' Nearest Neighbors
distances = []
for row in train_data:
    # row[:-1] is the features, row[-1] is the label
    dist = euclidean_distance(new_point, row[:-1])
    distances.append((dist, row[-1]))

# Sort by distance (closest first)
distances.sort(key=lambda x: x[0])
neighbors = distances[:k]

# 4. Voting
votes = [n[1] for n in neighbors]
prediction = max(set(votes), key=votes.count)

print(f"New Point: {new_point}")
print(f"Nearest {k} Neighbors (Distance, Label): {neighbors}")
print(f"Final Prediction: {'Versicolor' if prediction == 1 else 'Setosa'}")
