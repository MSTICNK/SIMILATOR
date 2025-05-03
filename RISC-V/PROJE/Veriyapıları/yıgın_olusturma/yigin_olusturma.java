import java.util.Stack;
public class yigin_olusturma {
    public static void main(String[] args) {
        // Stack'e başlangıç kapasitesi veriyoruz (örneğin 10)
        Stack<Integer> stack = new Stack<>();

        // Stack'e eleman ekleme
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Stack'teki en üst elemanı görmek
        System.out.println("Eleman eklendi: " + stack.peek());  // Çıktı: 30

        // Stack'ten eleman çıkarma
        System.out.println("Eleman silindi: " + stack.pop());  // Çıktı: 30

        // Stack boyutunu yazdırma
        System.out.println("Stack boyutu: " + stack.size());  // Çıktı: 2
    }
}

