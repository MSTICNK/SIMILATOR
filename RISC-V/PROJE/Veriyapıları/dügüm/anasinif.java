public class anasinif {
    Node head = null;
    Node tail = null;

    void yazdir() {
        if (head == null) {
            System.out.println("Liste Boş.");
        } else {
            Node temp = head; 
            System.out.print("Liste: ");
            while (temp != null) {
                System.out.print(temp.data + " ");
                temp = temp.next;
            }
            System.out.println(); 
        }
    }

    void basaekle(int x){
        Node eleman =new Node();
        eleman.data=x;

        if(head==null){
            eleman.next=null;
            head=eleman;
            tail=eleman;
            System.out.println("Liste oluşturuldu , ilk eleman eklendi.");
        }
        else{
            eleman.next=head;
            head=eleman;
            System.out.println("Eleman başa eklendi.");
        }

    }

    void sonaekle(int x){
        Node eleman = new Node();
        eleman.data=x;

        if(head==null){
            eleman.next=null;
            head=eleman;
            tail=eleman;
            System.out.println("Liste oluşturuldu, ilk eleman eklendi");
        }
        else{
            tail.next=eleman;
            eleman.next=null;
            tail=eleman;
            System.out.println("Listenin sonuna istenilen eleman eklendi.");
        }

    }

    void arayaekle(int x, int indeks) {
        Node eleman = new Node();
        eleman.data = x;
    
        if (head == null) {
            eleman.next = null;
            head = eleman;
            tail = eleman;
            System.out.println("Liste oluşturuldu, ilk eleman eklendi.");
        }
        else if (indeks == 0) {
            eleman.next = head;
            head = eleman;
            System.out.println("Eleman başa eklendi.");
        }
        else {
            Node temp = head;  
            int i = 0;
    
            while (temp != null && i < indeks - 1) {
                temp = temp.next;
                i++;
            }
    
            if (temp != null) {
                eleman.next = temp.next;
                temp.next = eleman;
    
                if (eleman.next == null) {
                    tail = eleman;
                }
    
                System.out.println(indeks + ". sıraya eleman eklendi.");
            } else {
                System.out.println("Geçersiz indeks.");
            }
        }
    }
    
    void bastansil(){
        if (head==null){
            System.out.println("Liste yapısı boş , silinecek eleman bulunamadı.");
        }
        else if(head==tail){
            head=null;
            tail=null;
            System.out.println("Liste boşaltıldı.");
        }
        else{
            head=head.next;
            System.out.println("Baştaki eleman silindi.");
        }
    }

    void sondansil(){
        if (head==null){
            System.out.println("Liste yapısı boş,silinecek eleman bulunamadı.");
        }
        else if (head==tail){
            head=null;
            tail=null;
            System.out.println("Liste Boşaltıldı.");
        }
        else{
            Node temp = head;
            Node temp2 = null;
            while(temp.next!=null){
                temp2=temp;
                temp=temp.next;
            }
            temp2.next=null;
            tail=temp2;
        }

    }

    void aradansil(int indeks) {
        if (head == null) {
            System.out.println("Liste yapısı boş, silinecek eleman bulunamadı.");
        } else if (head == tail) {
            head = null;
            tail = null;
            System.out.println("Liste Boşaltıldı.");
        } else {
            Node temp = head;
            Node temp2 = null;
            int i = 0;
    
            // Eğer silinecek indeks baştaysa
            if (indeks == 0) {
                head = head.next;
                System.out.println("Baştaki eleman silindi.");
                return;
            }
    
            // Belirtilen indekse kadar ilerliyoruz
            while (temp != null && i < indeks) {
                temp2 = temp;
                temp = temp.next;
                i++;
            }
    
            // Eğer temp null ise, indeks geçersiz
            if (temp == null) {
                System.out.println("Geçersiz Indeks");
            } else {
                temp2.next = temp.next; // temp'yi siliyoruz
                if (temp.next == null) {
                    tail = temp2; // Eğer son eleman silindiyse, tail güncelleniyor
                }
                System.out.println(indeks + ". sıradaki eleman silindi.");
            }
        }
    }
    
}
        
    

