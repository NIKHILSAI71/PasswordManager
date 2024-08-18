import secrets
import string

def generate_strong_password(length=12, require_uppercase=True, require_lowercase=True, require_digits=True, require_special=True):
    """Generates a strong password with specified criteria.

    Args:
        length (int, optional): Password length. Defaults to 12.
        require_uppercase (bool, optional): Require at least one uppercase letter. Defaults to True.
        require_lowercase (bool, optional): Require at least one lowercase letter. Defaults to True.
        require_digits (bool, optional): Require at least one digit. Defaults to True.
        require_special (bool, optional): Require at least one special character. Defaults to True.

    Returns:
        str: The generated password.
    """

    characters = string.ascii_letters + string.digits + string.punctuation
    characters = characters.replace('l', '').replace('I', '').replace('O', '').replace('0')

    # Ensure at least one of each required character type
    password = ""
    if require_uppercase:
        password += secrets.choice(string.ascii_uppercase)
    if require_lowercase:
        password += secrets.choice(string.ascii_lowercase)
    if require_digits:
        password += secrets.choice(string.digits)
    if require_special:
        password += secrets.choice(string.punctuation)

    # Fill the rest of the password with random characters
    password += ''.join(secrets.choice(characters) for i in range(length - len(password)))

    # Shuffle the password for better randomness
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password