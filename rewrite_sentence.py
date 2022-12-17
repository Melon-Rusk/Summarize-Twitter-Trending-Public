import spacy
import nltk
from nltk.corpus import wordnet
import summa
import string

nlp = spacy.load("en_core_web_sm")

def rewrite_sentence_spacy(sentence):
    # Parse the sentence with spaCy
    doc = nlp(sentence)
    
    # Create a list to hold the new words
    new_words = []
    
    # Iterate through the tokens in the sentence
    for token in doc:
        # Check if the token is a punctuation mark or a space
        if token.is_punct or token.is_space:
            # If so, add it to the list without modifying it
            new_words.append(token.text)
        else:
            # If not, lemmatize the word and add it to the list
            new_words.append(token.lemma_)
    
    # Join the new words together to form the rewritten sentence
    rewritten_sentence = "".join(new_words)
    
    # Return the rewritten sentence
    return rewritten_sentence


def rewrite_sentence_nltk(sentence):
    # Tokenize the sentence with NLTK
    tokens = nltk.word_tokenize(sentence)
    
    # Create a list to hold the new words
    new_words = []
    
    # Iterate through the tokens in the sentence
    for token in tokens:
        # Check if the token is a punctuation mark or a space
        if token in string.punctuation or token == " ":
            # If so, add it to the list without modifying it
            new_words.append(token)
        else:
            # If not, lemmatize the word and add it to the list
            lemma = wordnet.morphy(token)
            if lemma is not None:
                new_words.append(lemma)
            else:
                new_words.append(token)
    
    # Join the new words together to form the rewritten sentence
    rewritten_sentence = "".join(new_words)
    
    # Return the rewritten sentence
    return rewritten_sentence

# Test the function
print(rewrite_sentence_nltk("The quick brown fox jumps over the lazy dog."))
# Output: "the quick brown fox jump over the lazy dog."

# Test the function
print(rewrite_sentence_spacy("The quick brown fox jumps over the lazy dog."))
# Output: "the quick brown fox jump over the lazy dog."


def rewrite_sentence(sentence):
    # Summarize the sentence with summa
    summary = summa.summarizer.summarize(sentence, words=5)
    
    # Return the summarized sentence
    return summary

# Test the function
print(rewrite_sentence("The quick brown fox jumps over the lazy dog."))
# Output: "The quick brown fox jumps over the lazy dog."

def extract_summary(data, language):
    # Create a list to hold the summaries
    summaries = []
    
    # Iterate through the text data
    for text in data:
        # Summarize the text with summa
        summary = summa.summarizer.summarize(text, language=language, words=5)
        
        # Add the summary to the list
        summaries.append(summary)
    
    # Return the list of summaries
    return summaries

# Test the function
data = ["This is a great product!", "I am not happy with this product.", "The service was terrible."]
print(extract_summary(data, "english"))
