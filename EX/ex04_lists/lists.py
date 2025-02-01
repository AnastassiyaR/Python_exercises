"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).
    """
    if not all_phones:
        return []
    return all_phones.split(",")


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).
    """
    if not all_phones:
        return []
    result = all_phones.split(",")
    # print("r", result)
    new = []
    for i in result:
        # join is used to make from list to string
        # [1:] is a list, while [1] is one value
        i = i.split()[0]
        if i not in new:
            new.append(i)
    return new


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).
    """
    if not all_phones:
        return []
    result = all_phones.split(",")
    print("r", result)
    new = []
    for i in result:
        # join is used to make from list to string
        # [1:] is a list, while [1] is one value
        i = ' '.join(i.split()[1:])
        # print("i", i)
        if i not in new:
            new.append(i)
    return new


def search_by_brand(all_phones: str, brand: str) -> list:
    """
    Search for phones by brand.

    The search is case-insensitive.
    """
    if not all_phones:
        return []
    result = all_phones.split(",")
    # print("r", result)
    new = []
    for i in result:
        if ''.join(i.lower().split()[:1]) == brand.lower():
            new.append(i.strip())
    return new


def search_by_model(all_phones: str, model: str) -> list:
    """
    Search for phones by model.

    The search is case-insensitive.
    """
    if not all_phones:
        return []
    result = all_phones.split(",")
    # print("r", result)
    new = []
    for i in result:
        for j in i.split()[1:]:
            if j.lower() == model.lower():
                new.append(i.strip())
    return new


if __name__ == '__main__':
    print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))
    # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    print(phone_brands("Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))
    # ['Google', 'Honor', 'IPhone', 'Samsung']
    print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))
    # ['Google']
    print(phone_brands(""))
    # []
    print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14"))
    # ['14', 'Pixel', 'Magic5']
    print(phone_models("IPhone 14 A,Google Pixel B,Honor Magic5,IPhone 14"))
    # ['14 A', 'Pixel B', 'Magic5', '14']
    print(phone_models(' a 11, b 12, hh Magic5, uu Pixel, phh Pixel2, ppp XS'))
    # ['Optimus Black']
    print(search_by_brand('IPhone X ,IPhone 12 Pro, IPhone 14 pro Max', "iphone"))
    # ['IPhone X', 'IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "pro"))
    # ['IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "1"))
    # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "IPhone"))
    # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "12 Pro"))
    # []
