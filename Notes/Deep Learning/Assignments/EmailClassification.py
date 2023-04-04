import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
df = pd.read_csv('spam.csv')

def text_preprocess(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    return " ".join(text)
for i in range(len(df)):
    df.iloc[i][1] = text_preprocess(df.iloc[i][1])

vectorizer = TfidfVectorizer()
message_mat = vectorizer.fit_transform(df['Message'])

message_train, message_test, spam_nospam_train, spam_nospam_test = train_test_split(message_mat, df['Category'], test_size=0.3)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

Spam_model = LogisticRegression(solver='liblinear', penalty='l1')
Spam_model.fit(message_train, spam_nospam_train)
pred = Spam_model.predict(message_test)
print(f"Accuracy: {accuracy_score(spam_nospam_test,pred)}")
