/**
 * Heap
 */
public class Heap {
    private int[] Heap;
    private int size;
    private int maxsize;
  
    // Constructor to initialize an
    // empty max heap with given maximum
    // capacity.
    public void MaxHeap(int maxsize){
        this.maxsize = maxsize;
        this.size = 0;
        Heap = new int[this.maxsize + 1];
        Heap[0] = Integer.MAX_VALUE;
    }
    public int Parent(int i) {
        return ((i+1)/2)-1;
    }
    public int Left(int i) {
        return 2*(i+1)-1;
    }
    public int Right(int i) {
        return 2*(i+1);
    }
    public void maxHeapify(int [] A, int i) {
        Heap = A;
        int r = Right(i);
        int l = Left(i);
        int largest;
        if(l<size && Heap[l]>Heap[i]){
            largest = l;
        }else{largest=i;}
        if(r<size && A[r]>A[largest]){
            largest=r;
        }
        if(largest!=i){
            int temp = Heap[largest];
            Heap[largest] = Heap[i];
            Heap[i] = temp;
            maxHeapify(Heap, largest);
        }
    }
    public void BuildMaxHeap(int [] A) {
        size = A.length;
        for(int i=(size/2)-1; i>-1; i--){
            maxHeapify(A, i);
        }
    }
    // public static void main(String[] args) {
    //     int [] A = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    //     Heap h = new Heap();
    //     h.MaxHeap(11);
    //     h.BuildMaxHeap(A);
    //     for(int i=0; i<A.length; i++){
    //         System.out.printf("%d\n", h.Heap[i]);
    //     }
    // }
}