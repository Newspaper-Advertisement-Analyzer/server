import uuid


def generate_unique_id():
    return f"ad{str(uuid.uuid4())}"
