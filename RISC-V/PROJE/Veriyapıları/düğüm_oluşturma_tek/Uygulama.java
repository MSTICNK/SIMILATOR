package düğüm_oluşturma;
public class Uygulama {
public static void main(String[] args){
Liste_Yapisi liste = new Liste_Yapisi();

liste.basaekle(96);
liste.basaekle(58);
liste.basaekle(71);
liste.sonaekle(12);
liste.sonaekle(40);
liste.basaekle(9);
liste.sonaekle(0);
liste.arayaekle(5, 2);
liste.arayaekle(0, 4);
liste.yazdir();
liste.bastansil();
liste.sondansil();
liste.aradansil(2);
liste.aradansil(3);
liste.yazdır();

}
}
