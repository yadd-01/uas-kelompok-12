class User:
    def __init__(self, id_user, name):
        # Tanda _ (underscore) berarti private/protected
        self._id = int(id_user)
        self._name = str(name)
        self._is_active = True

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
        
    def is_active(self):
        return self._is_active