from http import client
import unittest

from domain.entitati import Client, Movie

class TestFilm(unittest.TestCase):
    def test_creare_film(self):
        film = Movie(1, "Fight Club", "Film jmek", "Drama")
        self.assertEqual(film.get_id(), 1)
        self.assertEqual(film.get_titlu(), "Fight Club")
        self.assertEqual(film.get_desc(), "Film jmek")
        self.assertEqual(film.get_gen(), "Drama")
        
    def test_eq_film(self):
        film1 = Movie(1, "Fight Club", "Film jmek", "Drama")
        film2 = Movie(1, "Fight Club", "Film jmek", "Drama")
        
        self.assertEqual(film1, film2)
        
        film3 = Movie(1, "Fight Club", "Film jmek", "Drama")
        
        self.assertEqual(film1, film3)
        
    
class TestClient(unittest.TestCase):
    def test_creare_client(self):
        client = Client(1, "Dan", "5081230441657")
        self.assertEqual(client.get_id(), 1)
        self.assertEqual(client.get_nume, "Dan")
        self.assertEqual(client.get_cnp, "5081230441657")
        
        client.set_nume("Geanny")
        client.set_cnp("5011129678912")
        
        self.assertEqual(client.get_nume, "Geanny")
        self.assertEqual(client.get_cnp, "5011129678912")
        
    def test_eq_client(self):
        client1 = Client(1, "Dan", "5081230441657")
        client2 = Client(1, "Dan", "5081230441657")
        
        self.assertEqual(client1, client2)
        
        