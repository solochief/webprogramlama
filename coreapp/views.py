import json

import os
from MySQLdb.constants.FIELD_TYPE import SET
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from hospitalweb import settings
from django.http import JsonResponse
from datetime import datetime, timedelta



# Create your views here.

def index(request):
    return render(request, 'index.html')

def hakkimizda_view(request):
    return render(request, 'hakkimizda.html')

def iletisim_view(request):
    return render(request, 'iletisim.html')

def admin_rapor_view(request):
    return render(request, 'admin_rapor.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        account_type = request.POST.get('loginAccountType')

        if account_type == 'Yonetici':
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM yonetici WHERE yoneticiun = %s AND yoneticisifre = %s",
                               [username, password])
                row = cursor.fetchone()[0]

            if row == 1:
                request.session['username'] = username
                return redirect('admin_account')
            else:
                return HttpResponse("Invalid username or password")

        if account_type == 'Doktor':
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM doktorlar WHERE doktorun = %s AND doktorsifre = %s",
                               [username, password])
                row = cursor.fetchone()[0]

            if row == 1:
                request.session['dr_username'] = username
                return redirect('doctor_account')
            else:
                return HttpResponse("Invalid username or password")

        if account_type == 'Hasta':
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM hastalar WHERE hastaun = %s AND hastasifre = %s",
                               [username, password])
                row = cursor.fetchone()[0]

            if row == 1:
                request.session['hasta_username'] = username
                return redirect('hasta_account')
            else:
                return HttpResponse("Invalid username or password")
    else:
        return HttpResponse("Method not allowed")

def register(request):
    if request.method == 'POST':
        # Handle registration form submission
        name = request.POST.get('registerName')
        surname = request.POST.get('registerSurname')
        username = request.POST.get('registerUsername')
        password = request.POST.get('registerPassword')
        account_type = request.POST.get('accountType')

        if account_type == 'Yonetici':
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO yonetici (Ad, Soyad, yoneticiun, yoneticisifre) VALUES (%s, %s, %s, %s)",
                               [name, surname, username, password])
        elif account_type == 'Hasta':
            dogumtarihi = request.POST.get('birthDate')
            cinsiyet = request.POST.get('gender')
            telefon = request.POST.get('phone')
            adres = request.POST.get('address')
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO hastalar (Ad, Soyad, DogumTarihi, Cinsiyet, Telefon, Adres, hastaun, hastasifre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                               [name, surname, dogumtarihi, cinsiyet, telefon, adres, username, password])

        elif account_type == 'Doktor':
            uzmanlikalani = request.POST.get('specialty')
            hastane = request.POST.get('hospital')

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO doktorlar (Ad, Soyad, UzmanlikAlani, CalistigiHastane, doktorun, doktorsifre) VALUES (%s, %s, %s, %s, %s, %s)",
                               [name, surname, uzmanlikalani, hastane, username, password])

        return redirect('index')
    else:
        return HttpResponse("Method not allowed")
    
def admin_account(request):
    admin_username = request.session.get('username')
    if admin_username:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM yonetici WHERE yoneticiun = %s", [admin_username])
            admin_data = cursor.fetchone()

        return render(request, 'admin_account.html', {'admin_data': admin_data})
    else:
        return redirect('login')
    
def doctor_account(request):
    dr_username = request.session.get('dr_username')
    if dr_username:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM doktorlar WHERE doktorun = %s", [dr_username])
            doktor_data = cursor.fetchone()

        return render(request, 'doktor_account.html', {'doktor_data': doktor_data})
    else:
        return redirect('login')

def hasta_account(request):
    hasta_username = request.session.get('hasta_username')
    if hasta_username:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM hastalar WHERE hastaun = %s", [hasta_username])
            hasta_data = cursor.fetchone()

        return render(request, 'hasta_account.html', {'hasta_data': hasta_data, 'hasta_username': hasta_username})
    else:
        return redirect('login')


def admin_hasta_view(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        hasta_username = request.POST.get('hasta_username')
        hasta_password = request.POST.get('hasta_password')

        # Yeni hasta verilerini veritabanına ekleyin
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO hastalar (Ad, Soyad, DogumTarihi, Cinsiyet, Telefon, Adres, hastaun, hastasifre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, hasta_username, hasta_password])

        # Başarılı bir şekilde eklendikten sonra yönlendirme yapabilirsiniz
        return HttpResponseRedirect('/admin-hasta/')  # veya başka bir URL'ye yönlendirme yapabilirsiniz

    # GET isteği alındığında veya form hatalıysa, aynı sayfayı gösterin
    with connection.cursor() as cursor:
        # SQL sorgusu ile hastaları çek
        cursor.execute("SELECT * FROM hastalar")
        # Sorgu sonucunu al
        hastalar = cursor.fetchall()

    # HTML sayfasına hastaları ve ekleme formunu gönderin
    return render(request, 'admin_hasta.html', {'hastalar': hastalar})


def admin_doktor_view(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        uzmanlik = request.POST.get('uzmanlik')
        calistigi_hastane = request.POST.get('calistigi_hastane')
        doktorun = request.POST.get('doktorun')
        doktorsifre = request.POST.get('doktorsifre')

        # Yeni doktoru veritabanına ekleyin
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO doktorlar (Ad, Soyad, UzmanlikAlani, CalistigiHastane, doktorun, doktorsifre) VALUES (%s, %s, %s, %s, %s, %s)",
                [ad, soyad, uzmanlik, calistigi_hastane, doktorun, doktorsifre])

    # Tüm doktorları veritabanından alın
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM doktorlar")
        doktorlar = cursor.fetchall()

    # Ekleme formu ve doktorları HTML sayfasına gönderin
    return render(request, 'admin_doktor.html', {'doktorlar': doktorlar})

def admin_randevu_goruntule(request):
    if 'username' not in request.session:
        return HttpResponse("Unauthorized", status=401)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT r.RandevuID, r.RandevuTarihi, r.RandevuSaati, h.Ad AS HastaAd, h.Soyad AS HastaSoyad, 
                   d.Ad AS DoktorAd, d.Soyad AS DoktorSoyad
            FROM randevular r
            JOIN hastalar h ON r.HastaID = h.HastaID
            JOIN doktorlar d ON r.DoktorID = d.DoktorID
            ORDER BY r.RandevuID
        """)
        appointments = cursor.fetchall()

    return render(request, 'admin_randevu_goruntule.html', {'appointments': appointments})

def admin_randevu_ekle(request):
    if request.method == 'POST':
        randevu_tarihi = request.POST.get('randevuTarihi')
        randevu_saati = request.POST.get('randevuSaati')
        hasta_id = request.POST.get('hastaID')
        doktor_id = request.POST.get('doktorID')

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO randevular (RandevuTarihi, RandevuSaati, HastaID, DoktorID)
                VALUES (%s, %s, %s, %s)
            """, [randevu_tarihi, randevu_saati, hasta_id, doktor_id])

        return redirect('admin_randevu_goruntule')

    else:
        return render(request, 'admin_randevu_ekle.html')
    

def admin_randevu_guncelle(request, randevu_id):
    if 'username' not in request.session:
        return HttpResponse("Unauthorized", status=401)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT r.RandevuID, r.RandevuTarihi, r.RandevuSaati, h.Ad AS HastaAd, h.Soyad AS HastaSoyad, 
                   d.Ad AS DoktorAd, d.Soyad AS DoktorSoyad
            FROM randevular r
            JOIN hastalar h ON r.HastaID = h.HastaID
            JOIN doktorlar d ON r.DoktorID = d.DoktorID
            WHERE r.RandevuID = %s
        """, [randevu_id])
        appointment_info = cursor.fetchone()

    return render(request, 'admin_randevu_guncelle.html', {'appointment_info': appointment_info})

def admin_randevu_guncelle_post(request, randevu_id):
    if request.method == 'POST':
        randevu_tarihi = request.POST.get('RandevuTarihi')
        randevu_saati = request.POST.get('RandevuSaati')
        # Diğer randevu bilgilerini buradan alabilirsiniz

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE randevular
                SET RandevuTarihi = %s, RandevuSaati = %s
                WHERE RandevuID = %s
            """, [randevu_tarihi, randevu_saati, randevu_id])

        return redirect('admin_randevu_goruntule')
    else:
        return HttpResponse("Method not allowed", status=405)
    
    
def admin_randevu_sil(request, randevu_id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM randevular WHERE RandevuID = %s", [randevu_id])
        return redirect('admin_randevu_goruntule')
    else:
        return HttpResponse("Method not allowed", status=405)

def admin_rapor_goruntule(request):
    if 'username' not in request.session:
        return HttpResponse("Unauthorized", status=401)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM tibbiraporlar ORDER BY RaporTarihi DESC""")
        raporlar = cursor.fetchall()

    return render(request, 'admin_rapor_goruntule.html', {'raporlar': raporlar})


# def admin_rapor_ekle(request):
#     if request.method == 'POST':
#         raporID = request.POST.get('raporID')
#         raporTarihi = request.POST.get('raporTarihi')
#         raporIcerigi = request.POST.get('raporIcerigi')
#         hastaID = request.POST.get('hastaID')
#         doktorID = request.POST.get('doktorID')

#         # Resim dosyasını al
#         resim = request.FILES.get('resim')
#         j_rapor=request.FILES.get('jsonFile')

#         if resim:
#             # Dosya adını belirle
#             resim_adı = resim.name
#             resim_yolu = os.path.join(settings.MEDIA_ROOT, resim_adı)
#             # Dosyayı projedeki media klasörüne kaydet
#             with open(resim_yolu, 'wb') as f:
#                 for chunk in resim.chunks():
#                     f.write(chunk)
#             # Resim URL'sini belirle
#             resim_url = os.path.join(settings.MEDIA_URL, resim_adı)
#         else:
#             resim_url = None

#         if j_rapor:
#             # Dosya adını belirle
#             j_rapor_adı = j_rapor.name
#             j_rapor_yolu = os.path.join(settings.MEDIA_ROOT, j_rapor_adı)
#             # Dosyayı projedeki media klasörüne kaydet
#             with open(j_rapor_yolu, 'wb') as f:
#                 for chunk in j_rapor.chunks():
#                     f.write(chunk)
#             # Resim URL'sini belirle
#             j_rapor_url = os.path.join(settings.MEDIA_URL, j_rapor_adı)
#         else:
#             j_rapor_url = None

#         with open(j_rapor_yolu, 'r') as dosya:
#             jjveri = json.load(dosya)
#         jj=json.dumps(jjveri)


#         json_data = {
#             "muayne_sonucu": "Hafif enfeksiyon",
#             "tedavi_sureci": "1 hafta",
#             "tibbi_oneriler": "Bol su içmek, dinlenmek",
#             "kan_tahlil_sonucu": "Düşük",
#             "hastanin_sikayetleri": ["Boğaz ağrısı", "Mide bulantısı", "Baş ağrısı", "Ateş"],
#             "hastaya_verilen_ilaclar": ["Parol"],
#             "hastanin_sahip_oldugu_hastalik": "Grip"
#         }

#         # Python sözlüğünü JSON formatına dönüştürme
#         json_text = json.dumps(json_data)


#         #file_id = upload_image(r'C:\Users\Sait Omer\Pictures\Screenshots\Ekran görüntüsü 2023-10-27 045919.png')
#         file_id=upload_image(resim_yolu)
#         shareable_link = get_shareable_link(file_id)

#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "INSERT INTO tibbiraporlar (RaporID, RaporTarihi,RaporIcerigi, HastaID, DoktorID, ResimURL, JsonRapor) VALUES (%s, %s, %s, %s, %s, %s,%s)",
#                 [raporID, raporTarihi, raporIcerigi, hastaID, doktorID, shareable_link,jj])        # Başka bir sayfaya yönlendirme yapabilirsiniz
#         return redirect('admin_account')


#     return render(request, 'admin_rapor_ekle.html')

def admin_rapor_guncelle(request, rapor_id):
    if request.method == 'POST':
        # Formdan gönderilen verileri al
        rapor_icerigi = request.POST['rapor_icerigi']
        
        # Raporu güncelle
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE tibbiraporlar
                SET RaporIcerigi = %s
                WHERE RaporID = %s
            """, [rapor_icerigi, rapor_id])
        
        # Güncelleme işlemi tamamlandıktan sonra rapor listesi sayfasına yönlendir
        return redirect('admin_rapor_goruntule')

    else:
        # Raporu veritabanından al
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT RaporIcerigi FROM tibbiraporlar
                WHERE RaporID = %s
            """, [rapor_id])
            rapor_icerigi = cursor.fetchone()[0]
        
        return render(request, 'admin_rapor_guncelle.html', {'rapor_id': rapor_id, 'rapor_icerigi': rapor_icerigi})

def admin_rapor_sil(request, rapor_id):
    # Raporu sil
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM tibbiraporlar
            WHERE RaporID = %s
        """, [rapor_id])
    
    # Silme işlemi tamamlandıktan sonra rapor listesi sayfasına yönlendir
    return redirect('admin_rapor_goruntule')


    

def hasta_randevu_view(request):
    if 'hasta_username' not in request.session:
        return HttpResponse("Unauthorized", status=401)

    username = request.session['hasta_username']
    with connection.cursor() as cursor:
        cursor.execute("SELECT HastaID FROM hastalar WHERE hastaun = %s", [username])
        hasta_id = cursor.fetchone()[0]

    if request.method == 'POST':
        hastane = request.POST.get('hastane')
        uzmanlik_alani = request.POST.get('uzmanlik_alani')
        doktor = request.POST.get('doktor')
        tarih = request.POST.get('tarih')
        saat = request.POST.get('saat')

        if not all([hastane, uzmanlik_alani, doktor, tarih, saat]):
            return JsonResponse({'success': False, 'message': 'Eksik veri. Tüm alanları doldurun.'}, status=400)

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM randevular WHERE DoktorID = %s AND RandevuTarihi = %s AND RandevuSaati = %s",
                [doktor, tarih, saat]
            )
            randevu = cursor.fetchone()
            if randevu is None:
                cursor.execute(
                    "INSERT INTO randevular (DoktorID, RandevuTarihi, RandevuSaati, HastaID) VALUES (%s, %s, %s, %s)",
                    [doktor, tarih, saat, hasta_id]
                )
                return JsonResponse({'success': True, 'tarih': tarih, 'saat': saat, 'doktor_id': doktor}, status=200)
            else:
                return JsonResponse({'success': False, 'message': 'Seçilen tarih ve saatte randevu mevcut.'}, status=400)

    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT CalistigiHastane FROM doktorlar")
        hastaneler = [hastane[0] for hastane in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT UzmanlikAlani FROM doktorlar")
        uzmanlik_alanlari = [alan[0] for alan in cursor.fetchall()]

        cursor.execute("""
            SELECT r.RandevuTarihi, r.RandevuSaati, d.Ad, d.Soyad, d.CalistigiHastane
            FROM randevular r
            JOIN doktorlar d ON r.DoktorID = d.DoktorID
            WHERE r.HastaID = %s
            ORDER BY r.RandevuTarihi, r.RandevuSaati
        """, [hasta_id])
        randevular = cursor.fetchall()

    return render(request, 'hasta_randevu.html', {
        'hastaneler': hastaneler,
        'uzmanlik_alanlari': uzmanlik_alanlari,
        'randevular': randevular
    })

def get_doktorlar(request):
    hastane = request.GET.get('hastane')
    uzmanlik_alani = request.GET.get('uzmanlik_alani')
    
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT DoktorID, Ad, Soyad FROM doktorlar WHERE CalistigiHastane = %s AND UzmanlikAlani = %s",
            [hastane, uzmanlik_alani]
        )
        doktorlar = cursor.fetchall()
        result = [{'id': doktor[0], 'ad': doktor[1], 'soyad': doktor[2]} for doktor in doktorlar]
        
    return JsonResponse(result, safe=False)

def get_randevu_tarihleri(request):
    doktor = request.GET.get('doktor')

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT DISTINCT RandevuTarihi FROM randevular WHERE DoktorID = %s AND RandevuTarihi >= CURDATE()",
            [doktor]
        )
        randevu_tarihleri = cursor.fetchall()

    return JsonResponse(randevu_tarihleri, safe=False)

def get_randevu_saatleri(request):
    doktor = request.GET.get('doktor')
    tarih = request.GET.get('tarih')

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT RandevuSaati FROM randevular WHERE DoktorID = %s AND RandevuTarihi = %s",
            [doktor, tarih]
        )
        mevcut_saatler = cursor.fetchall()
        mevcut_saatler = [str(saat[0]) for saat in mevcut_saatler]
    
    calisma_saatleri = [f"{i}:00" for i in range(8, 17)]
    uygun_saatler = [saat for saat in calisma_saatleri if saat not in mevcut_saatler]

    return JsonResponse(uygun_saatler, safe=False)

def randevu_ekle_view(request):
    if request.method == 'POST':
        randevu_tarihi = request.POST.get('tarih')
        randevu_saati = request.POST.get('saat')
        doktor_id = request.POST.get('doktor')

        if not randevu_tarihi or not randevu_saati or not doktor_id:
            return JsonResponse({'success': False, 'message': 'Eksik veri. Tüm alanları doldurun.'}, status=400)

        # Hasta ID'sini oturumdan al
        if 'hasta_username' in request.session:
            username = request.session['hasta_username']
            with connection.cursor() as cursor:
                cursor.execute("SELECT HastaID FROM hastalar WHERE hastaun = %s", [username])
                hasta_id = cursor.fetchone()[0]
        else:
            return JsonResponse({'success': False, 'message': 'Hasta oturum bilgisi alınamadı'}, status=400)

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO randevular (RandevuTarihi, RandevuSaati, HastaID, DoktorID) VALUES (%s, %s, %s, %s)",
                [randevu_tarihi, randevu_saati, hasta_id, doktor_id]
            )
            connection.commit()
            return JsonResponse({'success': True, 'randevu_tarihi': randevu_tarihi, 'randevu_saati': randevu_saati, 'doktor_id': doktor_id})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Geçersiz istek yöntemi'})

def doktor_hasta_view(request):
    if 'dr_username' not in request.session:
        return HttpResponse("Unauthorized", status=401)

    dr_username = request.session['dr_username']

    with connection.cursor() as cursor:
        cursor.execute("SELECT DoktorID FROM doktorlar WHERE doktorun = %s", [dr_username])
        row = cursor.fetchone()
        if row:
            doktorID = row[0]
        else:
            return HttpResponse("Doktor bulunamadı", status=404)

        cursor.execute("""
            SELECT r.RandevuTarihi, r.RandevuSaati, h.HastaID, h.Ad, h.Soyad
            FROM randevular r
            JOIN hastalar h ON r.HastaID = h.HastaID
            WHERE r.DoktorID = %s
            ORDER BY r.RandevuTarihi, r.RandevuSaati
        """, [doktorID])
        randevular = cursor.fetchall()

    return render(request, 'doktor_hasta.html', {'randevular': randevular})

# def doktor_rapor_ekle(request, hastaID):
#     if request.method == 'POST':
#         raporTarihi = request.POST.get('raporTarihi')
#         raporIcerigi = request.POST.get('raporIcerigi')

#         if 'dr_username' not in request.session:
#             return HttpResponse("Unauthorized", status=401)

#         dr_username = request.session['dr_username']

#         with connection.cursor() as cursor:
#             cursor.execute("SELECT DoktorID FROM doktorlar WHERE doktorun = %s", [dr_username])
#             row = cursor.fetchone()
#             if row:
#                 doktorID = row[0]
#             else:
#                 return HttpResponse("Doktor bulunamadı", status=404)

#         resim = request.FILES.get('resim')
#         j_rapor = request.FILES.get('jsonFile')

#         resim_url = None
#         if resim:
#             resim_adı = resim.name
#             resim_yolu = os.path.join(settings.MEDIA_ROOT, resim_adı)
#             with open(resim_yolu, 'wb') as f:
#                 for chunk in resim.chunks():
#                     f.write(chunk)
#             file_id = upload_image(resim_yolu)
#             resim_url = get_shareable_link(file_id)

#         j_rapor_url = None
#         jj = None
#         if j_rapor:
#             j_rapor_adı = j_rapor.name
#             j_rapor_yolu = os.path.join(settings.MEDIA_ROOT, j_rapor_adı)
#             with open(j_rapor_yolu, 'wb') as f:
#                 for chunk in j_rapor.chunks():
#                     f.write(chunk)
#             try:
#                 with open(j_rapor_yolu, 'r') as dosya:
#                     jjveri = json.load(dosya)
#                 jj = json.dumps(jjveri)
#             except json.JSONDecodeError:
#                 return HttpResponse("Geçersiz JSON dosyası", status=400)

#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "INSERT INTO tibbiraporlar (RaporTarihi, RaporIcerigi, HastaID, DoktorID, ResimURL, JsonRapor) VALUES (%s, %s, %s, %s, %s, %s)",
#                 [raporTarihi, raporIcerigi, hastaID, doktorID, resim_url, jj])

#         return redirect('doktor_hasta_view')

#     return render(request, 'doktor_rapor_ekle.html', {'hastaID': hastaID})

def doktor_rapor_goruntule(request, hastaID):
    if 'dr_username' not in request.session:
        return HttpResponse("Unauthorized", status=401)

    dr_username = request.session['dr_username']

    with connection.cursor() as cursor:
        cursor.execute("SELECT DoktorID FROM doktorlar WHERE doktorun = %s", [dr_username])
        row = cursor.fetchone()
        if row:
            doktorID = row[0]
        else:
            return HttpResponse("Doktor bulunamadı", status=404)

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT RaporTarihi, RaporIcerigi, ResimURL, JsonRapor FROM tibbiraporlar WHERE HastaID = %s AND DoktorID = %s",
            [hastaID, doktorID]
        )
        raporlar = cursor.fetchall()

    return render(request, 'doktor_rapor_goruntule.html', {'raporlar': raporlar, 'hastaID': hastaID})

def hasta_ekle(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        hasta_username = request.POST.get('hasta_username')
        hasta_password = request.POST.get('hasta_password')

        # Burada gelen verileri kullanarak yeni bir hasta oluşturabilirsiniz
        # Örneğin:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO hastalar (Ad, Soyad, DogumTarihi, Cinsiyet, Telefon, Adres, hastaun, hastasifre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, hasta_username, hasta_password])


        # Başarılı bir şekilde eklendikten sonra yönlendirme yapabilirsiniz
        return HttpResponseRedirect('/adminhesap/')  # veya başka bir URL'ye yönlendirme yapabilirsiniz

    return render(request, 'hasta_ekle.html')

def doktor_ekle(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        uzmanlik = request.POST.get('uzmanlik')
        calistigi_hastane = request.POST.get('calistigi_hastane')
        doktorun = request.POST.get('doktorun')
        doktorsifre = request.POST.get('doktorsifre')

        # Veritabanına yeni doktor ekleyin

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO doktorlar (Ad, Soyad, UzmanlikAlani, CalistigiHastane, doktorun, doktorsifre) VALUES (%s, %s, %s, %s, %s, %s)",
                [ad, soyad, uzmanlik, calistigi_hastane, doktorun, doktorsifre])        # Başka bir sayfaya yönlendirme yapabilirsiniz
        return redirect('admin_account')  # anasayfa yerine doğru URL'yi girin

    # POST dışında bir istek alındığında ya da form hatalıysa, aynı sayfayı göster
    return render(request, 'doktor_ekle.html')

def hasta_rapor(request):
    if 'hasta_username' in request.session:
        hasta_username = request.session['hasta_username']

        with connection.cursor() as cursor:
            cursor.execute("SELECT HastaID FROM hastalar WHERE hastaun = %s", [hasta_username])
            row = cursor.fetchone()
            if row:
                hastaID = row[0]
            else:
                return HttpResponse("Hasta bulunamadı", status=404)

        with connection.cursor() as cursor:
            cursor.execute("SELECT RaporID, RaporTarihi, RaporIcerigi, ResimURL, JsonRapor FROM tibbiraporlar WHERE HastaID = %s", [hastaID])
            rows = cursor.fetchall()

            raporlar = [
                {
                    'RaporID': row[0],
                    'RaporTarihi': row[1],
                    'RaporIcerigi': row[2],
                    'ResimURL': row[3],
                    'JsonRapor': row[4]
                } for row in rows
            ]
    else:
        raporlar = []

    return render(request, 'hasta_rapor.html', {'raporlar': raporlar})

def get_rapor_json(request, rapor_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT JsonRapor FROM tibbiraporlar WHERE RaporID = %s", [rapor_id])
        row = cursor.fetchone()
        if row:
            return JsonResponse({'json': row[0]})
        else:
            return JsonResponse({'error': 'Rapor bulunamadı'}, status=404)  



# def hasta_rapor_ekle(request):
#     if request.method == 'POST':
#         raporTarihi = request.POST.get('raporTarihi')
#         raporIcerigi = request.POST.get('raporIcerigi')
#         doktorID = request.POST.get('doktorID')
        
#         if 'hasta_username' not in request.session:
#             return HttpResponse("Unauthorized", status=401)

#         hasta_username = request.session['hasta_username']

#         with connection.cursor() as cursor:
#             cursor.execute("SELECT HastaID FROM hastalar WHERE hastaun = %s", [hasta_username])
#             row = cursor.fetchone()
#             if row:
#                 hastaID = row[0]
#             else:
#                 return HttpResponse("Hasta bulunamadı", status=404)

#         resim = request.FILES.get('resim')
#         j_rapor = request.FILES.get('jsonFile')

#         resim_url = None
#         if resim:
#             resim_adı = resim.name
#             resim_yolu = os.path.join(settings.MEDIA_ROOT, resim_adı)
#             with open(resim_yolu, 'wb') as f:
#                 for chunk in resim.chunks():
#                     f.write(chunk)
#             resim_url = os.path.join(settings.MEDIA_URL, resim_adı)

#         j_rapor_url = None
#         jj = None
#         if j_rapor:
#             j_rapor_adı = j_rapor.name
#             j_rapor_yolu = os.path.join(settings.MEDIA_ROOT, j_rapor_adı)
#             with open(j_rapor_yolu, 'wb') as f:
#                 for chunk in j_rapor.chunks():
#                     f.write(chunk)
#             j_rapor_url = os.path.join(settings.MEDIA_URL, j_rapor_adı)

#             try:
#                 with open(j_rapor_yolu, 'r') as dosya:
#                     jjveri = json.load(dosya)
#                 jj = json.dumps(jjveri)
#             except json.JSONDecodeError:
#                 return HttpResponse("Geçersiz JSON dosyası", status=400)

#         file_id = upload_image(resim_yolu)
#         shareable_link = get_shareable_link(file_id)

#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "INSERT INTO tibbiraporlar (RaporTarihi, RaporIcerigi, HastaID, DoktorID, ResimURL, JsonRapor) VALUES (%s, %s, %s, %s, %s, %s)",
#                 [raporTarihi, raporIcerigi, hastaID, doktorID, shareable_link, jj])

#         return redirect('hasta_rapor_ekle')

#     if 'hasta_username' in request.session:
#         hasta_username = request.session['hasta_username']

#         with connection.cursor() as cursor:
#             cursor.execute("SELECT HastaID FROM hastalar WHERE hastaun = %s", [hasta_username])
#             row = cursor.fetchone()
#             if row:
#                 hastaID = row[0]
#             else:
#                 return HttpResponse("Hasta bulunamadı", status=404)

#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM tibbiraporlar WHERE HastaID = %s", [hastaID])
#             raporlar = cursor.fetchall()
#     else:
#         raporlar = []

#     return render(request, 'hasta_rapor.html', {'raporlar': raporlar})



def hasta_goruntule(request):
    with connection.cursor() as cursor:
        # SQL sorgusu ile hastaları çek
        cursor.execute("SELECT * FROM hastalar")
        # Sorgu sonucunu al
        hastalar = cursor.fetchall()
    # HTML sayfasına hastaları gönder
    return render(request, 'hasta_goruntule.html', {'hastalar': hastalar})


def hasta_sil(request):
    if request.method == 'POST':
        hasta_id = request.POST.get('hasta_id')
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tibbiraporlar WHERE HastaID = %s", [hasta_id])
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM randevular WHERE HastaID = %s", [hasta_id])
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM hastalar WHERE HastaID = %s", [hasta_id])
        return redirect('admin_hasta_view')  # Silme işlemi tamamlandıktan sonra tüm hastaların listesine yönlendir.
    else:
        return redirect('admin_hasta_view')

def doktor_goruntule(request):
    with connection.cursor() as cursor:
        # SQL sorgusu ile hastaları çek
        cursor.execute("SELECT * FROM doktorlar")
        # Sorgu sonucunu al
        doktorlar = cursor.fetchall()
    # HTML sayfasına hastaları gönder
    return render(request, 'doktor_goruntule.html', {'doktorlar': doktorlar})

def doktor_sil(request):
    if request.method == 'POST':
        doktor_id = request.POST.get('doktor_id')

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tibbiraporlar WHERE DoktorID = %s", [doktor_id])
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM randevular WHERE DoktorID = %s", [doktor_id])
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM doktorlar WHERE DoktorID = %s", [doktor_id])

        return redirect('admin_doktor_view')  # Silme işlemi tamamlandıktan sonra tüm hastaların listesine yönlendir.
    else:
        return redirect('admin_doktor_view')



def update_hasta(request):
    if request.method == 'POST':
        hasta_id = request.POST.get('hasta_id')  # Hasta ID'sini al
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        kullanici_adi = request.POST.get('username')
        sifre = request.POST.get('sifre')

        # SQL sorgusunu hazırla

        # SQL sorgusunu çalıştır
        with connection.cursor() as cursor:
            cursor.execute("UPDATE hastalar SET ad = %s, soyad = %s, dogumtarihi = %s, cinsiyet = %s, telefon = %s, adres = %s, hastaun = %s, hastasifre = %s WHERE hastaid = %s", [ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, kullanici_adi, sifre, hasta_id])

        # Güncelleme yapıldıktan sonra yönlendirme yap
        return redirect('hasta_goruntule')
    else:
        return redirect('hasta_goruntule')


def dr_hasta_goruntule(request):
    dr_username = request.session.get('dr_username')

    with connection.cursor() as cursor:
        # SQL sorgusu ile hastaları çek
        cursor.execute("SELECT * FROM hastalar WHERE HastaID IN ( SELECT HastaID FROM randevular WHERE DoktorID = ( SELECT DoktorID FROM doktorlar WHERE doktorun = %s ))",[dr_username])
        # Sorgu sonucunu al
        hastalar = cursor.fetchall()
    # HTML sayfasına hastaları gönder
    '''
    with connection.cursor() as cursor:
        # SQL sorgusu ile hastaları çek
        cursor.execute("SELECT * FROM hastalar")
        # Sorgu sonucunu al
        hastalar = cursor.fetchall()
    # HTML sayfasına hastaları gönder
    '''
    return render(request, 'dr_hasta_goruntule.html',{'hastalar': hastalar})


def hasta_detay(request, hasta_id):
    # Hasta detaylarını burada al ve HTML şablonuna gönder
    return render(request, 'hasta_detay.html', {'hasta_id': hasta_id})