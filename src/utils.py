def validate_input(message):
    """
    Validates the input message to ensure it is a string and not empty.
    
    Args:
        message (str): The message to validate.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    return isinstance(message, str) and bool(message.strip())

def format_encrypted_message(encrypted_message):
    """
    Formats the encrypted message for display by removing extra spaces.
    
    Args:
        encrypted_message (str): The encrypted message to format.
        
    Returns:
        str: The formatted encrypted message.
    """
    return ' '.join(encrypted_message.split())