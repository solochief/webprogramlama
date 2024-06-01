# Hasta Takip ve Yönetim Sistemi

Bu proje, Django kullanılarak oluşturulmuş bir web uygulamasıdır. Hasta takibi ve yönetimi için geliştirilmiştir.

## Kurulum

Projenin çalıştırılması için Docker kullanılmaktadır. Bilgisayarınızda Docker yüklü olmalıdır. Docker'ı bilgisayarınıza [buradan](https://www.docker.com/get-started) indirebilirsiniz.

1. Bu repository'yi bilgisayarınıza klonlayın:

    ```bash
    git clone https://github.com/kullanici/hasta-takip-ve-yonetim-sistemi.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd hasta-takip-ve-yonetim-sistemi
    ```

3. Docker-compose kullanarak projeyi başlatın:

    ```bash
    docker-compose up
    ```

4. Web tarayıcınızdan `http://localhost:8000` adresine giderek uygulamaya erişebilirsiniz.

## Sorun Giderme

- **Port Hatası**: Docker'ı başlatırken port çakışması hatası alıyorsanız, bilgisayarınızda başka bir MySQL sunucusunun veya başka bir uygulamanın aynı portu kullandığından emin olun. Eğer başka bir uygulama kullanıyorsa, onu kapatın veya portunu değiştirin. Docker'da farklı bir port kullanmak için `docker-compose.yml` dosyasındaki `ports` bölümünden `db` servisi için portu değiştirebilirsiniz.

## Katkılar

- 210201074 / Berat Ölmez

