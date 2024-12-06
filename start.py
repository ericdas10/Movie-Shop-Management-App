from domain.entitati import Movie, Client
from domain.validatori import ClientVal,MovieVal
from repository.Movie_repo import MovieInFileRepo, MovieRepository
from repository.Client_repo import ClientiRepository, ClientinFileRepo
from repository.rent_repo import RentRepository
from service.movieservice import MovieService
from service.clientservice import ClientService
from service.rentservice import RentService
from console.ui import consola

Film = MovieService(MovieInFileRepo("data/filme.txt"),MovieVal())
Customer = ClientService(ClientinFileRepo("data/clienti.txt"),ClientVal())
Rent = RentService(RentRepository())

ui = consola(Film,Customer,Rent)

ui.show_ui()
