class CounselingSession:
    def __init__(self, id_session, survivor, counselor, date_time):
        self._id = id_session
        self._survivor = survivor       # Objek Survivor
        self._counselor = counselor     # Objek Counselor
        self._date_time = date_time     # Tanggal/Jam (String)
        self._notes = ""                # Catatan sesi (kosong dulu)

    # Getters
    def get_id(self):
        return self._id

    def get_details(self):
        return f"Sesi #{self._id}: {self._survivor.get_name()} bersama {self._counselor.get_name()} pada {self._date_time}"

    def set_notes(self, notes):
        self._notes = notes