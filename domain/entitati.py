class Movie:
    def __init__(self, id, titlu, desc, gen):

        self.__id = id
        self.__titlu = titlu
        self.__desc = desc
        self.__gen = gen

    def get_id(self):
        return self.__id
    
    def get_titlu(self):
        return self.__titlu
    
    def get_desc(self):
        return self.__desc
    
    def get_gen(self):
        return self.__gen
    
    
    def set_titlu(self, value):
        self.__titlu = value
    
    def set_desc(self, value):
        self.__desc = value
    
    def set_gen(self, value):
        self.__gen = value

    
    def __repr__(self):
        return f"Filmul: {self.__id}, Nume: {self.__titlu}, Descriere: {self.__desc}, Gen: {self.__gen}"
    

    def __eq__(self, value):
        return self.__titlu == value.__titlu and self.__gen == value.__gen and self.__desc == value.__desc
    


class Client:
    
    def __init__(self, id, nume, cnp):
        self.__id = id
        self.__nume = nume
        self.__cnp = cnp

    
    def get_id(self):
        return self.__id
    
    def get_nume(self):
        return self.__nume
    
    def get_cnp(self):
        return self.__cnp


    def set_id(self, value):
        self.__id = value
    
    def set_nume(self, value):
        self.__nume = value
    
    def set_cnp(self, value):
        self.__cnp = value 


    def __repr__(self):
        return f"Clientul: {self.__id}, Nume: {self.__nume}, CNP: {self.__cnp}"
    

    def __eq__(self, value):
        return self.__nume == value.__nume and self.__cnp == value.__cnp