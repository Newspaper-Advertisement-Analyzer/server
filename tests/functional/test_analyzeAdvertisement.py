from NLP.detailextract import analyze_advertisement
from NLP.detailextract import analyze_advertisement_img


def test_analyze_advertisement():
    # Replace this with an actual URL
    advertisement_URL = "https://www.hitad.lk/en/ad/1779332-Kalubowila-House-for-Sale?type=houses"
    location, category, contact_info, prices = analyze_advertisement(
        advertisement_URL)

    assert location == ['No locations found']
    assert category == "House Sales"
    assert contact_info == {'phone_numbers': [
        '0766982149'], 'email_addresses': []}
    assert prices == ('LKR', 77000000.0)

    # Add more assertions based on the expected behavior of the 'analyze_advertisement' function
