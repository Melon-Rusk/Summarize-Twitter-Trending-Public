from transformers import pipeline
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

summarizer = pipeline("summarization")

import re

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)



def abstract_summary(text,max_length=200):
    print(f"len of (text) before emoji: {len(text)}")
    text = remove_emoji(text)
    print(f"len(text): {len(text)}")
    summary = summarizer(text[:2000],max_length=max_length, min_length=5, do_sample=False)
    summary_text = summary[0]['summary_text']# type: ignore
    # print(summary_text)
    return summary_text

if __name__ == "__main__":
    text = """ xyz summarize this text"""
    abstract_summary(text,max_length=200)


