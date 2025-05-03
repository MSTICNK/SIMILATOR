public class uygulama {
public static void main(String[] args){
    kuyruk_yapisi kuyruk = new kuyruk_yapisi(3);
    kuyruk.ekleme(7);
    kuyruk.yazdır();
    kuyruk.silme();
    kuyruk.yazdır();
    kuyruk.ekleme(4);
    kuyruk.ekleme(9);
    kuyruk.ekleme(45);
    
    kuyruk.yazdır();
}    


}
