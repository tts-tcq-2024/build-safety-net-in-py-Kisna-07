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

def encode_character(char, mapping, previous_code):
    code = get_soundex_code(char, mapping)
    return code if code != previous_code else ''

def generate_soundex(name):
    if not name:
        return ""

    cleaned_name = clean_name(name)
    if not cleaned_name:
        return ""

    mapping = get_char_code_mapping()
    soundex = cleaned_name[0].upper()
    previous_code = get_soundex_code(soundex, mapping)

    for char in cleaned_name[1:]:
        code = encode_character(char, mapping, previous_code)
        if code:
            soundex += code
            previous_code = code
        if len(soundex) == 4:
            break

    return soundex.ljust(4, '0')
