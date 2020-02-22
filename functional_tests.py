from selenium import webdriver
import unittest

DEVELOPMENT_URL = "http://127.0.0.1:8000/"


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edyta dowiedziaa si o nowej wspaniaej aplikacji w postaci listy rzeczy do zrobienia
        # postanowila przejsc na ston gwnej applikacji
        self.browser.get(f'{DEVELOPMENT_URL}')

        # Zwróciła uwagę, że  tytuł strony i nagłówek zawierają słowo listy
        self.assertIn("Listy", self.browser.title)
        self.fail("Zakończenie testu!")

        # Od razu zostaje zachęcona, aby wpisać rzecz do zrobienia

        # W polu tekstowym wpisałą kupić pawie pióra

        # Po wciśnięciu klawisza Enter strona zostąła uaktualniona i wyświetla
        # 1: Kupić pawie pióra jako element listy rzeczy do zrobienia

        # Na stronie nadal znajduje się pole tekstowe zachęcające do podania kolejnego zadania
        # Edyta wpisałą "Użyć pawich piór do zrobienia przynęty

        # Strona została ponownie uaktualniona i teraz wyświetla dwa elementy na liście rzeczy do zrobienia

        # Usatysfakcjonowana kładzie się spać


if __name__ == "__main__":
    unittest.main()
