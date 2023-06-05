import os
from datetime import date

# Specify the folder path
folder_path = "DIRECTORY PATH HERE"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Today's sentiment score
today = date.today().strftime("%b %d, %Y")
today_sentiment_scores = []

# Overall sentiment score
sentiment_scores = []

# Initialize headline counts
today_headline_count = 0
overall_headline_count = 0

# Store the results for sorting
results = []

# Iterate over each file in the folder
for file_name in files:
    file_path = os.path.join(folder_path, file_name)

    # Read the headlines file
    with open(file_path, "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if lines[i].startswith("Headline:"):
            overall_headline_count += 1
            sentiment_score_line = lines[i + 3]
            if sentiment_score_line.strip():
                sentiment_score = float(sentiment_score_line.split(": ")[-1].strip())
                sentiment_scores.append(sentiment_score)

            event_time_line = lines[i + 2]
            event_time = event_time_line.split(": ")[-1].strip()
            if event_time.startswith(today):
                today_headline_count += 1
                today_sentiment_scores.append(sentiment_score)

    if today_sentiment_scores:
        today_cumulative_score = sum(today_sentiment_scores)
        today_average_score = today_cumulative_score / len(today_sentiment_scores)

        # Assign sentiment label based on average score
        if today_average_score > 0.2:
            sentiment_label = "Positive"
        elif today_average_score < -0.2:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        # Add the results to the list for sorting
        results.append((file_name, today_headline_count, today_average_score, sentiment_label))

    today_sentiment_scores.clear()
    today_headline_count = 0

if overall_headline_count > 0:
    cumulative_score = sum(sentiment_scores)
    average_score = cumulative_score / overall_headline_count

    # Assign sentiment label based on average score
    if average_score > 0.2:
        sentiment_label = "Positive"
    elif average_score < -0.2:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    # Add the overall results to the list for sorting
    results.append(("Overall", overall_headline_count, average_score, sentiment_label))

# Sort the results from highest to lowest based on average sentiment score
sorted_results = sorted(results, key=lambda x: x[2], reverse=True)

# Print the sorted results
for result in sorted_results:
    print("---------------------------------------------")
    print("----- Today's Sentiment Analysis Results -----")
    print("File: ", result[0])
    print("Headlines Processed: ", result[1])
    print("Average Sentiment Score: ", result[2])
    print("Sentiment Label: ", result[3])
    print("---------------------------------------------")
