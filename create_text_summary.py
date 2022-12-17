import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import pandas as pd
def summarize_text(text,n=20):
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    formatted_text = re.sub('[^a-zA-Z]', ' ', text )
    formatted_text = re.sub(r'\s+', ' ', formatted_text)
    sentence_list = nltk.sent_tokenize(text)

    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    try:
        maximum_frequncy = max(word_frequencies.values())
    except Exception as e:
        print(e)
        maximum_frequncy = 1
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    summary = ''
    if len(sentence_scores)>0:
        sentence_scores_df = pd.DataFrame.from_dict(sentence_scores,orient='index').reset_index().sort_values(by=0,ascending=False).head(n+5).tail(n) # type: ignore        
        summary_sentences = sentence_scores_df['index']
        summary = ' '.join(summary_sentences)

    summary = re.sub(r'http\S+', '', summary)
    # summary = summary
    # summary 
    return summary

if __name__ == "__main__":
    summary = summarize_text('article_text')

# print(summary)