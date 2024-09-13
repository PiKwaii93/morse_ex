# Dictionnaire de traduction du code Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': ' / '
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # Pour les caractères non reconnus
    return ' '.join(morse_code)

text = 'Hello EEMI'
morse_translation = text_to_morse(text)
print(morse_translation)

# Inverser le dictionnaire pour la traduction Morse -> Texte
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    text = []
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(REVERSE_MORSE_CODE_DICT.get(letter, '?') for letter in letters)
        text.append(decoded_word)
    return ' '.join(text)

morse_code = '.... . .-.. .-.. --- / . . -- ..'
text_translation = morse_to_text(morse_code)
print(text_translation)
