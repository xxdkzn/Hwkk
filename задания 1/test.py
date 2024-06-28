import unittest
from parameterized import parameterized

def race_between_hare_and_turtle(hare_distances, turtle_distances):
    hare_all = sum(hare_distances)
    turtle_all = sum(turtle_distances)

    if hare_all > turtle_all:
        return "заяц"
    elif hare_all < turtle_all:
        return "черепаха"
    else:
        return "одинаково"

def find_contest_winners(receipts):
    result = receipts[2::3]
    return result, len(result)

def match_people(boys, girls):
    if len(boys) == len(girls):
        pairs = ", ".join([f"{boy} и {girl}" for boy, girl in zip(sorted(boys), sorted(girls))])
        return pairs
    else:
        return "Кто-то может остаться без пары!"

class TestPythonBasics(unittest.TestCase):
    # Задача 1: Гонка между зайцем и черепахой
    @parameterized.expand([
        ([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], "заяц"),
        ([5, 3, 1, 2, 1, 0, 0], [3, 3, 3, 3, 3, 3, 3], "черепаха"),
        ([5, 3, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], "одинаково")
    ])
    def test_race_between_hare_and_turtle(self, hare_distances, turtle_distances, expected_output):
        result = race_between_hare_and_turtle(hare_distances, turtle_distances)
        self.assertEqual(result, expected_output)

    # Задача 2: Конкурс в магазине "Шестёрочка"
    @parameterized.expand([
        ([123, 145, 346, 246, 235, 166, 112, 351, 436], [246, 351, 436]),
        ([246, 351, 123, 145, 346, 235, 166, 112, 436], [246, 351, 436]),
        ([123, 145, 346, 246, 235, 166, 112], []),
    ])
    def test_find_contest_winners(self, receipts, expected_output):
        result = find_contest_winners(receipts)
        self.assertEqual(sorted(result), sorted(expected_output))

    # Задача 3: MVP dating-сервиса
    @parameterized.expand([
        (['Peter', 'Alex', 'John', 'Arthur', 'Richard'], ['Kate', 'Olivia', 'Emma', 'Charlotte', 'Sophia'], 'Peter и Kate, Alex и Olivia, John и Emma, Arthur и Charlotte, Richard и Sophia'),
        (['John', 'Peter', 'Alex'], ['Kate', 'Olivia', 'Emma'], 'John и Kate, Peter и Olivia, Alex и Emma'),
        (['John', 'Peter', 'Alex'], ['Kate', 'Olivia'], 'Кто-то может остаться без пары!')
    ])
    def test_match_people(self, boys, girls, expected_output):
        result = match_people(boys, girls)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()