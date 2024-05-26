
from siniflar import queryexecuter


from siniflar.queryexecuter import execute_query


class Yonetici:
    def __init__(self, ad, soyad, yoneticiun, yoneticisifre):
        self.ad = ad
        self.soyad = soyad
        self.yoneticiun = yoneticiun
        self.yoneticisifre = yoneticisifre

    def insert_yonetici(self):
        # SQL sorgusu
        sql = "INSERT INTO yonetici (Ad, Soyad, yoneticiun, yoneticisifre) VALUES (%s, %s, %s, %s)"
        val = (self.ad, self.soyad, self.yoneticiun, self.yoneticisifre)
        execute_query(sql, val)

    def update_yonetici(self, yonetici_id):
        # SQL sorgusu
        sql = "UPDATE yonetici SET Ad = %s, Soyad = %s, yoneticiun = %s, yoneticisifre = %s WHERE YoneticiID = %s"
        val = (self.ad, self.soyad, self.yoneticiun, self.yoneticisifre, yonetici_id)
        execute_query(sql, val)

    @staticmethod
    def delete_yonetici(yonetici_id):
        # SQL sorgusu
        sql = "DELETE FROM yonetici WHERE YoneticiID = %s"
        val = (yonetici_id,)
        execute_query(sql, val)