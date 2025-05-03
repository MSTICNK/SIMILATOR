package dügüm_d;

public class anasinif {
        Node head = null;
        Node tail = null;
    
        void yazdir() {
            if (head == null) {
                System.out.println("Liste Boş.");
            } else {
                Node temp = head;
                System.out.print("Liste: ");
                do {
                    System.out.print(temp.data + " ");
                    temp = temp.next;
                } while (temp != head); // Başa geri dönene kadar devam et
                System.out.println();
            }
        }
    
        void basaekle(int x) {
            Node eleman = new Node();
    
            if (head == null) {
                head = eleman;
                tail = eleman;
                head.next = head;
                head.prev = head;
                System.out.println("Liste oluşturuldu, ilk eleman eklendi.");
            } else {
                eleman.next = head;
                eleman.prev = tail;
                head.prev = eleman;
                tail.next = eleman;
                head = eleman;
                System.out.println("Eleman başa eklendi.");
            }
        }
    
        void sonaekle(int x) {
            Node eleman = new Node();
    
            if (head == null) {
                head = eleman;
                tail = eleman;
                head.next = head;
                head.prev = head;
                System.out.println("Liste oluşturuldu, ilk eleman eklendi.");
            } else {
                eleman.next = head;
                eleman.prev = tail;
                tail.next = eleman;
                head.prev = eleman;
                tail = eleman;
                System.out.println("Listenin sonuna istenilen eleman eklendi.");
            }
        }
    
        void arayaekle(int x, int indeks) {
            Node eleman = new Node();
    
            if (head == null) {
                head = eleman;
                tail = eleman;
                head.next = head;
                head.prev = head;
                System.out.println("Liste oluşturuldu, ilk eleman eklendi.");
            } else if (indeks == 0) {
                eleman.next = head;
                eleman.prev = tail;
                head.prev = eleman;
                tail.next = eleman;
                head = eleman;
                System.out.println("Eleman başa eklendi.");
            } else {
                Node temp = head;
                int i = 0;
    
                while (temp != null && i < indeks - 1) {
                    temp = temp.next;
                    i++;
                }
    
                if (temp != null) {
                    eleman.next = temp.next;
                    eleman.prev = temp;
                    if (temp.next != null) {
                        temp.next.prev = eleman;
                    }
                    temp.next = eleman;
    
                    if (eleman.next == head) {
                        tail = eleman; // tail güncelleniyor
                    }
    
                    System.out.println(indeks + ". sıraya eleman eklendi.");
                } else {
                    System.out.println("Geçersiz indeks.");
                }
            }
        }
    
        void bastansil() {
            if (head == null) {
                System.out.println("Liste yapısı boş, silinecek eleman bulunamadı.");
            } else if (head == tail) {
                head = null;
                tail = null;
                System.out.println("Liste boşaltıldı.");
            } else {
                head = head.next;
                head.prev = tail;
                tail.next = head;
                System.out.println("Baştaki eleman silindi.");
            }
        }
    
        void sondansil() {
            if (head == null) {
                System.out.println("Liste yapısı boş, silinecek eleman bulunamadı.");
            } else if (head == tail) {
                head = null;
                tail = null;
                System.out.println("Liste boşaltıldı.");
            } else {
                tail = tail.prev;
                tail.next = head;
                head.prev = tail;
                System.out.println("Listenin sonundaki eleman silindi.");
            }
        }
    
        void aradansil(int indeks) {
            if (head == null) {
                System.out.println("Liste yapısı boş, silinecek eleman bulunamadı.");
            } else if (head == tail) {
                head = null;
                tail = null;
                System.out.println("Liste boşaltıldı.");
            } else {
                Node temp = head;
                int i = 0;
    
                if (indeks == 0) {
                    bastansil();
                    return;
                }
    
                while (temp != null && i < indeks) {
                    temp = temp.next;
                    i++;
                }
    
                if (temp == null) {
                    System.out.println("Geçersiz indeks.");
                } else {
                    temp.prev.next = temp.next;
                    if (temp.next != null) {
                        temp.next.prev = temp.prev;
                    }
                    if (temp == tail) {
                        tail = temp.prev;
                    }
                    System.out.println(indeks + ". sıradaki eleman silindi.");
                }
            }
        }
    }
    

