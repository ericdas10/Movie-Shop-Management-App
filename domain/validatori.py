class MovieVal:
    def validate(self, film):
        eroare = []
        if film.get_titlu() == "":
            eroare.append("Titlul indisponibil")

        if film.get_gen() == "":
            eroare.append("Gen indisponibil")

        if film.get_desc() == "":
            eroare.append("Descriere indisponibila")

        if len(film.get_desc()) > 5000:
            eroare.append("Lungimea descrierii este prea mare")

        if len(film.get_gen()) > 50:
            eroare.append("Lungimea genului este prea mare")
        
        if len(eroare) > 0:
            eroare_str = '\n'.join(eroare)
            raise ValueError(eroare_str)


class ClientVal:
    def validate(self, cumparator):
        eroare = []
        if cumparator.get_nume() == "":
            eroare.append("Nume inexistent")

        if cumparator.get_cnp() == "":
            eroare.append("CNP inexistent")

        try:
            value = int(cumparator.get_cnp())
        except:
            eroare.append("CNP-ul trebuie sa fie format doar din cifre")
            value=0
        CNP=[]
        while value != 0:
            CNP.append(value % 10)
            value //= 10

        if len(CNP)>13:
            msg="Lungime invalida "+str(len(CNP))
            eroare.append(msg)


        if len(eroare) > 0:
            eroare_str = '\n'.join(eroare)
            raise ValueError(eroare_str)

        