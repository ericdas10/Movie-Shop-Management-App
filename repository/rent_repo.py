class RentRepository:
    def __init__(self):

        self.__rents = []

    def add_rent(self, id1, id2):

        self.__rents.append((id1, id2))

    def del_rent(self, id1, id2):
        """Complexitate:
        Caz favorabil: T(n) apartine O(1)
        Caz defavorabil: T(n) apartine O(n)
        Caz mediu: T(n) apartine O(n/2)
        """

        index  = 0
        ok = True
        for index in range(len(self.__rents)):
            if self.__rents[index][0] == id1 and self.__rents[index][1] == id2:
                self.__rents.pop(index)
                ok = False
                break

        if ok:
            raise ValueError("Nu a fost gasita inchirierea")
        
    def get_list(self):

        nr_rent = [0] * 100
        for id1, id2 in self.__rents:
            nr_rent[id1] += 1

        return nr_rent
    
    def get_max_rent(self):
        nr_rent = [0] * 100
        maxi = 0
        idmax = 0
        for id1, id2 in self.__rents:
            nr_rent[id2] += 1
            if nr_rent[id2] > maxi:
                maxi = nr_rent[id2]
                idmax = id2

        lista = []
        for id1, id2 in self.__rents:
            if id2 == idmax:
                lista.append(id1)

        return lista

    def get_all_id(self, id):
        """
        Functia cauta toate filmele inchiriate de un client
        :param id: id-ul clientului
        """
        filme=[]
        for id1, id2 in self.__rents:
            if id1 == id:
                filme.append(id2)
        return filme
    
    def get_all_id2(self,id):
        """
        Functia returneaza toti clientii care au inchiriat un film
        :param id: id-ul clientului
        :return: lista
        """
        cumparatori=[]
        for id1, id2 in self.__rents:
            if id2 == id:
                cumparatori.append(id1)
        return cumparatori
    
    def return_all_rents(self):

        return self.__rents