from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from src.utils.token_handler import preprocess

def train_model(model: LogisticRegression, dataset, labels):
    # Preprocess the texts in the dataset
    preprocessed_texts = [preprocess(text) for text in dataset]

    # Convert the text data to numerical features using TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(preprocessed_texts)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

    # Train a logistic regression model on the training set
    model.fit(X_train, y_train)

    # Evaluate the model's performance on the testing set
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.2f}")
    return model, vectorizer
