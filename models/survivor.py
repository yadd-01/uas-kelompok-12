from models.user import User  # Kita import induknya dulu

class Survivor(User):
    def __init__(self, id_user, name, trauma_type, mental_status):
        #Panggil konstruktor induk (User) pakainya super()
        super().__init__(id_user, name)
        
        self._trauma_type = str(trauma_type)
        self._mental_status = str(mental_status)

    def get_trauma_type(self):
        return self._trauma_type

    def get_mental_status(self):
        return self._mental_status