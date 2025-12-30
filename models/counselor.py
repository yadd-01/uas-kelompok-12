# Simpan dengan nama file: counselor.py
from models.user import User

class Counselor(User):
    def __init__(self, id_user, name, expertise, location):
        #Panggil konstruktor induk
        super().__init__(id_user, name)
        
        self._expertise = str(expertise)
        self._location = str(location)

    def get_expertise(self):
        return self._expertise

    def get_location(self):
        return self._location