def censor(tokens, predictions):
    # Create a list of censored tokens
    censored_tokens = [tokens[i] if predictions[i] == 1 else "*" * len(tokens[i]) for i in range(len(tokens))]
    return " ".join(censored_tokens)