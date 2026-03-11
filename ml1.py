import csv

# Training data
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Number of attributes
num_attributes = len(data[0]) - 1

# Initialize hypothesis with first positive example
hypothesis = ['0'] * num_attributes

print("Initial Hypothesis:", hypothesis)

for example in data:
    if example[-1] == 'Yes':  # Consider only positive examples
        for i in range(num_attributes):
            if hypothesis[i] == '0':
                hypothesis[i] = example[i]
            elif hypothesis[i] != example[i]:
                hypothesis[i] = '?'
        print("Updated Hypothesis:", hypothesis)

print("\nFinal Hypothesis:", hypothesis)
