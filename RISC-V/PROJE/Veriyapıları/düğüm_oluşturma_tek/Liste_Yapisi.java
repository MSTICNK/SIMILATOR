package düğüm_oluşturma;
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
        System.out.println(); 
    }
}

void basaekle(int x){
    Node eleman = new Node();
    eleman.data = x;
    if(head==null){
        eleman.next=null;
        head = eleman;
        tail=eleman;
    System.out.println("Liste yapısı oluştruldu , ilk eleman eklendi.");
    }
else {
    eleman.next = head;
    head = eleman;
    System.out.println("Eleman başa eklendi");
}
}

void sonaekle(int x){
   Node eleman = new Node();
   eleman.data = x;
   if(head == null){
    eleman.next=null;
    head=eleman;
    tail=eleman;
    System.out.println("Liste yapısı oluşturuldu,ilk eleman eklendi.");
   }
   else{
    eleman.next=null;
    tail.next=eleman;
    tail = eleman;
    System.out.println("Sona eleman eklendi");
   }

}

void arayaekle(int x, int indis){
    Node eleman = new Node();
    eleman.data=x;

    if(head==null && indis== 0){
        eleman.next=null;
        head=eleman;
        tail=eleman;
        System.out.println("Liste yapısı oluşturuldu, ilk eleman eklendi");
    }
    else if(head != null && indis==0){
        eleman.next = head;
        head =eleman;
        System.out.println("Liste başına eleman eklendi");
    }
    else{
        int n = 0;
        Node temp = head;
        Node temp2 =head;

        while(temp.next !=null)
        {
            n++;
            temp = temp.next;
        }
        if(n==indis){
            temp2.next=eleman;
            eleman.next=temp;
            System.out.println("eleman eklendi.");
        }
        else{
            temp=head;
            temp2=head;
            int i=0;
            while(i<indis){
                temp2 = temp;
                temp=temp.next;
                i++;
            }
            temp2.next=eleman;
            eleman.next=temp;
            System.out.println(indis+". sıraya yeni eleman eklendi.");
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
        System.out.println("Baştaki eleman silindi.");
    }
}

void sondansil(){

    if(head==null){
        System.out.println("Liste boş, silinecek eleman yok");
    }
    else if(head.next==null){
        head=null;
        tail=null;
        System.out.println("Listede kalan son eleman silindi");
    }
    else{
        Node temp = head;
        Node temp2 =head;

        while(temp.next!=null){
            temp2=temp;
            temp=temp.next;
        }
        temp2.next=null;
        tail=temp2;
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
        System.out.println("Baştaki eleman silindi");
    }

    else {
        int n=0;
        Node temp = head;
        Node temp2 =head;

        while(temp.next!=null){
            n++;
            temp2=temp;
            temp=temp.next;
        }
        if(n==indis){
            temp2.next=null;
            tail=temp2;
            System.out.println("Sondan eleman silindi");
        }
        else{
            temp =head;
            temp2=head;
            int j=0;
            while(j!=indis){
                temp2=temp;
                temp=temp.next;
                j++;
            }
            temp2.next=temp.next;
            System.out.println("Aradaki eleman çizildi.");

        }
    }

}

}
