__all__ = [
    "to_utf16_codes",
]

def to_utf16_codes(text):
    """
    Converts text to list of utf-16 codes.
    text : str
    return list(int)
    """
    codes = text.encode("utf-16-be")

    utf16_codes = []
    for ix in range(0, len(codes), 2):
        utf16_codes += [(codes[ix] << 8) | codes[ix + 1]]

    return utf16_codes

