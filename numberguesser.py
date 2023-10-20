import random

class MarkovChain:
    def __init__(self):
        self.transition_matrix = {}  # Transition probabilities between numbers
        self.current_state = None

    def train(self, data):
        # Calculate transition probabilities
        for sequence in data:
            for i in range(len(sequence) - 1):
                current_num = sequence[i]
                next_num = sequence[i + 1]

                if current_num not in self.transition_matrix:
                    self.transition_matrix[current_num] = {}

                if next_num not in self.transition_matrix[current_num]:
                    self.transition_matrix[current_num][next_num] = 1
                else:
                    self.transition_matrix[current_num][next_num] += 1

        # Normalize transition probabilities
        for current_num, next_nums in self.transition_matrix.items():
            total_transitions = sum(next_nums.values())
            for next_num in next_nums:
                self.transition_matrix[current_num][next_num] /= total_transitions

    def predict_next(self, current_input):
        if current_input in self.transition_matrix:
            next_probabilities = self.transition_matrix[current_input]
            next_input = max(next_probabilities, key=next_probabilities.get)
        else:
            # If there's no history for the current input, make a random guess
            next_input = random.choice([1, 2, 3, 4, 5, 6])

        return next_input

# Example usage
if __name__ == "__main__":
    # Simulated user input data
    user_data = [
        [1, 2, 3, 4, 5, 6],
        [2, 4, 1, 5, 3],
        [1, 3, 5, 2],
        [4, 6, 3, 2, 1],
    ]

    markov_model = MarkovChain()
    markov_model.train(user_data)

    current_input = random.choice([1, 2, 3, 4, 5, 6])  # Start with a random input

    total_attempts = 0
    correct_predictions = 0

    while True:
        print(f"Current Input: {current_input}")
        next_input = markov_model.predict_next(current_input)
        print(f"Predicted Next Input: {next_input}")
        user_input = int(input("Enter your next input (1-6): "))
        
        if user_input not in [1, 2, 3, 4, 5, 6]:
            print("Invalid input. Please enter a number from 1 to 6.")
            continue

        user_data[-1].append(user_input)  # Update the user's history
        markov_model.train(user_data)  # Retrain the model with updated data
        current_input = user_input

        total_attempts += 1
        if user_input == next_input:
            correct_predictions += 1
            print("Match! Your input matches the prediction.")

        accuracy = correct_predictions / total_attempts
        print(f"Accuracy: {accuracy * 100:.2f}%")
