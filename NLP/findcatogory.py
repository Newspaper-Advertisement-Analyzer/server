def identify_catogory(text):

    candidate_labels = ["land", "house", "vehicle", "rent", "wedding"]
    text = text.lower()

    for label in candidate_labels:
        if label in text:
            return label

    return "Unclassified"
