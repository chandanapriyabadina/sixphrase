# Accept input from the user
input_scores = input("Enter the scores: ")

# Split the input string into a list of scores
scores_list = input_scores.split()

# Convert scores from string to integer
scores_list = list(map(int, scores_list))

# Remove duplicates and sort the list
unique_scores = sorted(set(scores_list), reverse=True)

# Check if there is a runner-up score
if len(unique_scores) > 1:
    runner_up_score = unique_scores[1]
    print("Runner-up score:", runner_up_score)
else:
    print("No runner-up score available.")
