from siniflar.queryexecuter import execute_query

class Randevu:
    def __init__(self, randevu_tarihi, randevu_saati, hasta_id, doktor_id):
        self.randevu_tarihi = randevu_tarihi
        self.randevu_saati = randevu_saati
        self.hasta_id = hasta_id
        self.doktor_id = doktor_id

    def insert_randevu(self):
        # SQL sorgusu
        sql = "INSERT INTO randevular (RandevuTarihi, RandevuSaati, HastaID, DoktorID) VALUES (%s, %s, %s, %s)"
        val = (self.randevu_tarihi, self.randevu_saati, self.hasta_id, self.doktor_id)
        execute_query(sql, val)

    def update_randevu(self, randevu_id):
        # SQL sorgusu
        sql = "UPDATE randevular SET RandevuTarihi = %s, RandevuSaati = %s, HastaID = %s, DoktorID = %s WHERE RandevuID = %s"
        val = (self.randevu_tarihi, self.randevu_saati, self.hasta_id, self.doktor_id, randevu_id)
        execute_query(sql, val)

    @staticmethod
    def delete_randevu(randevu_id):
        # SQL sorgusu
        sql = "DELETE FROM randevular WHERE RandevuID = %s"
        val = (randevu_id,)
        execute_query(sql, val)