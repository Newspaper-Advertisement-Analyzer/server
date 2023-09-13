# def identify_catogory(text):

#     candidate_labels = ["land", "house", "vehicle", "rent", "wedding"]
#     text = text.lower()

#     for label in candidate_labels:
#         if label in text:
#             return label

#     return "Unclassified"
def identify_catogory(advertisement_text):
    category = "Couldn't found a category"  # Default category

    # Check for common keywords to categorize the advertisement
    keywords_to_category = {
        "Land Sales": ["land for sale", "landsales", "land plot", "property for sale", "land for", "land"],
        "House Sales": ["house", "apartment"],
        "Marriage Proposals": ["marriage proposal", "bride", "groom", "marriage partner", "matrimonial"],
        "vehicle_for_sale": ["vehicle for sale", "car for sale", "auto for sale", "motorcycle for sale", "toyota"]
    }

    lowercased_text = advertisement_text.lower()
    for cat, keywords in keywords_to_category.items():
        if any(keyword in lowercased_text for keyword in keywords):
            category = cat
            break

    return category


