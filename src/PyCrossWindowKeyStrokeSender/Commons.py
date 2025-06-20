def to_utf16_codes(text : str) -> list[int]:
    """
    Converts text to list of utf-16 codes.
    """
    codes = text.encode("utf-16-be")

    utf16_codes = []
    for ix in range(0, len(codes), 2):
        utf16_codes += [(codes[ix] << 8) | codes[ix + 1]]

    return utf16_codes

