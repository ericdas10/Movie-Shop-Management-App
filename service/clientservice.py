from http import client
from domain.entitati import Client
from utilitati.util import number_string_generator, string_generator


class ClientService():

    def __init__(self, repo, validator):

        self.__repo = repo
        self.__validator = validator

    def insert_client(self, id, nume, cnp):

        cumparator = Client(id, nume, cnp)
        self.__validator.validate(cumparator)
        self.__repo.add_client(cumparator)
        return cumparator
    
    def del_client(self, id):
        
        self.__repo.del_client(id)
        
    def mod_client(self, id, nume, cnp):
        
        cumparator = Client(id, nume, cnp)
        self.__validator.validate(cumparator)
        self.__repo.mod_client(id, nume, cnp)
        return cumparator
    
    def search_by_id(self, id):
        
        clt = self.__repo.search_by_id_cl(id)
        return clt
    
    def search_by_prm(self, nume, cnp):
        
        clt = self.__repo.search_by_par_cl(nume, cnp)
        return clt
    
    def search_id(self, id):
        
        self.__repo.search_ID(id)

    def add_random_clients(self, numar):

        for index in range(numar):
            elem = Client(1, string_generator(7), number_string_generator(13))
            self.__validator.validate(elem)
            self.__repo.add_client(elem)
        
    def return_all(self):
        
        return self.__repo.return_all_cl()

        