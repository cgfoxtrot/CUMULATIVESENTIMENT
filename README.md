# CUMULATIVESENTIMENT

# Headline Sentiment Analysis

The Headline Sentiment Analysis script is a Python program that performs sentiment analysis on headlines stored in text files using machine learning. It calculates the average sentiment score for today's headlines and the overall average sentiment score for all headlines.

## How it Works

1. Specify the folder path where the text files containing the headlines are located by assigning the `folder_path` variable.

2. The script retrieves a list of all files in the specified folder using the `os.listdir()` function.

3. It reads each file and extracts the sentiment scores and event times associated with the headlines.

4. For today's headlines, it calculates the average sentiment score, assigns a sentiment label, and adds the results to a list.

5. After processing all the files, it calculates the overall average sentiment score and sentiment label for all headlines.

6. The script sorts the results based on the average sentiment score in descending order.

7. Finally, it displays the sorted results, including the file name, number of processed headlines, average sentiment score, and sentiment label.

## Usage

1. Ensure that Python is installed on your system.

2. Clone the repository or download the script file.

3. Open the script file in a text editor.

4. Replace the `"DIRECTORY PATH HERE"` in the `folder_path` variable with the actual path to the folder containing the text files.

5. Save the changes to the script file.

6. Open a terminal or command prompt and navigate to the directory where the script is located.

7. Run the script using the following command:

   ```shell
   python cumulativesentiment.py

8. The script will process the headlines and display the sentiment analysis results.
Note


This script assumes that the headlines in the text files follow a specific format, with each headline line starting with "Headline:" and containing sentiment scores and event times in subsequent lines. Make sure the text files conform to this format for accurate analysis.
Please note that this script only performs sentiment analysis based on the provided data and does not guarantee the accuracy or representativeness of the sentiment analysis results.
