import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)
    return text.lower()

def calculate_similarity(resume_text, jd_text):
    texts = [resume_text, jd_text]
    
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts)
    
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)
