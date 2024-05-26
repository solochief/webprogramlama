from siniflar.queryexecuter import execute_query


class TibbiRapor:
    def __init__(self, rapor_tarihi, rapor_icerigi, hasta_id, doktor_id, yonetici_id, resim_url, json_rapor):
        self.rapor_tarihi = rapor_tarihi
        self.rapor_icerigi = rapor_icerigi
        self.hasta_id = hasta_id
        self.doktor_id = doktor_id
        self.yonetici_id = yonetici_id
        self.resim_url = resim_url
        self.json_rapor = json_rapor

    def insert_rapor(self):
        # SQL sorgusu
        sql = "INSERT INTO tibbiraporlar (RaporTarihi, RaporIcerigi, HastaID, DoktorID, YoneticiID, ResimURL, JsonRapor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (self.rapor_tarihi, self.rapor_icerigi, self.hasta_id, self.doktor_id, self.yonetici_id, self.resim_url, self.json_rapor)
        execute_query(sql, val)

    def update_rapor(self, rapor_id):
        # SQL sorgusu
        sql = "UPDATE tibbiraporlar SET RaporTarihi = %s, RaporIcerigi = %s, HastaID = %s, DoktorID = %s, YoneticiID = %s, ResimURL = %s, JsonRapor = %s WHERE RaporID = %s"
        val = (self.rapor_tarihi, self.rapor_icerigi, self.hasta_id, self.doktor_id, self.yonetici_id, self.resim_url, self.json_rapor, rapor_id)
        execute_query(sql, val)

    @staticmethod
    def delete_rapor(rapor_id):
        # SQL sorgusu
        sql = "DELETE FROM tibbiraporlar WHERE RaporID = %s"
        val = (rapor_id,)
        execute_query(sql, val)