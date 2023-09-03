import random

# Function generates scores from the range of 1500
def generate_scores(num_scores):
    scores = []
    for _ in range(num_scores):
        score = random.randint(51, 100)
        scores.append(score)
    return scores

# Determines what scores are A and calculates the percentage of them in the class
def calculate_percentage_a_scores(scores):
    a_scores = [score for score in scores if score >= 90]
    percentage = (len(a_scores) / len(scores)) * 100
    return percentage

#Determines the probability of getting an A
def calculate_probability_of_A(scores):
    a_scores = [score for score in scores if score >= 90]
    probability = (len(a_scores) / len(scores))
    return probability

# Generate 1,500 scores
num_scores = 1500
scores = generate_scores(num_scores)

# Calculates the percentage and probability of A scores
percentage_a_scores = calculate_percentage_a_scores(scores)
probability_a_score = calculate_probability_of_A(scores)

# Prints the first 30 generated scores
print("First 30 generated scores:")
print(scores[:30])

# Prints the percentage of A scores
print(f"Percentage of A scores: {percentage_a_scores:.1f}%")

# Prints the probability of getting an A
print(f"Probability of getting an A: {probability_a_score:.1f}")
