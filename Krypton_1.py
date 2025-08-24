"""ROT13 encryption and decryption module.

This module provides two functions, `encrypt_rot13` and `decrypt_rot13`, which
perform ROT13 transformation on a given string. Because ROT13 is symmetrical,
calling either function twice returns the original text.
"""

def encrypt_rot13(text: str) -> str:
    """Encrypt *text* using the ROT13 cipher.

    Parameters
    ----------
    text:
        The plaintext to encode.

    Returns
    -------
    str
        The ROT13 transformed string.
    """
    return _rot13(text)


def decrypt_rot13(text: str) -> str:
    """Decrypt *text* that was encoded with ROT13.

    Because ROT13 is symmetrical, this function is identical to
    :func:`encrypt_rot13`.

    Parameters
    ----------
    text:
        The ROT13 encrypted string.

    Returns
    -------
    str
        The decoded plaintext.
    """
    return _rot13(text)


def _rot13(text: str) -> str:
    """Return the ROT13 transformation of *text*.

    This helper performs the character substitution for both encryption and
    decryption.
    """
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    sample = "Hello, World!"
    encrypted = encrypt_rot13(sample)
    decrypted = decrypt_rot13(encrypted)
    print("Original:", sample)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
