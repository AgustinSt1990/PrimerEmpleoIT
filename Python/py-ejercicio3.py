from email.message import EmailMessage
from optparse import AmbiguousOptionError


class DatosContacto:
    column_labels = ['Nombre', "Apellido", "Edad", "Email", "Casado", "Con_hijos", "Lista_amigos", "Peliculas_vistas"]
    
    def __init__(self, fname:str, lname:str, age:int, email:str, married:bool, children:bool, friendList:list, watchedMovies:dict):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = email
        self.married = married
        self.children = children
        self.friendList = friendList
        self.watchedMovies = watchedMovies

    def __str__(self):
        value_list = [self.fname, self.lname, self.age, self.email, self.married, self.children, self.friendList, self.watchedMovies]
        return_str = ''
        for i, v in enumerate(value_list):
            return_str += f'{self.column_labels[i]}: {v}\n'
        return return_str


if __name__ == '__main__':
    fname = 'Agustin'
    lname = 'Stigliano'
    age = 32
    email = 'af.stigliano@gmail.com'
    married = False
    children = False
    friend_list = ['Chueco', 'Cabeza', 'Colo', 'Guido', 'Primo']
    watched_movies = {'0': 'El Padrino', '1': 'Casino'}

    data = DatosContacto(fname, lname, age, email, married, children, friend_list, watched_movies)

    print (data)
