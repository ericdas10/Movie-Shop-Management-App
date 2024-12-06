from service.movieservice import MovieService
from service.clientservice import ClientService
from service.rentservice import RentService
from utilitati.util import merge_sort



def cmp_name(elem):
    
    return elem[0]

def cmp_movie(elem):

    return elem[1]

class consola:
    
    def __init__(self, svc, svc1, svc2):
        
        self.__svc = svc
        self.__svc1 = svc1
        self.__svc2 = svc2
        consola.id = 1
        consola.id1 = 1
        
    #zona pentru filme
    
    def adauga_film(self):
        
        nume = input("Introduceti numele filmului:")
        desc = input("Introduceti descrierea filmului:")
        gen = input("Introduceti genul filmului:")
        
        try:
            film = self.__svc.insert_movie(consola.id, nume, desc, gen)
            print("Filmul a fost adaugat cu succes la id_ul " + str(consola.id))
            consola.id += 1
        except ValueError as ve:
            print(ve)

    def stergere_film(self):
        try:
            id_m = int(input("Introdu id ul filmului de sters:"))
            if id_m > consola.id:
                raise ValueError("Id invalid")
            self.__svc.del_movie(id_m)
            print("Film sters cu succes")
        except ValueError as ve:
            print(ve)

    def modifica_film(self):

        try:
            id_m = int(input("Introdu id ul filmului de sters:"))
            if id_m > consola.id:
                raise ValueError("Id invalid")
            nume = input("Introduceti numele filmului:")
            desc = input("Introduceti descrierea filmului:")
            gen = input("Introduceti genul filmului:")
            self.__svc.mod_movie(id_m, nume, desc, gen)
            print("Film modificat cu succes")

        except ValueError as ve:
            print(ve)

    def cautare_dupa_id(self):

        try:
            id = int(input("Id de cautat:"))
            film = self.__svc.search_by_id(id)
            return film
        except ValueError as ve:
            print(ve)


    def cautare_dupa_parametru(self):

        try:
            titlu = desc = gen = ""
            titlu = input("Introduceti titlul:")
            desc = input("Introduceti descrierea:")
            gen = input("Introduceti genul:")
            film = self.__svc.search_by_param(titlu, desc, gen)
            return film
        except ValueError as ve:
            print(ve)

    def random_film(self):
        try:
            numar = int(input("Introdu un numar de filme:"))
            self.__svc.add_random_movie(numar)
            consola.id += numar
            print("Au fost adaugate "+str(numar)+" filme")
        except:
            raise ValueError("Obtiunea a esuat")

    def printeaza_filme(self):
        for el in self.__svc.return_all():
            print(el)

    #zona pt clienti

    def adaugare_client(self):

        nume =input("Introdu numele:")
        cnp = input("Introdu CNP:")
        try:
            self.__svc1.insert_client(consola.id1, nume, cnp)
            consola.id1 += 1
            print("Clientul a fost adaugat cu succesc cu id-ul "+str(consola.id1))
        except ValueError as ve:
            print(ve)

    def stergere_client(self):

        try:
            id_m = int(input("Introdu id-ul clientului de sters:"))
            if id_m > consola.id1:
                raise ValueError("Id-ul nu este valid")
            self.__svc1.del_client(id_m)
            print("Client sters cu succes")
        except ValueError as ve:
            print(ve)

    def modificare_client(self):

        try:
            id_m = int(input("Introduceti id-ul clientului de modificat: "))
            if id_m > consola.id1:
                raise ValueError("Id-ul nu este valid")
            nume = input("Introduceti noul nume:")
            cnp = input("Introduceti noul CNP:")
            self.__svc1.mod_client(id_m, nume, cnp)
            print("Client modificat cu succes")
        except ValueError as ve:
            print(ve)

    def cautare_dupa_id_client(self):

        try:
            id = int(input("Introduceti id-ul de cautare:"))
            client = self.__svc1.search_by_id(id)
            return client
        except ValueError as ve:
            print(ve)

    def cautare_dupa_parametru_client(self):

        try:
            nume = cnp = ""
            nume = input("Introduceti numele: ")
            cnp = input("Introduceti CNP-ul: ")
            client = self.__svc1.search_by_prm(nume, cnp)
            return client
        except ValueError as ve:
            print(ve)

    def random_client(self):
        try:
            numar = int(input("Introdu un numar de clienti:"))
            self.__svc1.add_random_clients(numar)
            consola.id1 += numar
            print("Au fost adaugati "+str(numar)+" clienti")
        except:
            raise ValueError("Obtiunea a esuat")

    def afisare(self):
        
        return self.__svc1.return_all()

    def printeaza_clienti(self):
        for el in self.__svc1.return_all():
            print(el)
    
    
    # zona pentru inchiorieri

    def inchirieri(self):
        try:
            id1 = int(input("Introduceti id-ul clientului: "))
            self.__svc1.search_id(id1)
            cumparator = self.__svc1.search_by_id(id1)
            print("Bine ai venit, "+str(cumparator.get_nume()))
            print("Acestea sunt filmele disponibile:")
            for elem in self.__svc.return_all():
                print(elem)
            id2 = int(input("Introduceti id-ul filmului: "))
            self.__svc.search_id(id2)
            self.__svc2.add_rent_op(id1, id2)
            print("Filmul a fost inchiriat cu succes")
        except ValueError as ve:
            print(ve)

    def returnare(self):
        try:
            id1 = int(input("Introduceti id-ul clientului: "))
            self.__svc1.search_id(id1)
            cumparator = self.__svc1.search_by_id(id1)
            print("Bine ai venit, "+str(cumparator.get_nume()))
            print("Acestea sunt filmele inchiriate de dvs:")
            filme = self.__svc2.get_all_for_id(id1)
            for elem in filme:
                film = self.__svc.search_by_id(elem)
                print(film)
            id2 = int(input("Introduceti id-ul filmului de returnat: "))
            self.__svc.search_id(id2)
            self.__svc2.remove_rent_op(id1,id2)
            print("Filmul a fost returnat cu succes")
        except ValueError as ve:
            print(ve)
            
    
    #zona rapoarte
    
    def raport_clienti_nr(self):
        """
        Genereaza raportul clienti cu filme inchiriate, ordonat dupa nume
        """
        lista_clienti = []
        frecventa_cmp = self.__svc2.get_list_with_id()
        for index in range(len(frecventa_cmp)):
            if frecventa_cmp[index] != 0:
                cumparator = self.__svc1.search_by_id(index)
                lista_clienti.append([cumparator.get_nume(), frecventa_cmp[index]])
                
        lista_clienti.sort(key = cmp_name)
        for elem in lista_clienti:
            print("Nume ")
            print(elem[0])
            print("filme inchiriate: ")
            print(elem[1])
            
    def raport_filem_nr(self):
        """
        Genereaza raportul clienti cu filme inchiriate, ordonat dupa nr de filme inchiriate crescator
        """
        lista_clienti = []
        frecventa_cmp = self.__svc2.get_list_with_id()
        for index in range(len(frecventa_cmp)):
            if frecventa_cmp[index] != 0:
                cumparator = self.__svc1.search_by_id(index)
                lista_clienti.append([cumparator.get_nume(), frecventa_cmp[index]])
                
        lista_clienti.sort(key = cmp_movie)
        for elem in  lista_clienti:
            print("Nume ")
            print(elem[0])
            print("filme inchiriate: ")
            print(elem[1])
            
    def raport_spec(self):
        """
        Genereaza cel/cele mai inchiriat(e) film(e)
        """
        cumparatori = self.__svc2.get_list_with_idmax()
        
        frecventa_cmp = self.__svc2.get_list_with_id()
        
        lista_clienti = []
        for elem in cumparatori:
            cumparator = self.__svc1.search_by_id(elem)
            lista_clienti.append([cumparator.get_nume(), frecventa_cmp[elem]])
            
        for elem in lista_clienti:
            print("Nume ")
            print(elem[0])
            print("filme inchiriate: ")
            print(elem[1])
            
    def raport_30(self):
        """
        Genereaza raportul clienti cu filme inchiriate, ordonat dupa nr de filme inchiriate descrescator,primii 30%
        """
        
        lista_clienti = []
        frecventa_cmp = self.__svc2.get_list_with_id()
        for index in range(len(frecventa_cmp)):
            if frecventa_cmp[index] != 0:
                cumparator = self.__svc1.search_by_id(index)
                lista_clienti.append([cumparator.get_nume(), frecventa_cmp[index]])
                
        index = len(self.__svc1.return_all())
        index *= 3
        index //= 10
        ix = 0
        merge_sort(lista_clienti, keys = [cmp_movie, cmp_name], key_orders= [False, True])
        for elem in lista_clienti:
            if ix > index:
                break
            else:
                ix += 1
            print("Nume ")
            print(elem[0])
            print("filme inchiriate: ")
            print(elem[1])
            
        
        
    def show_ui(self):

        end = False
        while not(end):
            print("Comenzi disponbibile: film_nou, random_film, client_nou, random_client, sterge_film, sterge_client, modifica_film, modifica_client, printeaza_filme, printeaza_client, exit")
            print("Comenzi inchirieri: cauta_film, cauta_client, inchiriaza_film, returneaza_film")
            print("Comenzi rapoarte: ")
            print("1.Raport clienți cu filme închiriate ordonat dupa nume = raport_filme_nume")
            print("2.Raport clienți cu filme închiriate ordonat dupa numărul de filme închiriate = raport_filme_nr")
            print("3.Raport primii 30% clienți cu cele mai multe filme = raport_30")
            print("4.Raport cel(e) mai inchiriat(e) film(e) = raport_special")
            
            command=input("Comanda este: ")
            command.lower().strip()
            if command=="film_nou":
                self.adauga_film()
            elif command=="random_film":
                self.random_film()
            elif command=="random_client":
                self.random_client()
            elif command=="sterge_film":
                self.stergere_film()
            elif command=="printeaza_filme":
                self.printeaza_filme()
            elif command=="printeaza_client":
                self.printeaza_clienti()
            elif command=="modifica_film":
                self.modifica_film()
            elif command=="client_nou":
                self.adaugare_client()
            elif command=="sterge_client":
                self.stergere_client()
            elif command=="modifica_client":
                self.modificare_client()
            elif command=="cauta_film":
                print("Comenzi disponibile cautare: id, descriere")
                secondary_command=input("Introduceti comanada: ")
                if secondary_command=="id":
                    movie=self.cautare_dupa_id()
                    print(movie)
                elif secondary_command=="descriere":
                    movie=self.cautare_dupa_parametru()
                    print(movie)
                else:
                    print("Comanda invalida")
            elif command=="cauta_client":
                print("Comenzi disponibile cautare: id, descriere")
                secondary_command=input("Introduceti comanada: ")
                if secondary_command=="id":
                    customer=self.cautare_dupa_id_client()
                    print(customer)
                elif secondary_command=="descriere":
                    customer=self.cautare_dupa_parametru_client()
                    print(customer)
                else:
                    print("Comanda invalida")
            elif command=="inchiriaza_film":
                self.inchirieri()
            elif command=="returneaza_film":
                self.returnare()
            elif command=="raport_filme_nume":
                self.raport_clienti_nr()
            elif command=="raport_filme_nr":
                self.raport_filem_nr()
            elif command=="raport_30":
                self.raport_30()
            elif command=="raport_special":
                self.raport_spec()
            elif command=="exit":
                end=True
            else:
                print("Comanda invalida")


            