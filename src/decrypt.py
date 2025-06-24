import string

lorem_cipher_reversed = {
    'lorem': 'A', 'ipsum': 'B', 'dolor': 'C', 'sit': 'D', 'amet': 'E',
    'consectetur': 'F', 'adipiscing': 'G', 'elit': 'H', 'sed': 'I', 'do': 'J',
    'eiusmod': 'K', 'tempor': 'L', 'incididunt': 'M', 'ut': 'N', 'labore': 'O',
    'et': 'P', 'dolore': 'Q', 'magna': 'R', 'aliqua': 'S', 'enim': 'T',
    'ad': 'U', 'minim': 'V', 'veniam': 'W', 'quis': 'X', 'nostrud': 'Y', 'exercitation': 'Z'
}

def decrypt_message(encrypted_message):
    """
    Decrypts a message by replacing Lorem Ipsum-style words with their corresponding letters A-Z.
    Non-alphabetic characters are preserved as is.
    Expects triple spaces between words.
    Handles any capitalization and leading/trailing punctuation.
    """
    decrypted_message = []
    words = encrypted_message.split('   ')  # Triple space between words

    for word in words:
        tokens = word.split()
        decrypted_letters = []
        for token in tokens:
            # Remove leading/trailing punctuation for matching
            stripped = token.strip(string.punctuation)
            key = stripped.lower()
            if key in lorem_cipher_reversed:
                # Preserve punctuation
                prefix = token[:len(token)-len(stripped)] if token.startswith(stripped) == False else ''
                suffix = token[len(stripped):] if token.endswith(stripped) == False else ''
                decrypted_letters.append(prefix + lorem_cipher_reversed[key] + suffix)
            else:
                decrypted_letters.append(token)
        decrypted_message.append(''.join(decrypted_letters))
    return ' '.join(decrypted_message)