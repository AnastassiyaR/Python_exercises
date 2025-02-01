"""pizza_kiosk."""
import re


def is_correct_name(ingredient: str) -> bool:
    """
    Kontrollib, kas koostisosa nimetus on õigesti kirjutatud, ning tagastab vastavalt True või False.

    Nimetus ei tohi sisaldada erisümboleid, numbreid ega suurtähti. Samuti ei tohi nimetus olla tühi sõne.
    """
    control = r'^[a-zäöõü]+$'  # $ значит до конца
    if ingredient and re.match(control, ingredient):
        return True
    return False


def fix_names(ingredients: list) -> list:
    """
    Tagastada tuleb järjend õigesti kirjutatud sõnedest.

    Sõned peavad olema kirjutatud läbivalt väikese tähega (suured tähed peab väikesteks tegema) ning ei tohi sisaldada
    erisümboleid ega numbreid. Samuti ei või sõne olla tühi.
    """
    result = []
    for ingredient in ingredients:
        ingredient = ''.join(map(lambda x: x.lower(), filter(lambda char: char.isalpha(), ingredient)))
        if ingredient:  # Проверка, что строка не пуста, то есть не "45456"
            result.append(ingredient)

    return result


def pizza_at_index(pizzas: list, pizza: str) -> str:
    """
    Funktsioon peab leidma järjendist pitsa, mille indeksiks on antud pitsa esinemiste arv selles järjendis.

    Kui antud indeksiga elementi ei eksisteeri, tagasta tühi sõne.

    Näide: pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "juustupitsa") ->
    "kanapitsa" (järjendis on 1 juustupitsa, seega indeksiks on 1)
    """
    if pizza == '':
        return ''
    control = sum(map(lambda i: +1 if i == pizza in pizzas else 0, pizzas))

    return pizzas[control] if control < len(pizzas) else ''  # условие чтобы не было list index out of range


def format_orders(nr_order: list) -> dict:
    """
    Funktsioon peab koostama sõnastiku kõikidest tellimustest, kus võtmeks on tellimuse number täisarvuna.

    Sõnastik peab jääma samasse järjekorda kui etteantud järjend.
    Näide: format_orders(["5&kanapitsa", "1&pepperoni", "20&MeXican"]) -> {5: "kanapitsa", 1: "pepperoni", 20: "mexican"}
    """
    result = {}
    for i in nr_order:
        split_pattern = r'(\d+)&([A-Za-z]+)'
        match = re.match(split_pattern, i.lower())
        if match:
            result[int(match.group(1))] = match.group(2)
    return result


def calculate_income(prices: str) -> float:
    """
    Tagastada tuleb hindade summa ujukomaarvuna.

    Hinnad koosnevad alati neljast numbrist, kus punkt eraldab täis- ja murdarvu osa.
    Kui punkt on kusagil mujal erisümbolite keskel, siis see ei ole seotud hinnaga.
    Sõnes ei ole numbreid, mis pole seotud hinnaga.

    Lahendus peab olema rekursiivne.

    Näide: calculate_income("15.03*05.99|)=01.20&.$50.37") -> 72.59
    """
    if not prices:
        return 0.0

    if prices[0].isdigit():
        first_num = float(prices[:5])  # у нас стрингы
        other_num = prices[5:]  # заменяешь первую, ну убираешь число
        return first_num + calculate_income(other_num)
    else:
        return calculate_income(prices[1:])


def switch_keys_and_values(pizza_orders: dict) -> dict:
    """
    Ülesandeks on vahetada ära sõnastiku võtmed ja väärtused.

    Ette antud sõnastikus on võtmeks pitsa nimi ning väärtuseks järjend kõikidest tellimuste numbritest,
    mis sisaldavad seda pitsat.

    Näide: {"kanapitsa": [1, 5, 3, 4], "juustupitsa": [1, 2], "pepperoni": [1, 5, 3]} -> {1: ["kanapitsa", "juustupitsa", "pepperoni"], 5: ["kanapitsa", "pepperoni"], 3: {"kanapitsa", "pepperoni"], 4: ["kanapitsa"], 2: ["juustupitsa"]}
    """
    result = {}

    for list_num in pizza_orders.values():
        for num in list_num:
            result[num] = []

    for name, num in pizza_orders.items():
        for i in num:
            for y in result.keys():
                if y == i:
                    result[i].append(name)

    return result


def count_ingredients(menu: dict, orders: list) -> dict | None:
    """
    Funktsioon loeb kokku, kui palju iga koostisosa tellimuse jaoks vaja läheb ja tagastab tulemuse sõnastikuna.

    Kui tellimuses on mõni pitsa, mida sõnastikus pole, tagasta tühi sõnastik.

    count_ingredients({"margarita": ["juust", "tomat", "kaste"], "pepperoni": ["juust", "kaste", "pepperoni"]}, ["margarita", "margarita", "pepperoni"]) ->
    {"juust": 3, "kaste": 3, "tomat": 2, "pepperoni": 1}
    """
    if any(map(lambda order: order not in menu, orders)):
        return {}

    all_ingredients = list(map((lambda pizza: menu[pizza]), filter(lambda order: order in menu, orders)))  # Для каждой пиццы (каждого заказа) найди её ингредиенты в словаре menu".
    toitud = [ingredient for ingredients in all_ingredients for ingredient in ingredients]  # [[], [], []]

    result = {}
    print(toitud)
    for toit in toitud:
        if toit in result.keys():
            result[toit] += 1
        else:
            result[toit] = 1

    return result


def match_pizzas_with_prices(pizzas: list, prices: list) -> list:
    """
    Funktsioon eemaldab pitsade järjendist valesti kirjutatud või korduvad pitsade nimetused.

    Valesti kirjutatud nimetused sisaldavad suurtähti, numbreid või erisümboleid.

    Kui peale seda on pitsade ja hindade järjendid sama pikad, tagastada järjend ennikutest,
    kus esimene element on pitsa nimetus, teine hind.
    Kui järjendid on erineva pikkusega, tagasta tühi järjend.

    NB! Pitsade järjekord on oluline
    Näide: match_pizzas_with_prices(["pepperoni", "margarita", "ch7eese", "cheese", "margarita"], [3.99, 4.99, 3.99]) -> [("pepperoni", 3.99), ("margarita", 4.99), ("cheese", 3.99)]
    """
    new_pizzas = list(filter(lambda x: x.islower() and x.isalpha(), pizzas))

    if len(set(new_pizzas)) == len(prices):  # Kui järjendid on erineva pikkusega, tagasta tühi järjend. ПОСЛЕ ПРОВЕРКИ
        result = list(map(lambda x: (x[0], x[1]), zip(new_pizzas, prices)))  # x[0] - new_pizzas, x[1] - prices
        return result
    return []


if __name__ == "__main__":
    print(is_correct_name("WEDDF243"))
    print(fix_names(['555', "345"]))
    print(pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "juustupitsa"))
    print(format_orders(["5&kanapitsa", "1&pepperoni", "20&MeXican"]))
    print(switch_keys_and_values({"kanapitsa": [1, 5, 3, 4], "juustupitsa": [1, 2], "pepperoni": [1, 5, 3]}))
    print(count_ingredients({"margarita": ["juust", "tomat", "kaste"], "pepperoni": ["juust", "kaste", "pepperoni"]}, ["margarita", "margarita", "pepperoni"]))
    print(match_pizzas_with_prices(["pepperoni", "argarita", "f",], [3.99, 4.99, 3.99]))
    print(calculate_income("15.03*05.99|)=01.20&.$50.37"))
