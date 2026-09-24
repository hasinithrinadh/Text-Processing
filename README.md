 Text-Processing
* NLP Text Preprocessing using NLTK

A beginner-friendly Natural Language Processing (NLP) text preprocessing project that cleans and prepares customer review data for further analysis or machine learning tasks.

This project uses Python, Pandas, Regular Expressions, and NLTK to preprocess text reviews through multiple steps including:

Text cleaning
Lowercase conversion
URL removal
Number removal
Punctuation removal
Tokenization
Stopword removal
Lemmatization

The processed dataset is finally saved as a new CSV file for further NLP tasks.

* Project Overview

Raw text data usually contains unnecessary elements such as:

URLs
Numbers
Punctuation
Extra spaces
Common words
Different forms of the same word

These elements can make text analysis more difficult.

This project takes a dataset containing customer reviews and performs a series of preprocessing steps to convert raw text into cleaner and more meaningful data.

Example

Original Review:

"I really LOVE this product! Visit http://example.com for more details. It has 100% quality."

After preprocessing:

"really love product visit details quality"

The words are then tokenized, stopwords are removed, and the remaining words are lemmatized.

* Objectives
Understand the basics of Natural Language Processing
Learn how to clean raw text data
Perform tokenization using NLTK
Remove unnecessary stopwords
Apply lemmatization
Work with a CSV dataset using Pandas
Prepare text data for future NLP and machine learning applications
* Technologies Used
Technology	Purpose
Python	Programming language
Pandas	Dataset handling and processing
Regular Expressions (re)	Text cleaning
NLTK	Natural Language Processing
word_tokenize	Tokenization
stopwords	Stopword removal
WordNetLemmatizer	Lemmatization
CSV	Dataset and output format
* Project Structure
text
NLP-Text-Preprocessing/
│
├── dataset/
│   └── reviews.csv
│
├── output/
│   └── clean_reviews.csv
│
├── preprocess.py
├── requirements.txt
└── README.md
File Description
File / Folder	Description
dataset/reviews.csv	Original review dataset
output/clean_reviews.csv	Processed dataset
preprocess.py	Main preprocessing program
requirements.txt	Required Python libraries
README.md	Project documentation
* NLP Preprocessing Pipeline

The project follows this pipeline:

Raw Reviews
     ↓
Convert to Lowercase
     ↓
Remove URLs
     ↓
Remove Numbers
     ↓
Remove Punctuation
     ↓
Remove Extra Spaces
     ↓
Tokenization
     ↓
Stopword Removal
     ↓
Lemmatization
     ↓
Clean Processed Dataset
* Step-by-Step Explanation
1. Import Required Libraries

The project starts by importing the required Python libraries:

python
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

Libraries Used

Pandas — Used for reading, modifying, and saving the CSV dataset.
re — Used for regular-expression-based text cleaning.
NLTK — Used for different Natural Language Processing operations.
2. Download NLTK Resources

The required NLTK resources are downloaded:

python
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

These resources are required for:

Tokenization
Stopword removal
Lemmatization

These downloads are generally needed when setting up the environment for the first time.

3. Load Stopwords

English stopwords are loaded using:

python
stop_words = set(stopwords.words('english'))

Stopwords are common words that may not provide much useful information for some NLP tasks.

Examples include: the, is, a, an, and, of, to, in

4. Initialize the Lemmatizer

The project creates a WordNet lemmatizer:

python
lemmatizer = WordNetLemmatizer()

It is later used to convert words into their base or dictionary form.

For example: cars → car

* Dataset

The project reads the dataset from:

python
data = pd.read_csv("dataset/reviews.csv")

The dataset is expected to contain a column named Review.

The program then removes unnecessary spaces from column names:

python
data.columns = data.columns.str.strip()

This helps avoid problems caused by accidental spaces in column names.

* Text Cleaning

The main cleaning function is:

python
def preprocess(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

The function performs several preprocessing operations.

1. Convert to Lowercase
python
text = text.lower()

Example: "THIS PRODUCT IS AMAZING" becomes "this product is amazing"

This ensures that uppercase and lowercase versions of the same word are treated consistently.

2. Remove URLs
python
text = re.sub(r"http\S+", "", text)

This removes URLs from the review.

Example: "Visit https://example.com today" becomes approximately "Visit  today"

3. Remove Numbers
python
text = re.sub(r"\d+", "", text)

Numbers are removed from the text.

Example: "This product costs 500 rupees" becomes "This product costs  rupees"

4. Remove Punctuation
python
text = re.sub(r"[^\w\s]", "", text)

This removes punctuation marks.

Example: "Excellent product!" becomes "Excellent product"

5. Remove Extra Spaces
python
text = re.sub(r"\s+", " ", text).strip()

This removes unnecessary spaces from the text.

* Creating the Clean Text Column

The cleaning function is applied to every review:

python
data["clean_text"] = data["Review"].apply(preprocess)

A new column called clean_text is created.

The dataset now contains both the original review and its cleaned version.

* Tokenization

The project performs tokenization using:

python
data["tokens"] = data["clean_text"].apply(word_tokenize)

What is Tokenization?

Tokenization is the process of breaking text into smaller units called tokens.

Example: "I love this product" becomes ["I", "love", "this", "product"]

These tokens can then be processed individually.

* Stopword Removal

The project removes stopwords using:

python
def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

The function is applied to the tokenized text:

python
data["tokens_no_stopwords"] = data["tokens"].apply(remove_stopwords)

Example

Before: ["this", "is", "a", "good", "product"]

After: ["good", "product"]

Common words such as this, is, and a are removed.

* Lemmatization

The project uses:

python
lemmatizer = WordNetLemmatizer()

The lemmatization function is:

python
def lemmatize(tokens):
    return [lemmatizer.lemmatize(word) for word in tokens]

It is applied using:

python
data["lemmatized_tokens"] = data["tokens_no_stopwords"].apply(lemmatize)

What is Lemmatization?

Lemmatization converts words into their base or dictionary form.

Example: cars → car

This can help reduce different forms of words into a common representation.

* Dataset Transformation

The project gradually adds new columns to the dataset.

The processing flow can be represented as:

Review
  ↓
clean_text
  ↓
tokens
  ↓
tokens_no_stopwords
  ↓
lemmatized_tokens

For example:

Stage	Example
Original Review	I really LOVE this product!
Clean Text	i really love this product
Tokens	["i", "really", "love", "this", "product"]
Without Stopwords	["really", "love", "product"]
Lemmatized Tokens	["really", "love", "product"]
* Save Processed Dataset

After preprocessing, the final dataset is saved using:

python
data.to_csv("output/clean_reviews.csv", index=False)

The processed file is stored at output/clean_reviews.csv.

The program also displays:

Preprocessing completed successfully.
File saved as output/clean_reviews.csv
* Output

The final CSV file contains the original and processed information.

Example structure columns:

Review
clean_text
tokens
tokens_no_stopwords
lemmatized_tokens

This processed dataset can be used as input for future NLP tasks.

* How to Run
1. Clone the Repository
bash
git clone https://github.com/your-username/nlp-text-preprocessing.git
2. Navigate to the Project
bash
cd nlp-text-preprocessing
3. Install Dependencies
bash
pip install pandas nltk

Or:

bash
pip install -r requirements.txt
4. Add the Dataset

Place your CSV file inside dataset/reviews.csv.

Make sure the dataset contains a column named Review.

5. Run the Program
bash
python preprocess.py

After successful execution, the processed dataset will be created at output/clean_reviews.csv.

* Requirements

The requirements.txt file can contain:

pandas
nltk
* Features
Reads reviews from a CSV file
Cleans raw text
Converts text to lowercase
Removes URLs
Removes numbers
Removes punctuation
Tokenizes text
Removes stopwords
Performs lemmatization
Saves the processed dataset
Displays intermediate preprocessing results
* Applications

Text preprocessing is an important first step in many NLP applications, including:

Sentiment Analysis
Spam Detection
Chatbots
Text Classification
Text Search
Customer Review Analysis
Machine Learning for NLP
Document Classification
* Limitations

The current preprocessing pipeline has some limitations:

Numbers are completely removed even when they may contain useful information.
URLs are removed rather than analyzed.
Punctuation is removed, which can sometimes affect meaning.
Stopword removal may remove words that are useful in certain contexts.
The lemmatizer is used without specifying the part of speech, so some words may not be reduced to the most accurate base form.
The preprocessing is designed for English text.

Therefore, preprocessing techniques should be selected based on the specific NLP task and dataset.

* Future Improvements

The project can be extended by adding:

Sentiment analysis after preprocessing
Machine learning classification
Word frequency analysis
Word cloud visualization
Stemming comparison
POS tagging
Named Entity Recognition
Dataset statistics
Multilingual preprocessing
Comparison of different preprocessing techniques
* Concepts Learned

Through this project, I learned:

Natural Language Processing
Text preprocessing
Regular expressions
Data manipulation using Pandas
Tokenization
Stopword removal
Lemmatization
CSV dataset handling
Preparing text data for machine learning
* Learning Outcome

This project demonstrates how raw textual data can be transformed into a cleaner and more structured form using NLP preprocessing techniques.

The processed data can serve as a foundation for advanced NLP applications such as sentiment analysis, spam detection, text classification, and machine learning models.

* Author

D. Hasini

B.Sc. Computer Science with AI

* Conclusion

The NLP Text Preprocessing using NLTK project demonstrates the fundamental steps involved in preparing textual data for Natural Language Processing.

Starting with raw customer reviews, the project performs text cleaning, tokenization, stopword removal, and lemmatization, and then saves the processed data into a new CSV file.

This project provides a strong foundation for understanding how raw text is prepared before applying NLP algorithms, machine learning models, or AI-based text analysis.
