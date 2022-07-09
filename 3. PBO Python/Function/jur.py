class jurusan:

    def __init__(self, prodi, kajur, jml_siswa):
        self.prodi = prodi
        self.kajur = kajur
        self.jml_siswa = jml_siswa

    def akreditasi(self):
        if self.jml_siswa >= 80:
            return True
        else:
            return False