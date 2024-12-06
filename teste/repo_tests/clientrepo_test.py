from os import unlink
import unittest

from domain.entitati import Client
from repository.Client_repo import ClientiRepository

class TestClientRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = ClientiRepository()
        self.__repo1 = ClientiRepository()
        self.__repo2 = ClientiRepository()
        self.__repo3 = ClientiRepository()
        self.__new_repo = ClientiRepository()

    def test_eq(self):
        client = Client(1, "Dan", "5080724541217")
        client1 = Client(1, "Dan", "5080724541217")

        self.__repo1.add_client(client)
        self.__repo2.add_client(client)
        self.assertEqual(self.__repo1, self.__repo2)
        self.__repo3.add_client(client1)
        self.assertEqual(self.__repo1, self.__repo3)
        self.assertRaises(ValueError, self.__repo3.search_ID, 5)

    def test_add_client(self):
        client = Client(1, "Dan", "5080724541217")

        self.__repo.add_client(client)
        self.assertEqual(len(self.__repo.return_all_cl()), 1)

    def test_delete_client(self):
        client = Client(1, "Dan", "5080724541217")

        self.__repo.add_client(client)
        self.__repo.del_client(1)
        self.assertEqual(len(self.__repo.return_all_cl()), 0)

    def test_mod_client(self):
        client = Client(1, "Dan", "5080724541217")

        self.__repo.add_client(client)
        self.__repo.mod_client(1, "Dan Bilzerian", "5020421314002")

    def test_ret_all_clts(self):
        client = Client(1, "Dan", "5080724541217")

        self.__repo.add_client(client)
        self.assertEqual(self.__repo.return_all_cl(), [client])

    def test_search_client_by_id(self):
        customer1=Client(1,"Georgescu Valentin","5020421314002")
        customer2=Client(2,"Nicolae Guta","5020421314002")

        self.__repo.add_client(customer1)
        self.__repo.add_client(customer2)

        self.assertEqual(self.__repo.search_by_id_cl(1),customer1)
        self.assertEqual(self.__repo.search_by_id_cl(2),customer2)

    def test_search_client_by_param(self):
        customer1=Client(1,"Georgescu Valentin","5020421314002")
        customer2=Client(2,"Nicolae Guta","5020421314002")

        self.__repo.add_client(customer1)
        self.__repo.add_client(customer2)

        self.assertEqual(self.__repo.search_by_par_cl("Nicolae Guta",""),customer2)
        self.assertEqual(self.__repo.search_by_par_cl("","5020421314002"),customer1)

