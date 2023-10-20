import random
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Initialize the DataFrame with some initial data
data = pd.DataFrame({'user_input': [1, 2, 3, 4, 5, 6], 'predicted_next_input': [2, 3, 4, 5, 6, 1]})

# Define a function to train and update the model
def train_model(data):
    # Split the data into features (user_input) and labels (predicted_next_input)
    X = data['user_input'].values.reshape(-1, 1)
    y = data['predicted_next_input'].values

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a Random Forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Use KFold cross-validation to calculate the accuracy of the model
    kf = KFold(n_splits=3, shuffle=True, random_state=42)
    accuracy = cross_val_score(clf, X_train, y_train, cv=kf).mean()
    print(f"Model Accuracy (Cross-Validation): {accuracy}")

    return clf

# Train the initial model
model = train_model(data)

# Function to generate a random number for the computer's guess
def generate_random_number():
    return random.randint(1, 6)

def main():
    user_score = 0
    computer_score = 0
    user_turn = True

    while True:
        print("Hand Cricket")
        print(f"Score: {user_score} (User) - {computer_score} (Computer)")

        if user_turn:
            while True:
                try:
                    user_guess_str = input("Enter your guess (1-6): ")
                    user_guess = int(user_guess_str)
                    if 1 <= user_guess <= 6:
                        break
                    else:
                        print("Please enter a number between 1 and 6.")
                except ValueError:
                    print("Please enter a valid number.")

            # Predict the computer's guess based on the user's input
            computer_guess = model.predict([[user_guess]])[0]

            print(f"Computer's guess: {computer_guess}")

            if user_guess == computer_guess:
                print("You lost your turn! Computer's turn now.")
                user_turn = False
            else:
                user_score += user_guess
        else:
            # Generate a random guess for the computer
            computer_guess = generate_random_number()

            print(f"Computer's guess: {computer_guess}")

            while True:
                try:
                    user_guess_str = input("Enter your guess (1-6): ")
                    user_guess = int(user_guess_str)
                    if 1 <= user_guess <= 6:
                        break
                    else:
                        print("Please enter a number between 1 and 6.")
                except ValueError:
                    print("Please enter a valid number.")

            print(f"User's guess: {user_guess}")

            computer_score += computer_guess

            if computer_score >= user_score:
                print("Computer won! Your turn now.")
                user_turn = True
                user_score = 0
                computer_score = 0

            # Add the user input and predicted next input to the DataFrame
            new_data = pd.DataFrame({'user_input': [user_guess], 'predicted_next_input': [computer_guess]})
            data = pd.concat([data, new_data], ignore_index=True)

if __name__ == "__main__":
    main()
