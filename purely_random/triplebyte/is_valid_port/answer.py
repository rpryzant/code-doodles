import re

"""
This is the file with your answer, do not rename or move it.
Write your code in it, and save it before submitting your answer.
"""

def is_valid_ip(parts):
    """
    Determines if the given list is a valid ip address

    Args:
       parts: [int]

    Returns:
       whether each part is a valid ip segment
    """
    return all(map(lambda x: 0 <= x and x <= 255, parts))


def is_valid_port(x):
    """
    Determines if x is in the range [1, 65535]

    Args:
        x: int

    Returns:
        1 <= x <= 65535
    """
    return 1 <= x <= 65535


def is_valid_socket(socket_address):
    """Determine if the provided string is a valid socket address.
    This function declaration must be kept unmodified.

    Args:
        socket_address: A string with a socket address, eg, 
            '127.12.23.43:5000', to be checked for validity.
    Returns:
        A boolean indicating whether the provided string is a valid 
        socket address.
    """
    if socket_address is None or type("") != type(socket_address):
        return False

    parts = re.split('\.|\:', socket_address)
    if len(parts) != 5 or any(map(lambda x: not x.isdigit(), parts)):
        return False

    return is_valid_ip([int(x) for x in parts[:-1]]) and is_valid_port(int(parts[-1]))


# This tests your code with the examples given in the question, 
# and is provided only for your convenience.
if __name__ == '__main__':
    for socket_address in ["127.12.23.43:5000",
                   "127.A:-12"]:
        print is_valid_socket(socket_address)


