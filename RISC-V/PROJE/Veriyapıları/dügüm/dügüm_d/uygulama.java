package dügüm_d;

public class uygulama {
    
        public static void main(String[] args) {
            // Listeyi oluşturuyoruz
            anasinif liste = new anasinif();
    
            // Listeyi boşken yazdırmak
            liste.yazdir(); // Çıktı: Liste Boş.
    
            // Başa eleman ekliyoruz
            liste.basaekle(10);  // Çıktı: Eleman başa eklendi.
            liste.yazdir();  // Çıktı: Liste: 10
    
            // Sona eleman ekliyoruz
            liste.sonaekle(20);  // Çıktı: Listenin sonuna istenilen eleman eklendi.
            liste.yazdir();  // Çıktı: Liste: 10 20
    
            // Başa başka bir eleman ekliyoruz
            liste.basaekle(5);  // Çıktı: Eleman başa eklendi.
            liste.yazdir();  // Çıktı: Liste: 5 10 20
    
            // Araya bir eleman ekliyoruz (2. sıraya)
            liste.arayaekle(15, 1);  // Çıktı: 1. sıraya eleman eklendi.
            liste.yazdir();  // Çıktı: Liste: 5 15 10 20
    
            // 2. sıradaki elemanı siliyoruz
            liste.aradansil(1);  // Çıktı: 1. sıradaki eleman silindi.
            liste.yazdir();  // Çıktı: Liste: 5 10 20
    
            // Baştaki elemanı siliyoruz
            liste.bastansil();  // Çıktı: Baştaki eleman silindi.
            liste.yazdir();  // Çıktı: Liste: 10 20
    
            // Sondaki elemanı siliyoruz
            liste.sondansil();  // Çıktı: Listenin sonundaki eleman silindi.
    
}
}
