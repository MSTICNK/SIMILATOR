public class kuyruk_yapisi {
int [] dizi;
int size;
int front;
int rear;
public kuyruk_yapisi(int size){
    this.size =size;
    dizi = new int[size];
    front=0;
    rear=-1;
}


void ekleme(int data){
    if (isFull()){
        System.out.println("Kuyruk dolu.");
    }
    else{
    rear++;
    dizi[rear]=data;
    }
}
void silme(){
    if(isEmpty()){
        System.out.println("Kuyruk boş.");
    }
    else{
    int sayi = dizi[front];
    for(int i =1;i<=rear;i++){
        dizi[i-1]=dizi[i];
    }
    }
    rear--;

}
private boolean isFull(){
    return rear == size - 1;
}

private boolean isEmpty(){
    return rear ==size-1;
}
}
