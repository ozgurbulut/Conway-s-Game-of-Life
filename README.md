Çalışma açıklaması:
Program random değerler üreterek boş kareleri dolduracak hücreler üretmektedir. Hücrelerin bir sonraki durumu hesaplanıp yerine konulurken yeni durum sütünlar soldan sağa taranılarak yerine konulur. Her ekran yenilenmesi bir önceki durumun yenilenmiş halidir tekrardan random değerler üretilmez. Soldan sağa tarama işlemi yavaş olduğu için yenilenme süresi en düşük olarak 10ms ye çekildi.Her bir döngü bütün sütünların taranmasından sonra tekrar yenilendiği için 25x25 ızgara boyutundan büyük izgara seçilmedi hesaplama süresi çok uzuyor.



Gereklilikler:
Program Python 2x sürümleri üzerinde çalışmaktadir. Eğer çalışmıyorsa gerekli komutları aşağıdan çağırınız.
Programın Python 3x de çalışması için gerekli paketlerin yüklenmesi:

sudo apt install python-pip

sudo apt-get install python-tk

Açıklama:
Hayat oyunu 1970'te İngiliz matematikçi Horton Conway tarafından geliştirirmiş bir hücresel otomattır. Hücresel otomatın en iyi bilinen örneğidir. 
