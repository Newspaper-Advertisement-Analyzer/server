import ahocorasick
import pickle

# Generator function to read cities from the file one by one


def cities_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Initialize Aho-Corasick automaton and save it if not already saved


def initialize_automaton(filename, save_filename):
    if not hasattr(initialize_automaton, 'cities'):
        try:
            with open(save_filename, 'rb') as f:
                automaton = pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError):
            automaton = ahocorasick.Automaton()
            for city in cities_generator(filename):
                automaton.add_word(city, city)
            automaton.make_automaton()
            with open(save_filename, 'wb') as f:
                pickle.dump(automaton, f)
        initialize_automaton.automaton = automaton
    return initialize_automaton.automaton


def extract_locations(given_text):
    # Given text
    # given_text = "This is a text containing some city names like Ampara, Kalmunai, etc., Colombo, Galle,  Ambagasdowa"

    # Get the automaton (initialize if not already initialized)
    # ===========================change the name later
    automaton = initialize_automaton('cities.txt', 'cities.pkl')

    # Find matching cities using the Aho-Corasick automaton
    matching_cities = set()

    for _, city in automaton.iter(given_text):
        matching_cities.add(city)

    # print(matching_cities)

    if len(matching_cities) == 0:
        return ["No locations found"]

    return list(matching_cities)


# print(extract_locations(
#     "This is a text containing some city names like Ampara, Kalmunai, etc., Colombo, Galle,  Ambagasdowa Welimada"))
