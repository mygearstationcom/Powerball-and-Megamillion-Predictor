import pandas as pd
import numpy as np

def load_data(file_path):
    """Load data from CSV file and separate white balls from Powerball."""
    data = pd.read_csv(file_path, header=None)
    # Columns 0-4 are white balls (5 total)
    white_balls_data = data.iloc[:, 0:5]
    # Column 5 is the Powerball (1 total)
    powerball_data = data.iloc[:, 5]
    return white_balls_data, powerball_data

def create_transition_matrix(data):
    """Create transition matrix based on frequency for white balls (1-69)."""
    # Max number is 69. We use indices 1-69 in a 70x70 matrix.
    num_states = 70  # Reverted range
    transition_matrix = np.zeros((num_states, num_states))
    
    for index, row in data.iterrows():
        prev_num = None
        for num in row:
            # Ensure number is a valid integer between 1 and 69
            try:
                num = int(num)
                if not (1 <= num <= 69): # Reverted range
                    continue
            except ValueError:
                continue
            
            if prev_num is not None:
                transition_matrix[prev_num][num] += 1
            prev_num = num
    
    # Normalize transition matrix
    row_sums = transition_matrix.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1 
    transition_matrix /= row_sums

    return transition_matrix

def predict_white_balls_freq(transition_matrix, num_sets=1, num_numbers=5):
    """Predict next group of white ball numbers based on frequency (1-69)"""
    predicted_numbers = []
    max_white_ball = 69 # Reverted range
    
    for _ in range(num_sets):
        # Initial state should be a valid white ball number (1-69)
        current_state = np.random.randint(1, max_white_ball + 1) 
        numbers = [current_state]
        
        for _ in range(num_numbers - 1):
            choices = np.arange(1, max_white_ball + 1) 
            probabilities = transition_matrix[current_state][1:max_white_ball + 1] 
            
            if probabilities.sum() == 0:
                 next_state = np.random.choice(choices)
            else:
                probabilities /= probabilities.sum()
                next_state = np.random.choice(choices, p=probabilities)

            numbers.append(next_state)
            current_state = next_state
        
        predicted_numbers.append(numbers)
    
    return predicted_numbers

def predict_white_balls_unused(data, num_sets=1, num_numbers=5):
    """Predict next group of white ball numbers based on unused numbers (1-69)"""
    max_white_ball = 69 # Reverted range
    
    # Ensure data only contains valid integers for the white ball range
    used_numbers = set(data.values.flatten().astype(int))
    valid_used_numbers = {num for num in used_numbers if 1 <= num <= max_white_ball}
    
    all_possible_numbers = set(range(1, max_white_ball + 1))
    unused_numbers = all_possible_numbers - valid_used_numbers 
    
    selection_pool = list(unused_numbers)
    replace_mode = False

    if not selection_pool:
        print("Note: All white ball numbers 1-69 have been used. Choosing from the full range.")
        selection_pool = list(all_possible_numbers)
        replace_mode = True 
    elif len(selection_pool) < num_numbers:
        print(f"Warning: Not enough unused white balls ({len(selection_pool)}) to pick {num_numbers} unique numbers without replacement. Choosing with replacement.")
        replace_mode = True
            
    predicted_numbers = []
    for _ in range(num_sets):
        numbers = np.random.choice(selection_pool, num_numbers, replace=replace_mode)
        predicted_numbers.append(list(numbers))
    
    return predicted_numbers

# --- Function for Powerball ---

def predict_powerball(data, num_sets=1):
    """Predict the Powerball (1-26)."""
    # Max number is 26
    max_powerball = 26 # Reverted range
    predicted_pbs = []

    for _ in range(num_sets):
        # Simply pick a random integer between 1 and 26 inclusive
        pb_number = np.random.randint(1, max_powerball + 1)
        predicted_pbs.append(pb_number)
        
    return predicted_pbs
# ---- How to update the powerball.csv ----
# Go to https://catalog.data.gov/dataset/  
# Search on megamillions then select the Title: Lottery Powerball Winning Numbers: Beginning *****
# Download the file  into your subdirectory and rename as powerball.csv

def main():
    file_path = "powerball.csv" # Reverted file name
    # Load separate dataframes for white balls and powerballs
    white_balls_data, powerball_data = load_data(file_path)

    # --- Frequency Method ---
    transition_matrix = create_transition_matrix(white_balls_data)
    predicted_freq_white_balls = predict_white_balls_freq(transition_matrix, num_sets=1)
    predicted_freq_pb = predict_powerball(powerball_data, num_sets=1)

    print("Predicted numbers based on frequency (PowerBall):")
    # Format the output nicely, sorting white balls
    for i in range(len(predicted_freq_white_balls)):
        white_balls = sorted(predicted_freq_white_balls[i]) # Sort output
        pb = predicted_freq_pb[i]
        print(f"{white_balls}, PowerBall = {pb}")
    
    # --- Unused Method ---
    predicted_unused_white_balls = predict_white_balls_unused(white_balls_data, num_sets=1)
    predicted_unused_pb = predict_powerball(powerball_data, num_sets=1)

    print("\nPredicted numbers based on unused numbers (PowerBall):")
    # Format the output nicely, sorting white balls
    for i in range(len(predicted_unused_white_balls)):
        white_balls = sorted(predicted_unused_white_balls[i]) # Sort output
        pb = predicted_unused_pb[i]
        print(f"{white_balls}, PowerBall = {pb}")


if __name__ == "__main__":
    main()
