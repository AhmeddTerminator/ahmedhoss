# filepath: /lorem-encryptor-gui/lorem-encryptor-gui/src/Encrypt.py
# Dictionary mapping letters A-Z to Lorem Ipsum-style words
lorem_cipher = {
    'A': 'Lorem', 'B': 'Ipsum', 'C': 'Dolor', 'D': 'Sit', 'E': 'Amet',
    'F': 'Consectetur', 'G': 'Adipiscing', 'H': 'Elit', 'I': 'Sed', 'J': 'Do',
    'K': 'Eiusmod', 'L': 'Tempor', 'M': 'Incididunt', 'N': 'Ut', 'O': 'Labore',
    'P': 'Et', 'Q': 'Dolore', 'R': 'Magna', 'S': 'Aliqua', 'T': 'Enim',
    'U': 'Ad', 'V': 'Minim', 'W': 'Veniam', 'X': 'Quis', 'Y': 'Nostrud', 'Z': 'Exercitation'
}

def encrypt_message(message):
    """
    Encrypts a message by replacing each letter A-Z with a corresponding Lorem Ipsum-style word.
    Non-alphabetic characters are preserved as is.
    
    Args:
        message (str): The message to encrypt.
        
    Returns:
        str: The encrypted message.
    """
    words = message.split()
    encrypted_words = []
    for word in words:
        encrypted_letters = []
        for char in word:
            if char.isalpha():
                enc = lorem_cipher[char.upper()].capitalize()
                encrypted_letters.append(enc)
            else:
                encrypted_letters.append(char)
        encrypted_words.append(' '.join(encrypted_letters))
    return '   '.join(encrypted_words)  # Triple space between words