import pandas as pd
import numpy as np
import re 
import string 
from detoxify import Detoxify
from textblob import TextBlob
# from readability import Readability
import textstat
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification, AutoModelForCausalLM
from collections import Counter


df = pd.read_csv('train_essays_v1.csv')

df = df.iloc[:5] # drop everything excpet first 5 

print(df.head()) # print first 5 rows 

print(df.isnull().sum()) # checking for missing values - no missing values 

def clean_text(text):
    text = text.strip()
    text = re.sub('\s+', ' ', text)
    return text

# Function to extract URLs
def extract_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+') # s can occur or not ?, \s any non whitspace charachter, + means multiple
    # | or, www, \. = .
    urls = url_pattern.findall(text)
    return urls

df['text_cleaned'] = df['text'].apply(clean_text)
print(df.head())

# Extract URLs to a separate column
df['urls'] = df['text_cleaned'].apply(extract_urls)
print(df.head())

# Ensure 'text_cleaned' column does not contain lists by removing URLs from text 'sub' = replacing
df['text_cleaned'] = df['text_cleaned'].apply(lambda x: re.sub(r'https?://\S+|www\.\S+', '', x))
print(df.head())
# Print rows in 'text_cleaned' that have an instance of a list 
list_rows = df['text_cleaned'].apply(lambda x: isinstance(x, list))
print("Rows where 'text_cleaned' column contains lists:")
print(df[list_rows])

# check for toxicity - checks what percentage is the work toxic 
toxicity_scores = df['text'].apply(lambda x: Detoxify('original').predict(x))
df['toxicity'] = toxicity_scores.apply(lambda x: x['toxicity'])
print("Toxicity Scores:")
print(df[['text', 'toxicity']].head())


# textblob gives sentiment analys
# check for subjectivity s

df['subjectivity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
print("Subjectivity Scores:")
print(df[['text', 'subjectivity']].head())

# Load the formality ranker model
tokenizer = AutoTokenizer.from_pretrained("s-nlp/roberta-base-formality-ranker") # converts text into tokens, model understands
model = AutoModelForSequenceClassification.from_pretrained("s-nlp/roberta-base-formality-ranker") # load model
formality_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer)

def split_text(text, max_length=256): # alothough it says 512 wasnt working 
    tokens = tokenizer.encode(text, truncation=True) # if token longer, cut short 
    chunks = [tokens[i:i + max_length] for i in range(0, len(tokens), max_length)]
    return [tokenizer.decode(chunk) for chunk in chunks]

# Apply chunking to each row in 'text_cleaned'
df['text_chunks'] = df['text_cleaned'].apply(split_text)
print("Text Chunks:")
print(df[['text_cleaned', 'text_chunks']].head())

# Check formality using the model, handling long texts by splitting them into chunks
def get_formality(text):
    chunks = split_text(text)
    results = [formality_pipeline(chunk) for chunk in chunks]
    # Assuming we want to get the label with the highest score from the chunks
    final_label = max(results, key=lambda x: x[0]['score'])[0]['label']
    final_score = max([result[0]['score'] for result in results])
    return final_label, final_score

df['formality'] = df['text_cleaned'].apply(lambda x: get_formality(x)[0])
df['formality_score'] = df['text_cleaned'].apply(lambda x: get_formality(x)[1])

print("Formality Scores:")
print(df[['text', 'formality', 'formality_score']].head())


# N-Gram Analysis Function for redundancy 
def get_ngrams(text, n):
    words = text.split()
    ngrams = zip(*[words[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

def calculate_redundancy_score(text, n=3):
    ngrams = get_ngrams(text, n)
    ngram_counts = Counter(ngrams)
    redundant_ngrams = [ngram for ngram, count in ngram_counts.items() if count > 1]
    redundancy_score = len(redundant_ngrams) / len(ngrams) if len(ngrams) > 0 else 0
    return redundancy_score

# Calculate redundancy scores
df['redundancy_score'] = df['text'].apply(lambda x: calculate_redundancy_score(x, n=3))

# Print redundancy scores
print("Redundancy Scores:")
print(df[['text', 'redundancy_score']].head())



"""
im trying to preprocess my data 
steps i will be following
1) load data 
2) check for missing data- remove missing value rows or change with mean, median, mode depending 
3) clean data by removing extra spaces, punctuation, extra charachters, stop words 
4) remove duplicates 
5) normalization - convert to 0-1
6) standardidization to mean of 0 and 1
7) Handling outliers -> remove values above a threshold 
8) apply transformations to reduce effect of outliers 
9) Handling categorical data-> convert to numerical data - embeddings, one hot encoding 
10) feature engineering- create new features from exisiting ones 
11) dropping unneccessary features 


"""

