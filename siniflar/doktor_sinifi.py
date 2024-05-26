from siniflar.queryexecuter import execute_query


class Doktor:
    def __init__(self, ad, soyad, uzmanlik_alani, calistigi_hastane, doktorun, doktorsifre):
        self.ad = ad
        self.soyad = soyad
        self.uzmanlik_alani = uzmanlik_alani
        self.calistigi_hastane = calistigi_hastane
        self.doktorun = doktorun
        self.doktorsifre = doktorsifre

    def insert_doktor(self):
        # SQL sorgusu
        sql = "INSERT INTO doktorlar (Ad, Soyad, UzmanlikAlani, CalistigiHastane, doktorun, doktorsifre) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.ad, self.soyad, self.uzmanlik_alani, self.calistigi_hastane, self.doktorun, self.doktorsifre)
        execute_query(sql, val)

    def update_doktor(self, doktor_id):
        # SQL sorgusu
        sql = "UPDATE doktorlar SET Ad = %s, Soyad = %s, UzmanlikAlani = %s, CalistigiHastane = %s, doktorun = %s, doktorsifre = %s WHERE DoktorID = %s"
        val = (self.ad, self.soyad, self.uzmanlik_alani, self.calistigi_hastane, self.doktorun, self.doktorsifre, doktor_id)
        execute_query(sql, val)

    @staticmethod
    def delete_doktor(doktor_id):
        # SQL sorgusu
        sql = "DELETE FROM doktorlar WHERE DoktorID = %s"
        val = (doktor_id,)
        execute_query(sql, val)