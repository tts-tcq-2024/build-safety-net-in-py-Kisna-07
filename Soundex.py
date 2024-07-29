def get_char_code_mapping():
    return {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }

def get_soundex_code(c, mapping):
    return mapping.get(c.upper(), '0')

def clean_name(name):
    return ''.join(filter(str.isalpha, name))

def initialize_soundex(name, mapping):
    initial = name[0].upper()
    initial_code = get_soundex_code(initial, mapping)
    return initial, initial_code

def process_characters(name, initial_code, mapping):
    soundex = name[0].upper()
    prev_code = initial_code
    length = 1

    for char in name[1:]:
        code = get_soundex_code(char, mapping)
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
            length += 1
        if length == 4:
            break

    return soundex

def generate_soundex(name):
    if not name:
        return ""

    cleaned_name = clean_name(name)
    if not cleaned_name:
        return ""

    mapping = get_char_code_mapping()
    initial, initial_code = initialize_soundex(cleaned_name, mapping)
    soundex = process_characters(cleaned_name, initial_code, mapping)
    
    return soundex.ljust(4, '0')
