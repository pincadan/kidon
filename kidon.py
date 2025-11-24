import itertools
import string

def brute_force_attack(target_string):
    characters = string.ascii_letters + string.digits
    length = len(target_string)

    for attempt_length in range(1, length + 1):
        for attempt in itertools.product(characters, repeat=attempt_length):
            attempt_string = ''.join(attempt)
            if attempt_string == target_string:
                return attempt_string

    return None

target_string = input("Enter the target string: ")
result = brute_force_attack(target_string)

if result is not None:
    print(f"The target string '{target_string}' was found after {len(result)} attempts.")
else:
    print(f"The target string '{target_string}' was not found.")