"""Base64 encoding and decoding utilities.

This module offers two simple functions, `encode_base64` and
`decode_base64`, for converting between plain text and its Base64
representation.
"""

from __future__ import annotations

import base64


def encode_base64(text: str) -> str:
    """Return the Base64 encoded form of *text*.

    Parameters
    ----------
    text:
        The plaintext string to encode.

    Returns
    -------
    str
        The Base64 representation of *text*.
    """
    raw_bytes = text.encode("utf-8")
    encoded_bytes = base64.b64encode(raw_bytes)
    return encoded_bytes.decode("ascii")


def decode_base64(encoded: str) -> str:
    """Return the decoded plaintext from Base64 string *encoded*.

    Parameters
    ----------
    encoded:
        A Base64 encoded string.

    Returns
    -------
    str
        The decoded plaintext.
    """
    encoded_bytes = encoded.encode("ascii")
    raw_bytes = base64.b64decode(encoded_bytes)
    return raw_bytes.decode("utf-8")


if __name__ == "__main__":
    sample = "Hello, Base64!"
    encoded = encode_base64(sample)
    decoded = decode_base64(encoded)
    print("Original:", sample)
    print("Encoded:", encoded)
    print("Decoded:", decoded)
