from siniflar import doktor_sinifi
from siniflar.doktor_sinifi import Doktor
from siniflar.yonetici_sinifi import Yonetici

doktor = Doktor("ad", "soyad", "uzmanlik", "hastane", "kullanıcı", "şifre")
Yonetici.delete_yonetici(10)