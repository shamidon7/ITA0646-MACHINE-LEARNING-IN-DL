# Training data
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Number of attributes
num_attributes = len(data[0]) - 1

# Initialize S and G
S = ['0'] * num_attributes
G = [['?'] * num_attributes]

print("Initial S:", S)
print("Initial G:", G)

for example in data:
    attributes = example[:-1]
    label = example[-1]

    if label == 'Yes':  # Positive example
        
        # Remove inconsistent hypotheses from G
        G = [g for g in G if all(g[i] == '?' or g[i] == attributes[i] for i in range(num_attributes))]

        # Generalize S
        for i in range(num_attributes):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'

    else:  # Negative example
        
        # Specialize G
        new_G = []
        for g in G:
            for i in range(num_attributes):
                if g[i] == '?':
                    new_hypothesis = g.copy()
                    new_hypothesis[i] = S[i]
                    if new_hypothesis not in new_G:
                        new_G.append(new_hypothesis)
        G = new_G

    print("\nAfter example:", example)
    print("S:", S)
    print("G:", G)

print("\nFinal Specific Boundary S:", S)
print("Final General Boundary G:", G)
