# Natural Language Processing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# The dataset contains two columns: "Review" (text) and "Liked" (label: 1 for positive, 0 for negative)
dataset = pd.read_csv(
    "natural-language-processing/Restaurant_Reviews.tsv", delimiter="\t", quoting=3
)

# Cleaning the texts
import re
import nltk

# Downloading the stopwords (commonly used words like "the", "is", etc.)
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import (
    PorterStemmer,
)  # For stemming (reducing words to their root form)

corpus = []  # A list to store cleaned reviews
for i in range(0, 1000):
    # Removing special characters and numbers, keeping only letters
    review = re.sub("[^a-zA-Z]", " ", dataset["Review"][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    # Removing stopwords and applying stemming to each word
    review = [
        ps.stem(word) for word in review if not word in set(stopwords.words("english"))
    ]
    review = " ".join(review)
    corpus.append(review)


############# Creating the Bag of Words model #############
from sklearn.feature_extraction.text import CountVectorizer

# This converts the cleaned text into a sparse matrix of token countss
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)

# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)

# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")


# [[True Negative (TN), False Positive (FP)],
#  [False Negative (FN), True Positive (TP)]]

# [[55 42]
#  [12 91]]

# 55: Negative reviews (0) correctly predicted (True Negatives).
# 42: Negative reviews (0) incorrectly predicted as positive (False Positives).
# 12: Positive reviews (1) incorrectly predicted as negative (False Negatives).
# 91: Positive reviews (1) correctly predicted (True Positives).


############# SVM model #############s
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

classifier_svm = SVC(kernel="linear", random_state=0)
classifier_svm.fit(X_train, y_train)

y_pred_svm = classifier_svm.predict(X_test)

cm_svm = confusion_matrix(y_test, y_pred_svm)
print(cm_svm)

TP = cm_svm[1, 1]
TN = cm_svm[0, 0]
FP = cm_svm[0, 1]
FN = cm_svm[1, 0]

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
