"""Exam 2 (09.01.2025)."""
import re
def kebab_to_camel(kebab_str: str) -> str:
    """
    Convert the function name from kebab case to camel case.

    * Kebab case is a way of naming methods with "-" between words.
    * Camel case is a way of naming methods with the first letter being lowercase and other words being uppercase.
    * Your job is to convert a method name in kebab case to camel case.
    * If the input is an empty string or consists of only spaces return "".

    kebab_to_camel("this-is-function-name") => "thisIsFunctionName"
    kebab_to_camel("hello-hello-world") => "helloHelloWorld"

    :param kebab_str: Method name in kebab case to convert into camel case.
    :return: Method name that has been converted to camel case.
    """
    result = ''

    words = kebab_str.split('-')
    for word in words:
        if word.isalpha():
            if result:
                result += word.title()
            elif word == words[0]:
                result += word.lower()

    return result


def find_tagged_content(html_text: str, tag: str) -> str:
    """
    Extract the content between the specified HTML tags.

    * The opening tag is in the format: <tag>
    * The closing tag is in the format: </tag>
    * Return the text between the opening and closing tag (in that order) if the tag matches the given one.
    * If there are multiple matching tags, then add the contents together and return it (example 3).
    * If no matching tag is found or the given html_text is empty return an empty string.

    * You will NOT have to deal with cases of nested tags (<div>Hello<p>World</p>!<div>).

    find_tagged_content("<p>Wrong tag</p>", "div") => ""
    find_tagged_content("<p>Correct tag</p>", "p") => "Correct tag"
    find_tagged_content("<div>First</div><p>Ignore this, wrong tag</p><div>Second</div>", "div") => "FirstSecond"

    :param html_text: The input string containing HTML-formatted text.
    :param tag: The HTML tag to extract the content from.
    :return: A string containing the content inside the specified tag, or an empty string if no match is found.
    """
    if not html_text or not tag:
        return ""

    # Create a regex pattern to match the opening and closing tags
    pattern = r'<{}>(.*?)</{}>'.format(tag, tag)

    # Find all matches in the html_text
    matches = re.findall(pattern, html_text)

    # Join all matches into a single string
    return ''.join(matches)


def treasure_hunt(inventory: list, upgradable_items: list) -> list:
    """
    Manage inventory.

    Remove duplicates from the inventory. Only first occurrences of every item should remain.
    Additionally upgrade items that can be upgraded.
    upgradable_items is a list of lists, where the first word in each list is an upgradable item and the second is the
    item it can be upgraded to.
    You can assume that every given item is in lower-case.

    inventory = ["stone", "rope", "stone", "torch", "stone"]
    upgradable_items = [["stone", "gem"],  ["rope", "golden rope"]]
    treasure_hunt(inventory, upgradable_items) => ["gem", "golden rope", "torch"]

    :param inventory: List of current items.
    :param upgradable_items: List of lists that show upgrading rules.
    :return: List of items, where duplicates are removed and items have been upgraded.

    ["gem", "golden rope", "torch"]
    """

    new_inventory = []
    result = []
    inventory
    print('before', inventory)
    print('after', upgradable_items)
    removing_items = []
    a = []

    for item in inventory:
        for items in upgradable_items:
            print(item, items[0])
            if item == items[0]:
                a.append(items[1])
                print('a', a)
            else:
                a.append(item)

    print('update', new_inventory, removing_items)

    for item in zip(inventory):
        if not item in result:
            result.append(item)

    for item in inventory:
        if item not in removing_items and item not in result:
            result.append(item)

    return result


def get_average_grades(students_subjects_and_grades: dict) -> dict:
    """
    Get average grade for each subject.

    Given a dictionary where keys are students names and values are lists of tuples of subjects and grades,
    find the average grade for each subject for all students.

    If students_subjects_and_grades dictionary is empty, return a new dictionary.
    If students_subjects_and_grades dictionary has an empty list for a value,
    that should not change the average grades.

    examples:
        get_average_grades({}) -> {}

        get_average_grades(
            {
                "Mati": [('füüsika', 3), ('keemia', 3)],
                "Mari": [],
            }
        ) -> {'füüsika': 3.0, 'keemia': 3.0}

        get_average_grades(
            {
                "Mati": [('füüsika', 3), ('keemia', 3)],
                "Mari": [('füüsika', 4)]
            }
        ) -> {'füüsika': 3.5, 'keemia': 3.0}

    :param students_subjects_and_grades: dictionary where key is student name and value is
        the list of tuples of subjects they took and grades they got.
    :return: dictionary where key is subject name and value is the average grade for
        that subject rounded to two decimal places.
    """
    if not students_subjects_and_grades:
        return {}

    sum = {}
    grades = {}
    result = {}

    for scoops in students_subjects_and_grades.values():
        for j in scoops:
            subject, grade = j

            if subject not in grades:
                grades[subject] = grade
                sum[subject] = [grade]
            else:
                grades[subject] += grade
                sum[subject].append(grade)

    for subject, grade in grades.items():
        for sub, s in sum.items():
            if subject == sub:
                result[sub] = round(grade / len(s), 2)

    return result


def music_notes(chords: list, chord_book: dict) -> list:
    """
    Find the notes played from the list of chords using the chord book.

    You are given the list of chords being played and a dictionary of chords: lists of notes.
    Find the sequence of notes that the chords list corresponds to.

    Solution must be recursive!

    * If no chords are played (chords list is empty), return an empty list.
    * If no chords are given in the chord book, return all the chords played.
    * All played chords will always have a match in the chord book, so all given chords must be decomposed into notes.
    * The position of returned notes in the list should match the position of corresponding chords.

    examples:
    music_notes(["A", "B", "C"], {}) -> ["A", "B", "C"]

    music_notes(
        [],
        {
            "C": ["C", "E", "G"],
            "Am": ["A", "C", "E"],
        }
    ) -> []

    music_notes(
        ["C", "Am"],
        {
            "C": ["C", "E", "G"],
            "Am": ["A", "C", "E"],
        }
    ) -> ["C", "E", "G", "A", "C", "E"]

    :param chords: list of strings as chords played
    :param chord_book: dictionary of what chords are made up of what notes
    :return: list of notes played


    .............................
    print("music_notes:")
    print(music_notes(["A", "B", "C"], {}))  # -> ["A", "B", "C"]
    print(music_notes(
        [],
        {
            "C": ["C", "E", "G"],
            "Am": ["A", "C", "E"],
        }
    ))  # -> []
    print(music_notes(
        ["C", "Am"],
        {
            "C": ["C", "E", "G"],
            "Am": ["A", "C", "E"],
        }
    ))  # -> ["C", "E", "G", "A", "C", "E"]
    print()
    """
    if not chord_book:
        return chords
    if not chords:
        return chords


    for group, notes in chord_book.items():
        if group in chords:
            chords.remove(group)
            chords.extend(notes)
            chord_book.pop(group)
            return music_notes(chords, chord_book)


def count_neighbors(arr: tuple[tuple[bool, ...], ...]) -> list[list[int]]:
    """Count the number of neighboring `True` cells for each `True` cell in a 2D grid.

    This function calculates the number of `True` neighbors for each `True` cell in the provided 2D grid.
    A neighbor is any adjacent `True` cell, including diagonal, vertical, and horizontal neighbors.
    `False` cells are considered to have no neighbors (0).

    For example:
    (
        (False, False, True),
        (False, True,  True),
        (True,  False, True),
    )

    should return
    [
        [0, 0, 2],
        [0, 4, 3],
        [1, 0, 2],
    ]

    Args:
        arr: A collection of tuples, each representing a row in the grid,
          and each element representing a cell.

    Returns:
        A list of lists with the same dimensions as the provided 2D grid.
        Each element corresponds to the count of neighboring cells
        for the respective cell in the provided grid.
    """
    pass



class Animal:
    """
    Represents an animal in the zoo.

    Attributes:
        name (str): The name of the animal. Stored in capitalized form.
        species (str): The species of the animal. Stored in capitalized form.
        age (int): The age of the animal in years.
    """

    def __init__(self, name: str, species: str, age: int):
        """
        Initialize an Animal.

        :param name: The name of the animal. Will be capitalized.
        :param species: The species of the animal. Will be capitalized.
        :param age: The age of the animal in years.
        """
        self.name = name.title()
        self.species = species.title()
        self.age = age

    def __repr__(self):
        """
        Return a string representation of the animal.

        Format:
            "{Name} the {Species} ({Age} years old)"

        :return: A string describing the animal.
        """
        return f"{self.name} the {self.species} ({self.age} years old)"


class Zoo:
    """Represents a zoo with a collection of animals and cages."""

    def __init__(self):
        """
        Initialize a Zoo.

        animals (list): A list to store Animal objects currently in the zoo.
        cages (dict): A dictionary where keys are cage numbers and values are lists of animals assigned to those cages.
        """
        self.animals = []
        self.cages = {}

    def add_animal(self, animal: Animal):
        """
        Add an Animal to the zoo.

        :param animal: The Animal object to be added.
        :raises ValueError: If an animal is already in the zoo.

        Details:
        - This method ensures no duplicate animals are added to the zoo.
        - Equality is determined based on all attributes: `name`, `species`, and `age`.
        """
        if animal in self.animals:
            raise ValueError("Animal is already in the zoo.")

        self.animals.append(animal)

    def remove_animal(self, animal: Animal):
        """
        Remove an Animal from the zoo and its assigned cage (if applicable).

        :param animal: The Animal object to be removed.
        :raises ValueError: If the animal is not found in the zoo.

        Details:
        - Removes the animal from the zoo's `animals` list.
        - If the animal is assigned to a cage, it is removed from the cage.
        - If a cage becomes empty after removing the animal, the cage is deleted from `cages`.
        """
        if animal not in self.animals:
            raise ValueError("Animal is not in the zoo.")

        if animal in self.cages:
            self.cages.pop(animal)

        self.animals.remove(animal)

    def find_animals_by_species(self, species: str) -> list:
        """
        Find all animals of a specific species in the zoo.

        :param species: The species to search for. The search is case-insensitive.
        :return: List of Animal objects that belong to the specified species.

        Note:
        - Species matching is case-insensitive, so "Lion" and "lion" are treated the same.
        """
        result = []
        for i in self.animals:
            if i.species.lower() == species.lower():
                result.append(i)

        return result

    def get_animals_sorted_by_name(self) -> list:
        """
        Return a list of all animals in the zoo, sorted alphabetically by name.

        :return: List of Animal objects sorted by their names in case-insensitive alphabetical order.
        """
        return sorted(self.animals, key=lambda animal: animal.name)

    def assign_to_cage(self, animal: Animal, cage_number: int):
        """
        Assign an animal to a cage.

        :param animal: The Animal object to assign.
        :param cage_number: The cage number to assign the animal to.
        :raises ValueError:
            - If the animal is not part of the zoo.
            - If the animal is already in the specified cage.
            - If the cage contains animals of a different species.

        Details:
        - A cage can only contain animals of the same species.
        - If the cage does not exist, it will be created.
        - If the cage already exists and contains animals of the same species, the new animal is added.
        """
        if animal not in self.animals or animal in self.cages:
            raise ValueError("Cage is already assigned to the cage.")

        if cage_number not in self.cages:
            self.cages[cage_number] = []
        if cage_number in self.cages:
            if all(i.species == animal.species for i in self.cages[cage_number]):
                self.cages[cage_number].append(animal)
            else:
                raise ValueError("Cage number is already assigned to the cage.")


class Grade:
    """Grade."""

    def __init__(self, grade, weight: int, assignment: str, date: str):
        """Initialize grade."""
        self.assignment = assignment
        self.value = grade
        self.weight = weight
        self.date = date
        self.previous_grades = {}

    def change_grade(self, new_grade: int, date: str):
        """
        Change a previous grade.

        This function should save the previous grade in a dictionary previous_grades, where key is the date and value
        is the value of the grade. Value and date should be updated.
        """
        if date not in self.previous_grades:
            self.previous_grades[date] = [self.value]
        else:
            self.previous_grades[date].append(self.value)

        self.value = new_grade
        self.date = date


class Student:
    """Student."""

    def __init__(self, name: str):
        """Initialize student."""
        self.name = name
        self.grades = {}

    # jjjj: [4, 5, 6]
    def grade(self, grade: Grade):
        """
        Add a grade for an assignment that a students has done.

        Grades are kept in a dictionary where
        assignment name is the key
        and Grade object is the value (All previous
        grades for the same assignment are kept in the Grade object previous grades dictionary).
        Note that this function is only used when a student does an assignment for the first time.
        """
        if grade.assignment not in self.grades:
            self.grades[grade.assignment] = grade
        else:
            # Update the existing grade
            self.grades[grade.assignment].change_grade(grade.value, grade.date)

        if not grade.assignment or not grade.date:
            raise ValueError("Assignment cannot be empty.")

        if grade.assignment not in self.grades:
            self.grades[grade.assignment] = [grade]
        else:
            self.grades[grade.assignment].append(grade)

    def redo_assignment(self, new_grade: int, assignment: str, date: str):
        """
        Update the grade for given assignment.

        This function is only used when an assignment has been attempted at least once before. Keep in mind that you
        need to also keep the history of grades, not create a new grade!
        """
        if assignment not in self.grades.keys():
            raise ValueError("Assignment cannot be empty.")

        self.grades[assignment].change_grade(new_grade, date)


    def calculate_weighted_average(self):
        """
        Calculate the weighted average of grades.

        You should take into account the weights. There are three weights: 1, 2 and 3, where 3 means that one grade of
        weight 3 is the same as three grades of weight 1.

        For example:
        if there are grades 4 with weight 3 and 3 with weight 1, then the resulting value will be
                (4 * 3 + 3 * 1) / (3 + 1) = 15 / 4 = 3.75
        which will be rounded to 4.

        Also make sure not to miss out when a grade is noted as "!". If there is no attempt to redo this, then "!"
        should be equivalent to grade "1".
        """
        total_weighted_score = 0
        total_weight = 0

        for grade in self.grades.values():
            if grade.value == '!':
                grade.value = 1
            total_weighted_score += grade.value * grade.weight
            total_weight += grade.weight

        if total_weight == 0:
            return 0

        return round(total_weighted_score / total_weight)


class Class:
    """Class."""

    def __init__(self, teacher: str, students: list):
        """Initialize class."""
        self.teacher = teacher
        self.students = students

    def add_student(self, student: Student):
        """Add student to the class."""
        if student not in self.students:
            self.students.append(student)

    def add_students(self, students: list):
        """Add several students to the class."""
        for i in students:
            self.students.append(i)

    def remove_student(self, student: Student):
        """Remove student from the class."""
        if student in self.students:
            self.students.remove(student)

    def get_grade_sheet(self):
        """
        Return grade sheet as a table.

        Grade sheet includes information of all the students in the class and their final grades.
        All edges should be either "|" or "-".
        First column is student's name and the second column is the final grade (weighted average).
        First, second and third row should look something like this (notice the capital letters):
        ----------------------
        | Name | Final grade |
        ----------------------

        Make sure that all the columns are correctly aligned after the longest element.
        For example, consider following rows:
        | Ago                   |  5  |
        | Some really long name |  3  |

        Rules are following:
        Each row (except for "-----" rows) starts with "|" and a space " " and ends with a space " " and "|".
        Text in "Name" column needs to be aligned to left
        Grades in "Final grade" column need to be centered

        Students in the table should follow the order which they were added to the class.

        The whole table would look something like this:
        ---------------------------------------
        | Name                  | Final grade |
        ---------------------------------------
        | Ago                   |      5      |
        | Johannes              |      4      |
        | Mari                  |      5      |
        | Some really long name |      3      |
        ---------------------------------------

        """
        # Determine the maximum length of student names for formatting
        max_name_length = max(len(student.name) for student in self.students)
        name_column_width = max(max_name_length, len("Name"))
        grade_column_width = len("Final grade") + 2  # Add padding

        # Header
        header = f"| {'Name':<{name_column_width}} | {'Final grade':^{grade_column_width}} |"
        separator = "-" * len(header)

        # Prepare rows for each student
        rows = []
        for student in self.students:
            final_grade = student.calculate_weighted_average()
            rows.append(f"| {student.name:<{name_column_width}} | {final_grade:^{grade_column_width}} |")

        # Combine everything into the final table
        grade_sheet = [separator, header, separator] + rows + [separator]
        return "\n".join(grade_sheet)


if __name__ == "__main__":
    print("kebab_to_camel:")
    print(kebab_to_camel("this-is-function-name"))  # => "thisIsFunctionName"
    print(kebab_to_camel("hello-hello-world"))      # => "helloHelloWorld"
    print(kebab_to_camel("    hello-world"))        # => helloWorld
    print()

    print("find_tagged_content:")
    print(find_tagged_content("<p>Wrong tag</p>", "div"))  # => ""
    print(find_tagged_content("<p>Correct tag</p>", "p"))  # => "Correct tag"
    print(find_tagged_content("<div>First</div><p>Ignore this, wrong tag</p><div>Second</div>", "div"))  # => "FirstSecond"
    print()

    print("treasure_hunt")
    inventory = ["stone", "rope", "stone", "torch", "stone"]
    upgradable_items = [["stone", "gem"], ["rope", "golden rope"]]
    print(treasure_hunt(inventory, upgradable_items))  # => ["gem", "golden rope", "torch"]
    print()

    print("get_average_grades:")
    print(get_average_grades({}))  # -> {}
    print(get_average_grades(
        {
            "Mati": [('füüsika', 3), ('keemia', 3)],
            "Mari": [],
        }
    ))  # -> {'füüsika': 3.0, 'keemia': 3.0}

    print(get_average_grades(
        {
            "Mati": [('füüsika', 3), ('keemia', 3)],
            "Mari": [('füüsika', 4)]
        }
    ))  # -> {'füüsika': 3.5, 'keemia': 3.0}
    print()

    print("music_notes:")
    print(music_notes(["A", "B", "C"], {}))  # -> ["A", "B", "C"]
    print(music_notes(
        [],
        {
            "C": ["C", "E", "G"],
            "Am": ["A", "C", "E"],
        }
    ))  # -> []
    print(music_notes(
        ["C", "Am"],
        {
            "C": ["C", "E", "G"],
            "Am": ["A", "C", "E"],
        }
    ))  # -> ["C", "E", "G", "A", "C", "E"]
    print()

    print("count_neighbors:")
    grid = (
        (False, False, True),
        (False, True, True),
        (True, False, True),
    )
    print(count_neighbors(grid))
    # [
    #     [0, 0, 2],
    #     [0, 4, 3],
    #     [1, 0, 2],
    # ]
    print()

    print("Zoo:")
    zoo = Zoo()
    lion = Animal("leo", "lion", 3)
    platypus = Animal("perry", "platypus", 5)
    print(lion)  # => "Leo the Lion (3 years old)"
    try:
        zoo.add_animal(lion)
        zoo.add_animal(platypus)
        zoo.assign_to_cage(lion, 1)
        zoo.assign_to_cage(platypus, 2)

        print(zoo.animals)  # => [Leo the Lion (3 years old), Perry the Platypus (5 years old)]
        print(zoo.find_animals_by_species("crocodile"))  # => []
        print(zoo.find_animals_by_species("platypus"))  # => [Perry the Platypus (5 years old)]
        print(zoo.get_animals_sorted_by_name())  # => [Leo the Lion (3 years old), Perry the Platypus (5 years old)]
        print(zoo.cages)  # {1: [Leo the Lion (3 years old)], 2: [Perry the Platypus (5 years old)]}

        zoo.remove_animal(lion)
        print(zoo.animals)  # => [Perry the Platypus (5 years old)]
        print(zoo.cages)  # => {2: [Perry the Platypus (5 years old)]}
    except NameError:
        print("Zoo is missing required fields (animals, cages)")
    print()

    print("University:")
    mari = Student("Mari Maa")
    jyri = Student("Jyri Jogi")
    teele = Student("Teele Tee")
    cl = Class("Anna", [mari, jyri, teele])
    mari.grade(Grade(5, 3, "KT", "01/09/2020"))
    gr = Grade("!", 3, "KT", "01/09/2020")
    jyri.grade(gr)
    teele.grade(Grade(4, 3, "KT", "01/09/2020"))

    print(f"Jyri keskmine hinne on {jyri.calculate_weighted_average()}.")  # 1

    jyri.redo_assignment(3, "KT", "14/09/2020")
    print(len(gr.previous_grades))  # 1

    print(f"Jyri keskmine hinne on nyyd {jyri.calculate_weighted_average()}.")  # 3
    print()

    mari.grade(Grade(5, 1, "TK", "30/11/2020"))
    jyri.grade(Grade(4, 1, "TK", "30/11/2020"))
    teele.grade(Grade(3, 1, "TK", "30/11/2020"))

    print(f"Teele keskmine hinne on {teele.calculate_weighted_average()}.")  # 4
    print(cl.get_grade_sheet())
    print()

    tuuli = Student("Tuuli Karu")
    cl.add_student(tuuli)
    print(len(cl.students))  # 4
    print()
