import uuid


def generate_unique_id(starting_number):
    # Generate a UUID and remove hyphens
    unique_id = str(uuid.uuid4()).replace('-', '')
    return ("ad"+str(starting_number)+unique_id[:5])
