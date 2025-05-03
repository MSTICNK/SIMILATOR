public class kuyruk_yapisi {
    int dizi[];
    int front;
    int rear;
    int size;

    public kuyruk_yapisi(int size){
        this.size = size;
        dizi = new int[size];
        front = 0;
        rear = -1;
    }

    void ekle(int x){
        if (rear == size - 1) {
            System.out.println("Kuyruk dolu, ekleme yapılamaz.");
            return;
        }
        rear++;
        dizi[rear] = x;
        System.out.println("Eklendi: " + x);
    }
    void cikar() {
        if (front > rear) {
            System.out.println("Kuyruk boş, çıkarma yapılamaz.");
            return;
        }
    
        System.out.println("Çıkarıldı: " + dizi[front]);
        front++;
    
        if (front > rear) {
            front = 0;
            rear = -1;
        }
    }
    
    

    
    void yazdir() {
        if (rear < front) {
            System.out.println("Kuyruk yapısı boş");
            return;
        }
    
        System.out.print("Kuyruk: ");
        for (int i = front; i <= rear; i++) {
            System.out.print(dizi[i] + " ");
        }
        System.out.println();
    }
    

}
