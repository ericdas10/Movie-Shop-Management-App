from domain.entitati import Movie


def search_movie(lista, id, index):
    if index < 0:
        raise ValueError("Id-ul nu a fost gasit")
    if lista[index - 1].get_id() == id:
        return lista[index - 1]
    
    return search_movie(lista, id, index - 1)

"""def search_movie(lista, id):
    for index in len(lista):
        if lista[index].get_id() == id:
            return lista[index]"""

class MovieRepository:

    def __init__(self):
        self.__filme = []
        MovieRepository.id = 1

    
    def add_movie(self, new_movie):
        film = Movie(MovieRepository.id, new_movie.get_titlu(), new_movie.get_desc(), new_movie.get_gen())
        MovieRepository.id += 1
        self.__filme.append(film)


    def del_movie(self, id):
        filme_noi = []
        for film in self.__filme:
            if film.get_id() != id:
                filme_noi.append(film)
        self.__filme = filme_noi

    def mod_movie(self, id, titlu_nou, desc_nou, gen_nou):
        filme_noi = []
        for film in self.__filme:
            if film.get_id() == id:
                film.set_titlu(titlu_nou)
                film.set_desc(desc_nou)
                film.set_gen(gen_nou)
            filme_noi.append(film)
        
        self.__filme = filme_noi

    def search_by_id(self, id):
        return search_movie(self.__filme, id, len(self.__filme))
    
    def search_by_par(self, titlu, desc, gen):
        for film in self.__filme:
            if film.get_titlu() == titlu or film.get_desc() == desc or film.get_gen() == gen:
                    return film
            
        raise ValueError("Filmul nu a fost gasit")
    
    def search_ID(self, id):
        ok = True

        for el in self.__filme:
            if el.get_id() == id:
                ok = False
        
        if ok:
            raise ValueError("Id-ul nu apartine nici unui film")
        

    def return_all_movies(self):
        return self.__filme
    
    def __eq__(self, other):
        return self.__filme == other.__filme
    
class MovieInFileRepo(MovieRepository):

    def __init__(self, filename):
        """
        Constructorul clasei
        :param filename: numele fisierului
        """
        MovieRepository.__init__(self)
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Pune in repo-ul din memorie filmele din fisier
        """
        with open(self.__filename, "r") as f:
            lines=f.readlines()
            for line in lines:
                if line == '\n':
                    break
                movie_id, movie_titlu, movie_desc, movie_gen=[token.strip() for token in line.split(";")]
                film = Movie(movie_id, movie_titlu, movie_desc, movie_gen)
                MovieRepository.add_movie(self, film)

    def __save_to_file(self):
        """
        Salveaza in fisier date din in memory
        """
        with open(self.__filename,"w") as f:
            films = MovieRepository.return_all_movies(self)
            for film in films:
                str_movie = str(film.get_id())+";"+str(film.get_titlu())+";"+str(film.get_desc())+";"+str(film.get_gen())+"\n"
                f.write(str_movie)
    
    def add_movie(self, new_movie):
        MovieRepository.add_movie(self, new_movie)
        self.__save_to_file()

    def del_movie(self, id):
        MovieRepository.del_movie(self, id)
        self.__save_to_file()

    def mod_movie(self, id, titlu_nou, desc_nou, gen_nou):
        MovieRepository.mod_movie(self, id, titlu_nou, desc_nou, gen_nou)
        self.__save_to_file()

    def search_by_id(self, id):
        return MovieRepository.search_by_id(self, id)

    def search_by_par(self, titlu, desc, gen):
        return MovieRepository.search_by_par(self, titlu, desc, gen)
    
    def search_ID(self, id):
        return MovieRepository.search_ID(self, id)
    
    def return_all_movies(self):
        return MovieRepository.return_all_movies(self)
    
    def __eq__(self, other):
        return MovieRepository.__eq__(self, other)