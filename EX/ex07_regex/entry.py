"""Entry."""
import re


def parse(row: str) -> tuple:
    """
    Parse string row into a tuple.

    The row has a first name, last name, ID code, phone number, date of birth and address.
    Only ID code is mandatory, other values may not be included.

    They can be found by the following rules:
    - Both the first name and last name begin with a capital letter and are followed by at least one lowercase letter
    - ID code is an 11-digit number
    - Phone number has the same rules applied as in the first part
    - Date of birth is in the form of dd-MM-YYYY
    - Address is everything else that's left

    :param row: given string to find values from
    :return: tuple of values found in given string
    """
    result = ()

    # names
    pattern_name = r'^([A-Z][a-z]+)([A-Z][a-z]+)'
    match_name = re.match(pattern_name, row)
    if match_name:
        result += match_name.groups()
    else:
        result += (None, None)

    # ID
    pattern_ID = r'(\d{11})'
    match_ids = re.search(pattern_ID, row)
    # print("SO", match_ids)
    if match_ids:
        result += match_ids.groups()
    else:
        result += (None,)
    # print("result with IDS", result)

    # Phone number
    pattern_phone_numbers = r'\d{11}?(\+\d{3}\s?|\s|)(\d{7,8})'
    # r'(\+\d{3}?\s?\d{7,8})', '(\+\d{3}\s?|\s)(\d{7,8})'
    # print("SyyO", re.findall(pattern_phone_numbers, row))
    match_phone_numbers = re.search(pattern_phone_numbers, row)
    if match_phone_numbers:
        match = ''.join(match_phone_numbers.groups()).strip()
        result += (match,)
    else:
        result += (None,)
    # print("result with numbers", result)

    # Date
    pattern_date = r'(\d{2}-\d{2}-\d{4})'
    match_date = re.search(pattern_date, row)
    # print("SO", match_date)
    if match_date:
        result += match_date.groups()
    else:
        result += (None,)
    # print("result with date", result)

    # Address
    pattern_address = r'([A-Z][a-z]+(?= ).*$)'
    match_address = re.search(pattern_address, row)
    if match_address:
        result += match_address.groups()
    else:
        result += (None,)

    return result


if __name__ == '__main__':
    print(parse('PriitPann397120476235688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')

    print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # (None, None, '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')

    print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', None, '02-12-1998', 'Oja 18-2,Pärnumaa,Are')

    print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', None, 'Oja 18-2,Pärnumaa,Are')

    print(parse('39712047623'))
    # (None, None, '39712047623', None, None, None)
