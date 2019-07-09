list_response_1 = ["hello", "hi", "car"]


def is_valid_input(text, list_response):
    if text in list_response:
        return True
    else:
        return False

is_valid_input(input("type in either hello, hi, or car"), list_response_1)
