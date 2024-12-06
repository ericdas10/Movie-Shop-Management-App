import unittest

from domain.entitati import Movie, Client
from domain.validatori import MovieVal, ClientVal

class MVTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__valid = MovieVal()
        
    def test_film(self):
        film = Movie(1, "Fight Club", "Film jmek", "Drama")
        self.__valid.validate(film)
        
        film1 = Movie(1, "", "Film jmek", "Drama")
        self.assertRaises(ValueError, self.__valid.validate, film1)

        film2 = Movie(1, "Fight Club", "", "Drama")
        self.assertRaises(ValueError, self.__valid.validate, film2)

        film3 = Movie(1, "Fight Club", "Film jmek", "")
        self.assertRaises(ValueError, self.__valid.validate, film3)

class CVTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__valid = ClientVal()
        
    def test_client(self):
        customer = Client(1, "Georgescu Valentin", "5020421314002")
        self.__valid.validate(customer)

        customer1 = Client(1, "", "5020421314002")
        self.assertRaises(ValueError, self.__valid.validate, customer1)

        customer3 = Client(1, "Georgescu Valentin", "")
        self.assertRaises(ValueError, self.__valid.validate, customer3)