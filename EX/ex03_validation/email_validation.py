"""Email validation."""


def has_at_symbol(email: str) -> bool:
    """
    Check if the e-mail address given as an argument of the function contains the @ symbol.

    :param email: email to be checked
    :return: True if the given email address contains the @ symbol
    """
    if "@" in email:
        return True
    else:
        return False


def is_valid_username(email: str) -> bool:
    """
    Check whether the username part of the email address contains special symbols (e.g. ?+-.,;:%¤#"&/).

    :param email: email to be checked
    :return: True if the username part of the given email address does not contain
    special symbols other than a period
    """
    name = email.split("@")
    print("nnn", name[0])
    if len(name) > 2:
        return False

    for i in name[0]:
        if not (i.isalnum() or i == '.'):
            return False
    return True


def find_domain(email: str) -> bool:
    """
    Check the domain of the email adress.

    :param email: email to be checked
    :return: domain of the email
    """
    return email.split("@")[-1]


def is_valid_domain(email: str) -> bool:
    """
    Check if the domain name contained in the email address is correct.

    :param email: email to be checked
    :return: True if the domain name part of the given email address passes validation.
    """
    email_split = email.split("@")
    print(email_split)
    if len(email_split) != 2:
        return False
    domain = email_split[1].lower()
    print("fff", domain)
    if domain.count(".") == 1:
        point = domain.index(".")
        without_point = domain.replace(".", "")
        # print(without_point)
        if 3 <= len(domain[:point]) <= 10 and 2 <= len(domain[point + 1:]) <= 5 and without_point.isalpha():
            return True
        else:
            return False
    else:
        return False


def is_valid_email_address(email: str) -> bool:
    """
    Check the correctness of the email address received as an argument of the whole function.

    :param email: email to be checked
    :return: True if the email address passes validation
    """
    if has_at_symbol(email) and is_valid_username(email) and is_valid_domain(email):
        return True
    else:
        return False


def create_email_address(domain: str, username: str) -> str:
    """
    Create a whole email address if it passes validations.

    :param email: email to be checked
    :return: Creates a correct email address with the given arguments
    otherwise output "Cannot create a valid email address using the given parameters!"
    """
    check_email = username + "@" + domain
    if is_valid_email_address(check_email):
        return check_email
    else:
        return "Cannot create a valid email address using the given parameters!"


if __name__ == '__main__':
    print("Email has the @ symbol:")
    print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
    print(has_at_symbol("joonas.kivigmail.com"))  # -> False

    print("\nUsername has no special symbols:")
    print(is_valid_username("martalumi@taltech.ee"))  # -> True
    print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
    print(is_valid_username("marta lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta@lumi@taltech.ee"))  # -> False

    print("\nFind the email domain name:")
    print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
    print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
    print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
    print(find_domain("karla@karu@yahoo.com"))  # -> yahoo.com

    print("\nCheck if the domain is correct:")
    print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
    print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
    print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
    print(is_valid_domain("pannkook@m.oos"))  # -> False

    print("\nIs the email valid:")
    print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
    print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

    print("\nCreate your own email address:")
    print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
    print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
    print(create_email_address("koobas.com",
                               "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!
