"""Phone number."""

#1-3 DONE
def add_country_code(number: str) -> str:
    """
    Funktsioon lisab numbrile "+372 " ette, kui numbril pole maakoodi ("+...").
    Tagastab õigesti vormistatud numbri.
    :param number: number
    :return: number koos "+372"
    """
    if not number.startswith("+") and not " " in number:
        return "+372 " + number
    elif not number.startswith("+") and " " in number:
        return "+" + number
    else:
        return number

#4-10 DONE
def is_valid(number: str) -> bool:
    """
    Funktsioon tagastab True, kui number on korrektne ja False, kui ei ole.

    :param number: number
    :return: True if vali
    """
    number_split = number.split(" ", 1)
    if len(number_split) == 2:
        # print(number_split[1])
        if number.startswith("+") and number_split[0][1:].isdigit() and len(number_split[1]) >= 7 and number_split[1].isdigit():
            return True
    return False

#11-16 DONE
def remove_unnecessary_chars(number: str) -> str:
    """
    Funktsioon eemaldab antud sõnest (mis peaks olema telefoninumber).

    Eemaldab kõik tähed ja erisümbolid (v.a '+' enne maakoodi ja tühik pärast maakoodi)
    :param number:
    :return: a valid number
    """
    new = ''
    number.replace(" ", "")
    # print(number)

    for i in number:
        # Check if the number is valid after adding country code
        if i == "+" and len(new) == 0 or i.isdigit() or i == " " and new.startswith("+") and not " " in new and len(new) > 1:
            new += i

    if " " not in new and new.startswith("+"):
        new = new.replace("+", "")

    # print("new", new)
    return new

#DONE
def get_last_numbers(numbers: list[str], n: int) -> list[str]:
    """
    Funktsioon tagastab n viimast telefoninumbrit antud järjendist.

    :param number:
    :return:
    """
    if n <= 0:
        return []
    return numbers[-n:]

#21-26
def get_first_correct_number(names: list[str], numbers: list[str], name: str) -> str | None:
    """
    Funktsioon peab tagastama esimese korrektselt vormistatud telefoninumbr.
    mis vastab otsitava kontakti nimele.

    :param number:
    :return:
    """

    for i in range(len(names)):
        # print(i, names[i].lower())
        # print("kk", name.lower())
        if names[i].lower() == name.lower():
            if is_valid(numbers[i]):
                return numbers[i]
    return None


#27-32
def correct_numbers(numbers: list[str]) -> list[str]:
    """
    Function receives a list of phone numbers that may not be valid.

    :param numbers: List of phone numbers as strings
    :return: List of corrected phone numbers
    """
    new_numbers = []

    for i in numbers:
        # Check if the number is valid after adding country code
        if not is_valid(add_country_code(i)):
            check = remove_unnecessary_chars(i)
            if is_valid(add_country_code(check)):
                new_numbers.append(add_country_code(check))
        else:
            new_numbers.append(add_country_code(i))
    return new_numbers


#33-37
def get_names_of_contacts_with_correct_numbers(names: list[str], numbers: list[str]) -> list[str]:
    """
    Funktsioon peab tagastama järjendi kontaktidest (nimedest ainult), mille telefoninumbrid on korrektsed

    :param number:
    :return:
    """
    new = []
    for j in numbers:
        # print("j", j)
        # print("1", add_country_code(j))
        # print("2", is_valid(add_country_code(j)))
        if is_valid(j):
            new.append(names[numbers.index(j)].title())
    return new


if __name__ == '__main__':
    #print(get_last_numbers(["+372 1234567", "+372 1234567", "+372 1234567", "+372 1234767"], 2))
    #print(add_country_code("372 1234567"))
    #print(is_valid("+12 3456789"))
    #print(is_valid("456"))
    #print(is_valid("+372123456"))
    #print(is_valid("+372A12345*7"))
    #print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 2))
    #print(get_last_numbers(["+372 1234567"], 3))
    #print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 0))
    #print(correct_numbers(["+372 12345", "1234567", "+111 23456789", "456"]))
    #print(correct_numbers(["1234567", "+1 234567890", "5551234", "+372 51234567", "+372 59876543"]))
    #print(correct_numbers(["+372 123456", "+44 1234567AAA", "555-1234"]))
    #print(correct_numbers(["555-1234", "123", "AAAAA"]))
    #print(correct_numbers(["5234", "123", "A8AA", "+1 12345"]))
    #print(remove_unnecessary_chars("+abc 12 3456789"))
    #print(remove_unnecessary_chars("+++37ooo2 1234+AAA567"))
    #print(remove_unnecessary_chars(" 123+h n456!7"))
    #print(remove_unnecessary_chars("+abc   ++ "))
    #print(remove_unnecessary_chars("+abc 12 3456 789"))
    #print(remove_unnecessary_chars("45678"))
    print(get_first_correct_number(["Alice Smith", "Bob Brown", "Carol White"], ["555-1234", "+1 234567890", "+1 234567890"], "Alice Smith"))
    print(get_first_correct_number(["alice Smith", "Alice Smith", "ALICE Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234567890", "+44 1234567"], "Alice Smith"))
    print(get_first_correct_number(["Alice Smith", "Alice Smith", "Alice Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234-567890", "+44 123AA567"], "A"))
    #print(get_names_of_contacts_with_correct_numbers(["ALICE Smith", "Bob Brown", "Carol White"], ["+372 1234567", "555-1234", "+1 234567890"]))
    #print(get_names_of_contacts_with_correct_numbers(["Alice Smith", "Bob Brown", "Carol White"], ["+372 123456", "555-1234", "*1 234567890"]))
