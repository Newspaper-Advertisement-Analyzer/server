import pickle


def cities_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def initialize_automaton(filename):
    if not hasattr(initialize_automaton, 'cities'):
        try:
            with open(filename, 'rb') as f:
                automaton = pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError):
            raise Exception("Automaton file not found or invalid.")
        initialize_automaton.cities = automaton
    return initialize_automaton.cities


def extract_locations(given_text):

    automaton = initialize_automaton('cities.pkl')

    matching_cities = set()

    for _, city in automaton.iter(given_text):
        matching_cities.add(city)

    if len(matching_cities) == 0:
        return ["No locations found"]

    return list(matching_cities)





