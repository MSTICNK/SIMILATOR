public class Anasinif {
Node head = null;
Node tail=null;

void yazdir(){
if ( head == null){
    System.out.println("liste boş");
}
else{
Node temp = head;
while(temp !=null){
    System.out.println(temp.data + "");
}

}
}

void basaekle(int x){
Node eleman = new Node();
eleman.data=x;
if(head==null){
    eleman.next=null;
    head=eleman;
    tail=eleman;
}

}
}






