-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tibbiraporlar`
--

DROP TABLE IF EXISTS `tibbiraporlar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tibbiraporlar` (
  `RaporID` int NOT NULL AUTO_INCREMENT,
  `RaporTarihi` date DEFAULT NULL,
  `RaporIcerigi` text,
  `HastaID` int DEFAULT NULL,
  `DoktorID` int DEFAULT NULL,
  `ResimURL` varchar(255) DEFAULT NULL,
  `JsonRapor` text,
  PRIMARY KEY (`RaporID`),
  KEY `HastaID` (`HastaID`),
  KEY `DoktorID` (`DoktorID`),
  CONSTRAINT `tibbiraporlar_ibfk_1` FOREIGN KEY (`HastaID`) REFERENCES `hastalar` (`HastaID`),
  CONSTRAINT `tibbiraporlar_ibfk_2` FOREIGN KEY (`DoktorID`) REFERENCES `doktorlar` (`DoktorID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tibbiraporlar`
--

LOCK TABLES `tibbiraporlar` WRITE;
/*!40000 ALTER TABLE `tibbiraporlar` DISABLE KEYS */;
INSERT INTO `tibbiraporlar` VALUES (1,'2024-05-16','Hasta şikayetleri incelendi, muayene yapıldı. Tedavi önerildi.',6005,734,'http://example.com/resim1.jpg','{\"muayene\": \"normal\", \"tedavi\": \"ilaç önerildi\"}'),(2,'2024-05-17','Hasta muayene edildi, kan testi yapıldı. Sonuçlar normal.',6005,1752,'http://example.com/resim2.jpg','{\"muayene\": \"normal\", \"kan_testi\": \"normal\"}'),(3,'2024-05-18','Hasta şikayetleri değerlendirildi, tetkikler yapıldı.',6005,700,'http://example.com/resim3.jpg','{\"muayene\": \"normal\", \"tetkikler\": \"sonuçlar beklenecek\"}'),(4,'2024-05-19','Hastanın durumu değerlendirildi, tedavi planlandı.',6005,734,'http://example.com/resim4.jpg','{\"muayene\": \"normal\", \"tedavi\": \"fizik tedavi önerildi\"}'),(5,'2024-05-20','Hasta muayene edildi, ilaçlarına devam edecek.',6005,1752,'http://example.com/resim5.jpg','{\"muayene\": \"normal\", \"tedavi_durumu\": \"iyileşme var\"}'),(6,'2024-05-21','Hasta kontrol için geldi, şikayetleri azaldı.',6005,700,'http://example.com/resim6.jpg','{\"muayene\": \"normal\", \"kontrol\": \"şikayetler azaldı\"}'),(7,'2024-05-22','Hasta muayene edildi, tetkikler sonucu bekleniyor.',6005,734,'http://example.com/resim7.jpg','{\"muayene\": \"normal\", \"tetkikler\": \"sonuçlar beklenecek\"}'),(8,'2024-05-23','Hasta muayene edildi, tedavi planlandı. Rapor güncelleme denemesi yapılıyor...',6005,1752,'http://example.com/resim8.jpg','{\"muayene\": \"normal\", \"tedavi\": \"ilaç değişikliği önerildi\"}'),(9,'2024-05-19','Rapor ekleme denemesi 1',6005,NULL,'https://drive.google.com/file/d/1MeMtD6w4W5yNN0z4Wz-m2973drA_Gx25/view?usp=drivesdk','[{\"version\": \"1.0\", \"image\": {\"name\": \"../tmp/959997099914099917243508/QTg=.png\", \"permissions\": 644, \"format\": \"PNG\", \"formatDescription\": \"Portable Network Graphics\", \"mimeType\": \"image/png\", \"class\": \"DirectClass\", \"geometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"resolution\": {\"x\": 37.79, \"y\": 37.79}, \"printSize\": {\"x\": 22.2281, \"y\": 13.3633}, \"units\": \"PixelsPerCentimeter\", \"type\": \"TrueColorAlpha\", \"endianness\": \"Undefined\", \"colorspace\": \"sRGB\", \"depth\": 8, \"baseDepth\": 8, \"channelDepth\": {\"alpha\": 1, \"red\": 8, \"green\": 8, \"blue\": 8}, \"pixels\": 424200, \"imageStatistics\": {\"all\": {\"min\": 0, \"max\": 255, \"mean\": 204.654, \"standardDeviation\": 44.5497, \"kurtosis\": 4.22209, \"skewness\": -2.09753, \"entropy\": 0.588752}}, \"channelStatistics\": {\"alpha\": {\"min\": 0, \"max\": 0, \"mean\": 0, \"standardDeviation\": 0, \"kurtosis\": 8.192e+51, \"skewness\": 1e+36, \"entropy\": 0}, \"red\": {\"min\": 0, \"max\": 255, \"mean\": 188.498, \"standardDeviation\": 68.2057, \"kurtosis\": 2.21149, \"skewness\": -1.91501, \"entropy\": 0.784664}, \"green\": {\"min\": 0, \"max\": 255, \"mean\": 193.775, \"standardDeviation\": 57.2233, \"kurtosis\": 3.98933, \"skewness\": -2.16648, \"entropy\": 0.78196}, \"blue\": {\"min\": 0, \"max\": 255, \"mean\": 181.341, \"standardDeviation\": 52.77, \"kurtosis\": 4.84562, \"skewness\": -2.29728, \"entropy\": 0.788384}}, \"renderingIntent\": \"Perceptual\", \"gamma\": 0.45455, \"chromaticity\": {\"redPrimary\": {\"x\": 0.64, \"y\": 0.33}, \"greenPrimary\": {\"x\": 0.3, \"y\": 0.6}, \"bluePrimary\": {\"x\": 0.15, \"y\": 0.06}, \"whitePrimary\": {\"x\": 0.3127, \"y\": 0.329}}, \"backgroundColor\": \"#FFFFFFFF\", \"borderColor\": \"#DFDFDFFF\", \"matteColor\": \"#BDBDBDFF\", \"transparentColor\": \"#00000000\", \"interlace\": \"None\", \"intensity\": \"Undefined\", \"compose\": \"Over\", \"pageGeometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"dispose\": \"Undefined\", \"iterations\": 0, \"compression\": \"Zip\", \"orientation\": \"Undefined\", \"properties\": {\"date:create\": \"2024-05-16T18:00:10+00:00\", \"date:modify\": \"2024-05-16T18:00:10+00:00\", \"date:timestamp\": \"2024-05-16T18:00:10+00:00\", \"png:cHRM\": \"chunk was found (see Chromaticity, above)\", \"png:gAMA\": \"gamma=0.45455 (See Gamma, above)\", \"png:IHDR.bit-depth-orig\": \"8\", \"png:IHDR.bit_depth\": \"8\", \"png:IHDR.color-type-orig\": \"6\", \"png:IHDR.color_type\": \"6 (RGBA)\", \"png:IHDR.interlace_method\": \"0 (Not interlaced)\", \"png:IHDR.width,height\": \"840, 505\", \"png:pHYs\": \"x_res=3779, y_res=3779, units=1\", \"png:sRGB\": \"intent=0 (Perceptual Intent)\", \"signature\": \"6733390d71c4c1d463c722ddd7d18bcfa78b8ed7ebeb70acc547bb5f3289522e\"}, \"artifacts\": {\"filename\": \"../tmp/959997099914099917243508/QTg=.png\"}, \"tainted\": false, \"filesize\": \"694599B\", \"numberPixels\": \"424200\", \"pixelsPerSecond\": \"27.2605MB\", \"userTime\": \"0.020u\", \"elapsedTime\": \"0:01.015\", \"version\": \"ImageMagick 6.9.12-93 Q16 x86_64 17898 https://legacy.imagemagick.org\"}}]'),(10,'2024-05-19','Rapor ekleme denemesi 1',6005,NULL,'https://drive.google.com/file/d/1290tqF9-MOTRVeANUpF2pZg0Zr5LNLc1/view?usp=drivesdk','[{\"version\": \"1.0\", \"image\": {\"name\": \"../tmp/959997099914099917243508/QTg=.png\", \"permissions\": 644, \"format\": \"PNG\", \"formatDescription\": \"Portable Network Graphics\", \"mimeType\": \"image/png\", \"class\": \"DirectClass\", \"geometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"resolution\": {\"x\": 37.79, \"y\": 37.79}, \"printSize\": {\"x\": 22.2281, \"y\": 13.3633}, \"units\": \"PixelsPerCentimeter\", \"type\": \"TrueColorAlpha\", \"endianness\": \"Undefined\", \"colorspace\": \"sRGB\", \"depth\": 8, \"baseDepth\": 8, \"channelDepth\": {\"alpha\": 1, \"red\": 8, \"green\": 8, \"blue\": 8}, \"pixels\": 424200, \"imageStatistics\": {\"all\": {\"min\": 0, \"max\": 255, \"mean\": 204.654, \"standardDeviation\": 44.5497, \"kurtosis\": 4.22209, \"skewness\": -2.09753, \"entropy\": 0.588752}}, \"channelStatistics\": {\"alpha\": {\"min\": 0, \"max\": 0, \"mean\": 0, \"standardDeviation\": 0, \"kurtosis\": 8.192e+51, \"skewness\": 1e+36, \"entropy\": 0}, \"red\": {\"min\": 0, \"max\": 255, \"mean\": 188.498, \"standardDeviation\": 68.2057, \"kurtosis\": 2.21149, \"skewness\": -1.91501, \"entropy\": 0.784664}, \"green\": {\"min\": 0, \"max\": 255, \"mean\": 193.775, \"standardDeviation\": 57.2233, \"kurtosis\": 3.98933, \"skewness\": -2.16648, \"entropy\": 0.78196}, \"blue\": {\"min\": 0, \"max\": 255, \"mean\": 181.341, \"standardDeviation\": 52.77, \"kurtosis\": 4.84562, \"skewness\": -2.29728, \"entropy\": 0.788384}}, \"renderingIntent\": \"Perceptual\", \"gamma\": 0.45455, \"chromaticity\": {\"redPrimary\": {\"x\": 0.64, \"y\": 0.33}, \"greenPrimary\": {\"x\": 0.3, \"y\": 0.6}, \"bluePrimary\": {\"x\": 0.15, \"y\": 0.06}, \"whitePrimary\": {\"x\": 0.3127, \"y\": 0.329}}, \"backgroundColor\": \"#FFFFFFFF\", \"borderColor\": \"#DFDFDFFF\", \"matteColor\": \"#BDBDBDFF\", \"transparentColor\": \"#00000000\", \"interlace\": \"None\", \"intensity\": \"Undefined\", \"compose\": \"Over\", \"pageGeometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"dispose\": \"Undefined\", \"iterations\": 0, \"compression\": \"Zip\", \"orientation\": \"Undefined\", \"properties\": {\"date:create\": \"2024-05-16T18:00:10+00:00\", \"date:modify\": \"2024-05-16T18:00:10+00:00\", \"date:timestamp\": \"2024-05-16T18:00:10+00:00\", \"png:cHRM\": \"chunk was found (see Chromaticity, above)\", \"png:gAMA\": \"gamma=0.45455 (See Gamma, above)\", \"png:IHDR.bit-depth-orig\": \"8\", \"png:IHDR.bit_depth\": \"8\", \"png:IHDR.color-type-orig\": \"6\", \"png:IHDR.color_type\": \"6 (RGBA)\", \"png:IHDR.interlace_method\": \"0 (Not interlaced)\", \"png:IHDR.width,height\": \"840, 505\", \"png:pHYs\": \"x_res=3779, y_res=3779, units=1\", \"png:sRGB\": \"intent=0 (Perceptual Intent)\", \"signature\": \"6733390d71c4c1d463c722ddd7d18bcfa78b8ed7ebeb70acc547bb5f3289522e\"}, \"artifacts\": {\"filename\": \"../tmp/959997099914099917243508/QTg=.png\"}, \"tainted\": false, \"filesize\": \"694599B\", \"numberPixels\": \"424200\", \"pixelsPerSecond\": \"27.2605MB\", \"userTime\": \"0.020u\", \"elapsedTime\": \"0:01.015\", \"version\": \"ImageMagick 6.9.12-93 Q16 x86_64 17898 https://legacy.imagemagick.org\"}}]'),(12,'2024-05-16','Salim Doktor İçin Rapor Denemesi',6006,2019,NULL,'[{\"version\": \"1.0\", \"image\": {\"name\": \"../tmp/959997099914099917243508/QTg=.png\", \"permissions\": 644, \"format\": \"PNG\", \"formatDescription\": \"Portable Network Graphics\", \"mimeType\": \"image/png\", \"class\": \"DirectClass\", \"geometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"resolution\": {\"x\": 37.79, \"y\": 37.79}, \"printSize\": {\"x\": 22.2281, \"y\": 13.3633}, \"units\": \"PixelsPerCentimeter\", \"type\": \"TrueColorAlpha\", \"endianness\": \"Undefined\", \"colorspace\": \"sRGB\", \"depth\": 8, \"baseDepth\": 8, \"channelDepth\": {\"alpha\": 1, \"red\": 8, \"green\": 8, \"blue\": 8}, \"pixels\": 424200, \"imageStatistics\": {\"all\": {\"min\": 0, \"max\": 255, \"mean\": 204.654, \"standardDeviation\": 44.5497, \"kurtosis\": 4.22209, \"skewness\": -2.09753, \"entropy\": 0.588752}}, \"channelStatistics\": {\"alpha\": {\"min\": 0, \"max\": 0, \"mean\": 0, \"standardDeviation\": 0, \"kurtosis\": 8.192e+51, \"skewness\": 1e+36, \"entropy\": 0}, \"red\": {\"min\": 0, \"max\": 255, \"mean\": 188.498, \"standardDeviation\": 68.2057, \"kurtosis\": 2.21149, \"skewness\": -1.91501, \"entropy\": 0.784664}, \"green\": {\"min\": 0, \"max\": 255, \"mean\": 193.775, \"standardDeviation\": 57.2233, \"kurtosis\": 3.98933, \"skewness\": -2.16648, \"entropy\": 0.78196}, \"blue\": {\"min\": 0, \"max\": 255, \"mean\": 181.341, \"standardDeviation\": 52.77, \"kurtosis\": 4.84562, \"skewness\": -2.29728, \"entropy\": 0.788384}}, \"renderingIntent\": \"Perceptual\", \"gamma\": 0.45455, \"chromaticity\": {\"redPrimary\": {\"x\": 0.64, \"y\": 0.33}, \"greenPrimary\": {\"x\": 0.3, \"y\": 0.6}, \"bluePrimary\": {\"x\": 0.15, \"y\": 0.06}, \"whitePrimary\": {\"x\": 0.3127, \"y\": 0.329}}, \"backgroundColor\": \"#FFFFFFFF\", \"borderColor\": \"#DFDFDFFF\", \"matteColor\": \"#BDBDBDFF\", \"transparentColor\": \"#00000000\", \"interlace\": \"None\", \"intensity\": \"Undefined\", \"compose\": \"Over\", \"pageGeometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"dispose\": \"Undefined\", \"iterations\": 0, \"compression\": \"Zip\", \"orientation\": \"Undefined\", \"properties\": {\"date:create\": \"2024-05-16T18:00:10+00:00\", \"date:modify\": \"2024-05-16T18:00:10+00:00\", \"date:timestamp\": \"2024-05-16T18:00:10+00:00\", \"png:cHRM\": \"chunk was found (see Chromaticity, above)\", \"png:gAMA\": \"gamma=0.45455 (See Gamma, above)\", \"png:IHDR.bit-depth-orig\": \"8\", \"png:IHDR.bit_depth\": \"8\", \"png:IHDR.color-type-orig\": \"6\", \"png:IHDR.color_type\": \"6 (RGBA)\", \"png:IHDR.interlace_method\": \"0 (Not interlaced)\", \"png:IHDR.width,height\": \"840, 505\", \"png:pHYs\": \"x_res=3779, y_res=3779, units=1\", \"png:sRGB\": \"intent=0 (Perceptual Intent)\", \"signature\": \"6733390d71c4c1d463c722ddd7d18bcfa78b8ed7ebeb70acc547bb5f3289522e\"}, \"artifacts\": {\"filename\": \"../tmp/959997099914099917243508/QTg=.png\"}, \"tainted\": false, \"filesize\": \"694599B\", \"numberPixels\": \"424200\", \"pixelsPerSecond\": \"27.2605MB\", \"userTime\": \"0.020u\", \"elapsedTime\": \"0:01.015\", \"version\": \"ImageMagick 6.9.12-93 Q16 x86_64 17898 https://legacy.imagemagick.org\"}}]'),(13,'2024-05-29','Salim Doktor İçin Rapor Denemesi-2',6006,2019,'https://drive.google.com/file/d/1290tqF9-MOTRVeANUpF2pZg0Zr5LNLc1/view?usp=drivesdk','[{\"version\": \"1.0\", \"image\": {\"name\": \"../tmp/959997099914099917243508/QTg=.png\", \"permissions\": 644, \"format\": \"PNG\", \"formatDescription\": \"Portable Network Graphics\", \"mimeType\": \"image/png\", \"class\": \"DirectClass\", \"geometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"resolution\": {\"x\": 37.79, \"y\": 37.79}, \"printSize\": {\"x\": 22.2281, \"y\": 13.3633}, \"units\": \"PixelsPerCentimeter\", \"type\": \"TrueColorAlpha\", \"endianness\": \"Undefined\", \"colorspace\": \"sRGB\", \"depth\": 8, \"baseDepth\": 8, \"channelDepth\": {\"alpha\": 1, \"red\": 8, \"green\": 8, \"blue\": 8}, \"pixels\": 424200, \"imageStatistics\": {\"all\": {\"min\": 0, \"max\": 255, \"mean\": 204.654, \"standardDeviation\": 44.5497, \"kurtosis\": 4.22209, \"skewness\": -2.09753, \"entropy\": 0.588752}}, \"channelStatistics\": {\"alpha\": {\"min\": 0, \"max\": 0, \"mean\": 0, \"standardDeviation\": 0, \"kurtosis\": 8.192e+51, \"skewness\": 1e+36, \"entropy\": 0}, \"red\": {\"min\": 0, \"max\": 255, \"mean\": 188.498, \"standardDeviation\": 68.2057, \"kurtosis\": 2.21149, \"skewness\": -1.91501, \"entropy\": 0.784664}, \"green\": {\"min\": 0, \"max\": 255, \"mean\": 193.775, \"standardDeviation\": 57.2233, \"kurtosis\": 3.98933, \"skewness\": -2.16648, \"entropy\": 0.78196}, \"blue\": {\"min\": 0, \"max\": 255, \"mean\": 181.341, \"standardDeviation\": 52.77, \"kurtosis\": 4.84562, \"skewness\": -2.29728, \"entropy\": 0.788384}}, \"renderingIntent\": \"Perceptual\", \"gamma\": 0.45455, \"chromaticity\": {\"redPrimary\": {\"x\": 0.64, \"y\": 0.33}, \"greenPrimary\": {\"x\": 0.3, \"y\": 0.6}, \"bluePrimary\": {\"x\": 0.15, \"y\": 0.06}, \"whitePrimary\": {\"x\": 0.3127, \"y\": 0.329}}, \"backgroundColor\": \"#FFFFFFFF\", \"borderColor\": \"#DFDFDFFF\", \"matteColor\": \"#BDBDBDFF\", \"transparentColor\": \"#00000000\", \"interlace\": \"None\", \"intensity\": \"Undefined\", \"compose\": \"Over\", \"pageGeometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"dispose\": \"Undefined\", \"iterations\": 0, \"compression\": \"Zip\", \"orientation\": \"Undefined\", \"properties\": {\"date:create\": \"2024-05-16T18:00:10+00:00\", \"date:modify\": \"2024-05-16T18:00:10+00:00\", \"date:timestamp\": \"2024-05-16T18:00:10+00:00\", \"png:cHRM\": \"chunk was found (see Chromaticity, above)\", \"png:gAMA\": \"gamma=0.45455 (See Gamma, above)\", \"png:IHDR.bit-depth-orig\": \"8\", \"png:IHDR.bit_depth\": \"8\", \"png:IHDR.color-type-orig\": \"6\", \"png:IHDR.color_type\": \"6 (RGBA)\", \"png:IHDR.interlace_method\": \"0 (Not interlaced)\", \"png:IHDR.width,height\": \"840, 505\", \"png:pHYs\": \"x_res=3779, y_res=3779, units=1\", \"png:sRGB\": \"intent=0 (Perceptual Intent)\", \"signature\": \"6733390d71c4c1d463c722ddd7d18bcfa78b8ed7ebeb70acc547bb5f3289522e\"}, \"artifacts\": {\"filename\": \"../tmp/959997099914099917243508/QTg=.png\"}, \"tainted\": false, \"filesize\": \"694599B\", \"numberPixels\": \"424200\", \"pixelsPerSecond\": \"27.2605MB\", \"userTime\": \"0.020u\", \"elapsedTime\": \"0:01.015\", \"version\": \"ImageMagick 6.9.12-93 Q16 x86_64 17898 https://legacy.imagemagick.org\"}}]'),(20,'2024-05-24','Rapor ekleme denemesi 111',76,255,'https://drive.google.com/file/d/1SHkVy2bklcoZfP46rSlV8qYLgSQLJM9O/view?usp=drivesdk','{\"raporlar\": [{\"id\": 1, \"baslik\": \"Sat\\u00c4\\u00b1\\u00c5\\u0178 Raporu\", \"tarih\": \"2024-05-18\", \"icerik\": \"Bu rapor, ayl\\u00c4\\u00b1k sat\\u00c4\\u00b1\\u00c5\\u0178 verilerini i\\u00c3\\u00a7ermektedir.\"}, {\"id\": 2, \"baslik\": \"M\\u00c3\\u00bc\\u00c5\\u0178teri Raporu\", \"tarih\": \"2024-05-18\", \"icerik\": \"Bu rapor, m\\u00c3\\u00bc\\u00c5\\u0178teri memnuniyet anketlerinin sonu\\u00c3\\u00a7lar\\u00c4\\u00b1n\\u00c4\\u00b1 i\\u00c3\\u00a7ermektedir.\"}]}'),(21,'2024-05-25','Doktor Rapor Ekliyor...',6006,2019,NULL,'{\"raporlar\": [{\"id\": 1, \"baslik\": \"Sat\\u00c4\\u00b1\\u00c5\\u0178 Raporu\", \"tarih\": \"2024-05-18\", \"icerik\": \"Bu rapor, ayl\\u00c4\\u00b1k sat\\u00c4\\u00b1\\u00c5\\u0178 verilerini i\\u00c3\\u00a7ermektedir.\"}, {\"id\": 2, \"baslik\": \"M\\u00c3\\u00bc\\u00c5\\u0178teri Raporu\", \"tarih\": \"2024-05-18\", \"icerik\": \"Bu rapor, m\\u00c3\\u00bc\\u00c5\\u0178teri memnuniyet anketlerinin sonu\\u00c3\\u00a7lar\\u00c4\\u00b1n\\u00c4\\u00b1 i\\u00c3\\u00a7ermektedir.\"}]}'),(22,'2024-05-25','Doktor Rapor Ekliyor.1234',6006,2019,'https://drive.google.com/file/d/18akYVQm1xOnBK2Ss8_13ktw4hnhIQPLe/view?usp=drivesdk','{\"raporlar\": [{\"id\": 1, \"baslik\": \"Sat\\u00c4\\u00b1\\u00c5\\u0178 Raporu\", \"tarih\": \"2024-05-18\", \"icerik\": \"Bu rapor, ayl\\u00c4\\u00b1k sat\\u00c4\\u00b1\\u00c5\\u0178 verilerini i\\u00c3\\u00a7ermektedir.\"}, {\"id\": 2, \"baslik\": \"M\\u00c3\\u00bc\\u00c5\\u0178teri Raporu\", \"tarih\": \"2024-05-18\", \"icerik\": \"Bu rapor, m\\u00c3\\u00bc\\u00c5\\u0178teri memnuniyet anketlerinin sonu\\u00c3\\u00a7lar\\u00c4\\u00b1n\\u00c4\\u00b1 i\\u00c3\\u00a7ermektedir.\"}]}'),(23,'2024-05-24','Rapor Ekleniyor',6005,34,'https://drive.google.com/file/d/1SHkVy2bklcoZfP46rSlV8qYLgSQLJM9O/view?usp=drivesdk','[{\"version\": \"1.0\", \"image\": {\"name\": \"../tmp/959997099914099917243508/QTg=.png\", \"permissions\": 644, \"format\": \"PNG\", \"formatDescription\": \"Portable Network Graphics\", \"mimeType\": \"image/png\", \"class\": \"DirectClass\", \"geometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"resolution\": {\"x\": 37.79, \"y\": 37.79}, \"printSize\": {\"x\": 22.2281, \"y\": 13.3633}, \"units\": \"PixelsPerCentimeter\", \"type\": \"TrueColorAlpha\", \"endianness\": \"Undefined\", \"colorspace\": \"sRGB\", \"depth\": 8, \"baseDepth\": 8, \"channelDepth\": {\"alpha\": 1, \"red\": 8, \"green\": 8, \"blue\": 8}, \"pixels\": 424200, \"imageStatistics\": {\"all\": {\"min\": 0, \"max\": 255, \"mean\": 204.654, \"standardDeviation\": 44.5497, \"kurtosis\": 4.22209, \"skewness\": -2.09753, \"entropy\": 0.588752}}, \"channelStatistics\": {\"alpha\": {\"min\": 0, \"max\": 0, \"mean\": 0, \"standardDeviation\": 0, \"kurtosis\": 8.192e+51, \"skewness\": 1e+36, \"entropy\": 0}, \"red\": {\"min\": 0, \"max\": 255, \"mean\": 188.498, \"standardDeviation\": 68.2057, \"kurtosis\": 2.21149, \"skewness\": -1.91501, \"entropy\": 0.784664}, \"green\": {\"min\": 0, \"max\": 255, \"mean\": 193.775, \"standardDeviation\": 57.2233, \"kurtosis\": 3.98933, \"skewness\": -2.16648, \"entropy\": 0.78196}, \"blue\": {\"min\": 0, \"max\": 255, \"mean\": 181.341, \"standardDeviation\": 52.77, \"kurtosis\": 4.84562, \"skewness\": -2.29728, \"entropy\": 0.788384}}, \"renderingIntent\": \"Perceptual\", \"gamma\": 0.45455, \"chromaticity\": {\"redPrimary\": {\"x\": 0.64, \"y\": 0.33}, \"greenPrimary\": {\"x\": 0.3, \"y\": 0.6}, \"bluePrimary\": {\"x\": 0.15, \"y\": 0.06}, \"whitePrimary\": {\"x\": 0.3127, \"y\": 0.329}}, \"backgroundColor\": \"#FFFFFFFF\", \"borderColor\": \"#DFDFDFFF\", \"matteColor\": \"#BDBDBDFF\", \"transparentColor\": \"#00000000\", \"interlace\": \"None\", \"intensity\": \"Undefined\", \"compose\": \"Over\", \"pageGeometry\": {\"width\": 840, \"height\": 505, \"x\": 0, \"y\": 0}, \"dispose\": \"Undefined\", \"iterations\": 0, \"compression\": \"Zip\", \"orientation\": \"Undefined\", \"properties\": {\"date:create\": \"2024-05-16T18:00:10+00:00\", \"date:modify\": \"2024-05-16T18:00:10+00:00\", \"date:timestamp\": \"2024-05-16T18:00:10+00:00\", \"png:cHRM\": \"chunk was found (see Chromaticity, above)\", \"png:gAMA\": \"gamma=0.45455 (See Gamma, above)\", \"png:IHDR.bit-depth-orig\": \"8\", \"png:IHDR.bit_depth\": \"8\", \"png:IHDR.color-type-orig\": \"6\", \"png:IHDR.color_type\": \"6 (RGBA)\", \"png:IHDR.interlace_method\": \"0 (Not interlaced)\", \"png:IHDR.width,height\": \"840, 505\", \"png:pHYs\": \"x_res=3779, y_res=3779, units=1\", \"png:sRGB\": \"intent=0 (Perceptual Intent)\", \"signature\": \"6733390d71c4c1d463c722ddd7d18bcfa78b8ed7ebeb70acc547bb5f3289522e\"}, \"artifacts\": {\"filename\": \"../tmp/959997099914099917243508/QTg=.png\"}, \"tainted\": false, \"filesize\": \"694599B\", \"numberPixels\": \"424200\", \"pixelsPerSecond\": \"27.2605MB\", \"userTime\": \"0.020u\", \"elapsedTime\": \"0:01.015\", \"version\": \"ImageMagick 6.9.12-93 Q16 x86_64 17898 https://legacy.imagemagick.org\"}}]');
/*!40000 ALTER TABLE `tibbiraporlar` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-26  1:24:31