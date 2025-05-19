# --- The Translation Function (remains the same) ---
def translate_mac_option_string(input_string):
    """
    Translates a string containing Mac Option-key modified characters
    back to their standard keyboard equivalents using the provided map.

    Args:
        input_string (str): The string with Option-modified characters.
        translation_map (dict): The dictionary mapping Option-modified
                                characters to their standard equivalents.

    Returns:
        str: The translated string.
    """

    translation_map = {
        # Option + Letters (map to lowercase letter)
        'å': 'a',  # Option + a
        '∫': 'b',  # Option + b
        'ç': 'c',  # Option + c
        '∂': 'd',  # Option + d
        # '´': 'e',  # Option + e (acute accent - dead key) - Handled by Opt+Shift+E preference if char is same
        'ƒ': 'f',  # Option + f
        '©': 'g',  # Option + g
        # '˙': 'h',  # Option + h (dot above - dead key)
        # 'ˆ': 'i',  # Option + i (circumflex accent - dead key)
        '∆': 'j',  # Option + j
        # '˚': 'k',  # Option + k (ring above - dead key)
        '¬': 'l',  # Option + l
        'µ': 'm',  # Option + m
        # '˜': 'n',  # Option + n (small tilde - dead key)
        'ø': 'o',  # Option + o
        'π': 'p',  # Option + p
        'œ': 'q',  # Option + q
        '®': 'r',  # Option + r
        'ß': 's',  # Option + s
        '†': 't',  # Option + t
        # '¨': 'u',  # Option + u (diaeresis - dead key)
        '√': 'v',  # Option + v
        '∑': 'w',  # Option + w
        '≈': 'x',  # Option + x
        '¥': 'y',  # Option + y
        'Ω': 'z',  # Option + z

        # Option + Number Row (map to number)
        '¡': '1',  # Option + 1
        '™': '2',  # Option + 2
        '£': '3',  # Option + 3
        '¢': '4',  # Option + 4
        '∞': '5',  # Option + 5
        '§': '6',  # Option + 6
        '¶': '7',  # Option + 7
        '•': '8',  # Option + 8
        'ª': '9',  # Option + 9
        'º': '0',  # Option + 0

        # Option + Symbols (map to unshifted symbol)
        '`': '`',  # Option + ` (grave accent - dead key)
        '–': '-',  # Option + - (en dash)
        '≠': '=',  # Option + =
        '‘': '[',  # Option + [ (left single quotation mark)
        '’': ']',  # Option + ] (right single quotation mark)
        '«': '\\',  # Option + \ (left-pointing double angle quotation mark)
        '…': ';',  # Option + ; (horizontal ellipsis)
        'æ': "'",  # Option + ' (ae ligature)
        '≤': ',',  # Option + , (less than or equal to)
        '≥': '.',  # Option + . (greater than or equal to)
        '÷': '/',  # Option + / (division sign)

        # --- Option + Shift Combinations ---
        # (These are listed after to ensure they take precedence if a character is identical
        # to one produced by Option + non-Shifted key, mapping to the shifted/uppercase base key)

        # Option + Shift + Letters (map to UPPERCASE letter)
        'Å': 'A',  # Option + Shift + A
        'Î': 'B',  # Option + Shift + B (Capital I-circumflex)
        'Ç': 'C',  # Option + Shift + C (Capital C-cedilla)
        'Ï': 'D',  # Option + Shift + D (Capital I-diaeresis)
        '¯': 'E',  # Option + Shift + E (Macron - can be dead key)
        'ı': 'F',  # Option + Shift + F (Latin small letter dotless i)
        '˝': 'G',  # Option + Shift + G (Double acute accent - dead key)
        'Ó': 'H',  # Option + Shift + H (Capital O-acute)
        'ˆ': 'I',  # Option + Shift + I (Circumflex accent - dead key, same char as Opt+i) -> maps to I
        'Ô': 'J',  # Option + Shift + J (Capital O-circumflex)
        '': 'K',  # Option + Shift + K (Apple logo)
        'Ò': 'L',  # Option + Shift + L (Capital O-grave)
        'Ú': 'M',  # Option + Shift + M (Capital U-acute)
        '˜': 'N',  # Option + Shift + N (Tilde - dead key, same char as Opt+n) -> maps to N
        'Ø': 'O',  # Option + Shift + O (Capital O-slash)
        'Π': 'P',  # Option + Shift + P (Greek capital letter Pi)
        'Œ': 'Q',  # Option + Shift + Q (Latin capital ligature OE)
        '‰': 'R',  # Option + Shift + R (Per mille sign)
        'Í': 'S',  # Option + Shift + S (Capital I-acute)
        'ˇ': 'T',  # Option + Shift + T (Caron - dead key)
        '¨': 'U',  # Option + Shift + U (Diaeresis - dead key, same char as Opt+u) -> maps to U
        '◊': 'V',  # Option + Shift + V (Lozenge)
        '„': 'W',  # Option + Shift + W (Double low-9 quotation mark)
        '˛': 'X',  # Option + Shift + X (Ogonek - dead key)
        'Á': 'Y',  # Option + Shift + Y (Capital A-acute)
        '¸': 'Z',  # Option + Shift + Z (Cedilla - dead key)

        # Option + Shift + Number Row (map to shifted number row symbol)
        '⁄': '!',  # Option + Shift + 1 (Fraction slash)
        '€': '@',  # Option + Shift + 2 (Euro sign)
        '‹': '#',  # Option + Shift + 3 (Single left-pointing angle quotation mark)
        '›': '$',  # Option + Shift + 4 (Single right-pointing angle quotation mark)
        'ﬁ': '%',  # Option + Shift + 5 (Latin small ligature fi)
        'ﬂ': '^',  # Option + Shift + 6 (Latin small ligature fl)
        '‡': '&',  # Option + Shift + 7 (Double dagger)
        '°': '*',  # Option + Shift + 8 (Degree sign)
        '·': '(',  # Option + Shift + 9 (Middle dot)
        '‚': ')',  # Option + Shift + 0 (Single low-9 quotation mark)

        # Option + Shift + Symbols (map to shifted symbol)
        '~': '~',  # Option + Shift + ` (Tilde - dead key, same char as Opt+n but from Shift+`)
        '—': '_',  # Option + Shift + - (Em dash)
        '±': '+',  # Option + Shift + = (Plus-minus sign)
        '“': '{',  # Option + Shift + [ (Left double quotation mark) - { is Shift + [
        '”': '}',  # Option + Shift + ] (Right double quotation mark) - } is Shift + ]
        '»': '|',  # Option + Shift + \ (Right-pointing double angle quotation mark) - | is Shift + \
        'Æ': '"',  # Option + Shift + ' (Latin capital ligature AE) - " is Shift + '
        '˘': '<',  # Option + Shift + , (Breve - dead key) - < is Shift + ,
        # Note: Opt+Sh+. (period) also produces '˛' (ogonek) on some layouts/viewers.
        # Since '˛' is already mapped to 'X' (from Opt+Sh+X), we keep that.
        # If Opt+Sh+. must map to '>', '˛' can't be its key.
        # Standard US Mac: Option+Shift+. is indeed '˛'. So no direct map to '>'.
        '¿': '?',  # Option + Shift + / (Inverted question mark)

        # Explicit handling for dead key characters that might have been produced by Option + lowercase letter
        # This ensures that if Opt+Shift+Letter producing the same character didn't override,
        # the lowercase letter source is still available.
        # However, the Opt+Shift definitions above will take precedence if the character is identical.
        '´': 'e',  # Option + e (acute accent - dead key)
        '˙': 'h',  # Option + h (dot above - dead key)
        # 'ˆ': 'i', # Already set to 'I' from Opt+Shift+i
        '˚': 'k',  # Option + k (ring above - dead key)
        # '˜': 'n', # Already set to 'N' from Opt+Shift+n
        # '¨': 'u', # Already set to 'U' from Opt+Shift+u
    }

    translated_chars = []
    for char in input_string:
        # Get the standard character from the map.
        # If the character is not in the map, default to the character itself.
        standard_char = translation_map.get(char, char)
        translated_chars.append(standard_char)

    return "".join(translated_chars).lower()
