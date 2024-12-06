from domain.entitati import Movie
from utilitati.util import string_generator


class MovieService:
    
    def __init__(self, repo, validator):
        
        self.__repo = repo
        self.__validator = validator
        
    def insert_movie(self, id, titlu, desc, gen):
        
        film = Movie(id, titlu, desc, gen)
        self.__validator.validate(film)
        self.__repo.add_movie(film)
        return film
    
    def del_movie(self, id):
        
        self.__repo.del_movie(id)
        
    def mod_movie(self, id, titlu, desc, gen):
        
        film = Movie(id, titlu, desc, gen)
        self.__validator.validate(film)
        self.__repo.mod_movie(id, titlu, desc, gen)
        return film
        
    def search_by_id(self, id):
        
        film = self.__repo.search_by_id(id)
        return film
    
    def search_by_param(self, titlu, desc, gen):
        
        film = self.__repo.search_by_par(titlu, desc, gen)
        return film
    
    def search_id(self, id):
        
        self.__repo.search_ID(id)

    def add_random_movie(self, numar):

        for index in range(numar):
            film = Movie(1, string_generator(6), string_generator(20), string_generator(6))
            self.__validator.validate(film)
            self.__repo.add_movie(film)
        
    def return_all(self):
        
        return self.__repo.return_all_movies()