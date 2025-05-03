package düğüm_oluşturma_cift;
public class Liste_Yapisi {
Node head =null;
Node tail = null;

void yazdir() {
    if (head == null) {
        System.out.println("Liste boş.");
    } else {
        Node temp = head;
        while (temp != null) {
            System.out.println(temp.data + " ");
            temp = temp.next;
        }
        System.out.println(); // Yeni satıra geçmek için
    }
}


void basaekle(int x){
    Node eleman = new Node();
    eleman.data = x;
    eleman.prev=null;
    if(head==null){
        eleman.next=null;
        head = eleman;
        tail=eleman;
    System.out.println("Liste yapısı oluştruldu , ilk eleman eklendi.");
    }
else {
    eleman.next = head;
    head.prev=eleman;
    head = eleman;
    System.out.println("Eleman başa eklendi");
}
}

void sonaekle(int x){
   Node eleman = new Node();
   eleman.data = x;
   eleman.next=null;
   if(head == null){
    eleman.prev=null;
    eleman.next=null;
    head=eleman;
    tail=eleman;
    System.out.println("Liste yapısı oluşturuldu,ilk eleman eklendi.");
   }
   else{
    eleman.prev=tail;
    eleman.next=null;
    tail.next=eleman;
    tail = eleman;
    System.out.println("Sona eleman eklendi");
   }

}

void arayaekle(int x, int indis) {
    Node eleman = new Node();
    eleman.data = x;

    // Eğer liste boşsa
    if (head == null && indis == 0) {
        head = tail = eleman;
        System.out.println("Liste yapısı oluşturuldu, ilk eleman eklendi.");
    } 
    // Eğer başa eklemek istiyorsak
    else if (indis == 0) {
        eleman.next = head;
        head.prev = eleman; // başı işaret eden prev bağlantısı
        head = eleman; // başa ekliyoruz
        System.out.println("Liste başına eleman eklendi.");
    } 
    // Eğer sondan önce eklemek istiyorsak
    else {
        Node temp = head;
        int n = 0;

        // İlgili indise kadar git
        while (temp != null && n < indis) {
            temp = temp.next;
            n++;
        }

        // Eğer geçerli indis bulunduysa
        if (temp != null) {
            // Önceki elemanı ve sonraki elemanı birbirine bağla
            eleman.prev = temp.prev;
            eleman.next = temp;

            // Önceki elemanın next'ini yeni elemana ayarla
            if (temp.prev != null) {
                temp.prev.next = eleman;
            }

            // Sonraki elemanın prev'ini yeni elemana ayarla
            if (temp != null) {
                temp.prev = eleman;
            }

            // Eğer sondaki eleman ekleniyorsa, tail'i güncelle
            if (temp == tail) {
                tail = eleman;
            }

            System.out.println(indis + ". sıraya yeni eleman eklendi.");
        } else {
            System.out.println("Geçerli bir indis bulunamadı.");
        }
    }
}








void bastansil(){

    if (head==null){
        System.out.println("Liste boş , silinecek eleman yok");
    }
    else if(head.next==null){

        head=null;
        tail=null;
        System.out.println("Listede kalan son eleman silindi");
    }
    else{
        head = head.next;
        head.prev=null;
        System.out.println("Baştaki eleman silindi.");
    }
}

void sondansil() {
    if (head == null) {
        System.out.println("Liste boş, silinecek eleman yok");
    } else if (head.next == null) {
        // Liste sadece 1 elemandan oluşuyorsa
        head = null;
        tail = null;
        System.out.println("Listede kalan son eleman silindi");
    } else {
        // Liste 2 ya da daha fazla elemandan oluşuyorsa
        Node temp = head;
        
        // Sonraki elemanlara geçmek için döngü
        while (temp.next != null) {
            temp = temp.next;
        }

        // Sondaki elemanı silmek için, prev bağlantısını düzenle
        if (temp.prev != null) {
            temp.prev.next = null; // son elemanı sil
        }
        
        tail = temp.prev; // son elemanı silince, tail'i önceki elemana ayarla
        System.out.println("Sondan eleman silindi");
    }
}


void aradansil(int indis){

    if(head==null){
        System.out.println("Liste boş, silinecek eleman yok");
    }
    else if(head.next==null){
        head=null;
        tail=null;
        System.out.println("Listede kalan son eleman silindi");
    }
    else if(head.next!=null && indis ==0){
        head=head.next;
        head.prev=null;
        System.out.println("Baştaki eleman silindi");
    }

    else {
        int n=0;
        Node temp = head;
        while(temp.next!=null){
            n++;
            temp=temp.next;
        }
        if (temp != null) {
            if (temp.next != null) {
                temp.next.prev = temp.prev; // sonraki elemanın prev'ini düzelt
            }
            if (temp.prev != null) {
                temp.prev.next = temp.next; // önceki elemanın next'ini düzelt
            }

            if (temp == tail) { // Eğer sondaki eleman siliniyorsa
                tail = temp.prev;
            }

            System.out.println(indis + ". sıradaki eleman silindi.");
        } 
        else{
            System.out.println("Geçerli bir indis bulunamadı.");
        }
    }
}
}

        
    




