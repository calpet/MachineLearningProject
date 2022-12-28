def create_predictions_model(preprocessed_tokens, vectorizer, model):
    token_features = vectorizer.transform(preprocessed_tokens)

    # Make a prediction for each token
    predictions = model.predict(token_features)
    return predictions

