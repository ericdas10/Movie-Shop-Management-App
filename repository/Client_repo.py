from domain.entitati import Client

def search_client(lista, id, index):
    if index < 0:
        raise ValueError("Clientul nu a fost gasit")
    
    if lista[index - 1].get_id() == id:
        return lista[index - 1]
    
    return search_client(lista, id, index - 1)

"""def search_client(lista, id):
    for index in len(lista):
        if lista[index].get_id() == id:
            return lista[index]"""

class ClientiRepository:
    def __init__(self):
        
        self.__clienti = []
        ClientiRepository.id = 1

    def add_client(self, client_nou):    
        cumparator = Client(ClientiRepository.id, client_nou.get_nume(), client_nou.get_cnp())
        ClientiRepository.id += 1
        self.__clienti.append(cumparator)

    def del_client(self, id):
        lista_noua = []
        for el in self.__clienti:
            if el.get_id() != id:
                lista_noua.append(el)
        self.__clienti = lista_noua

    def mod_client(self, id, nume_nou, cnp_nou):

        lista_noua = []
        for el in self.__clienti:
            if el.get_id() == id:
                el.set_nume(nume_nou)
                el.set_cnp(cnp_nou)
            lista_noua.append(el)
        
        self.__clienti = lista_noua

    def search_by_id_cl(self, id):
        return search_client(self.__clienti, id, len(self.__clienti))
    
    def search_by_par_cl(self, nume, cnp):

        for el in self.__clienti:
            if el.get_nume() == nume or el.get_cnp() == cnp:
                return el
            
        raise ValueError("Clientul nu a fost gasit")
    
    def search_ID(self, id):

        ok = 1
        for el in self.__clienti:
            if el.get_id() == id:
                ok = 0

        if ok:
            raise ValueError("Nu exista clientul cu id-ul respectiv")
        
    def return_all_cl(self):

        return self.__clienti
    
    def __eq__(self, other):
        if self.__clienti == other.__clienti:
            return True
        
        return False
    
    
class ClientinFileRepo(ClientiRepository):
    
    def __init__(self, filename):

        ClientiRepository.__init__(self)
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
                client_id, client_nume, client_cnp = [token.strip() for token in line.split(";")]
                client = Client(client_id, client_nume, client_cnp)
                ClientiRepository.add_client(self, client)

    def __save_to_file(self):
        with open(self.__filename,"w") as f:
            clienti = ClientiRepository.return_all_cl(self)
            for client in clienti:
                str_clienti = str(client.get_id())+";"+str(client.get_nume())+";"+str(client.get_cnp())+"\n"
                f.write(str_clienti)

    def add_client(self, client_nou):
        ClientiRepository.add_client(self, client_nou)
        self.__save_to_file()

    def del_client(self, id):
        ClientiRepository.del_client(self, id)
        self.__save_to_file()

    def mod_client(self, id, nume_nou, cnp_nou):
        ClientiRepository.mod_client(self, id, nume_nou, cnp_nou)
        self.__save_to_file()

    def search_by_id_cl(self, id):
        return ClientiRepository.search_by_id_cl(self, id)
    
    def search_by_par_cl(self, nume, cnp):
        return ClientiRepository.search_by_par_cl(self, nume, cnp)
    
    def search_ID(self, id):
        return ClientiRepository.search_ID(self, id)
    
    def return_all_cl(self):
        return ClientiRepository.return_all_cl(self)
    
    def __eq__(self, other):
        return ClientiRepository.__eq__(self, other)
    