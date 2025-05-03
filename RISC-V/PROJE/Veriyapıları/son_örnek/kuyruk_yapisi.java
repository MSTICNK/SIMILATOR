public class kuyruk_yapisi {
    int[] dizi;
    int size;
    int front;
    int rear;

    public kuyruk_yapisi(int size) {
        this.size = size;
        dizi = new int[size];
        front = 0;
        rear = -1;
    }

    void ekleme(int x) {
        if (isFull()) {
            System.out.println("Kuyruk yapısı dolu");
        } else {
            rear++;
            dizi[rear] = x;
            System.out.println("Eklendi: " + x);
        }
    }

    void silme() {
        if (isEmpty()) {
            System.out.println("Silinecek eleman yok");
        } else {
            System.out.println("Silindi: " + dizi[front]);
            // Elemanları sola kaydır
            for (int i = front + 1; i <= rear; i++) {
                dizi[i - 1] = dizi[i];
            }
            rear--;
        }
    }

    void yazdır() {
        if (isEmpty()) {
            System.out.println("Kuyruk boş.");
            return;
        }
        System.out.print("Kuyruktaki elemanlar: ");
        for (int i = front; i <= rear; i++) {
            System.out.print(dizi[i] + " ");
        }
        System.out.println();
    }

    boolean isFull() {
        return rear == size - 1;
    }

    boolean isEmpty() {
        return front > rear;
    }
}
