# Panduan clone repository untuk Collaborator
1. Clone repository ini
```bash
git clone https://github.com/ZulfiFazhar/PSD-UAS-IF1-FOLIUM.git
```
2. Masuk ke folder PSD-UAS-IF1-FOLIUM
```bash
cd PSD-UAS-IF1-FOLIUM
```

# Panduan push code ke github
1. Pindah ke branch yang sudah disediakan sesuai dengan nama kalian, dengan list branch sebagai berikut:<br>
> main, irsyad, zulfi, mutiara, alif, izza

```bash
# sesuaikan dengan nama kalian, disini contoh akan masuk ke branch zulfi
git checkout zulfi
```
2. Lakukan pull code terlebih dahulu saat ingin memulai sesuatu
```bash
git pull origin main
```
3. Silahkan melakukan perubahan code apapun
4. Jika sudah menyelesaikan perubahan code dan akan melakukan push ke repository github, maka lakukan
```bash
git add .
```
5. Lakukan commit untuk memberi tahu pesan perubahannya
```bash
git commit -m "tulis pesan disini"
```
6. Lakukan perintah push ke repository github
```bash
# sesuaikan dengan nama kalian, disini contoh akan push code ke branch zulfi
git push origin zulfi
```