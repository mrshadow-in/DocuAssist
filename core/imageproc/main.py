import os
import json
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import sys

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Define file paths and configurations
input_dir = 'temp.txt'  # Update with actual path to temp.txt
# output_dir = 'medgpt/media/{username}/output.txt'  # Update with actual path to output.txt
output_dir = 'output.txt'  # Update with actual path to output.txt
intents_file = 'intents.json'  # Path to intents JSON file

# Load intents from JSON
with open(intents_file, 'r') as file:
    intents = json.load(file)


# Function to extract medical data from converted text
def extract_medical_data(text):
    try:
        # Implement your logic here for extracting medical data
        # This may involve using regular expressions, NLP, or specific keywords

        # For demonstration, we'll tokenize the text into sentences and extract keywords
        sentences = sent_tokenize(text)
        medical_data = []

        for sentence in sentences:
            tokens = word_tokenize(sentence)
            tokens = [word.lower() for word in tokens if
                      word.isalnum() and word.lower() not in stopwords.words('english')]

            for intent in intents['intents']:
                for pattern in intent['patterns']:
                    if any(keyword in tokens for keyword in pattern.split()):
                        medical_data.append(intent['tag'])

        return medical_data
    except Exception as e:
        raise Exception(f"Error during data extraction: {str(e)}")


# Main function to process the converted text
def process_converted_text(username):
    try:
        # Read the converted text from temp.txt
        with open(input_dir.format(username=username), 'r') as input_file:
            converted_text = input_file.read()

        medical_data = extract_medical_data(converted_text)

        # Save the medical data to the output file
        with open(output_dir.format(username=username), 'w') as output_file:
            output_file.write('\n'.join(medical_data))

        return f"Medical data extracted and saved to {output_dir.format(username=username)} ({len(medical_data)} tags)"
    except Exception as e:
        raise Exception(f"Error during processing: {str(e)}")


# Example usage
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <username>")
        sys.exit(1)

    username = sys.argv[1]

    try:
        result = process_converted_text(username)
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")
