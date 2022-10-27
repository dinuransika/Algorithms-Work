import java.util.Arrays;

public class Priority_queues {

    public int Parent(int i) {
        return ((i+1)/2)-1;
    }
    public int Left(int i) {
        return 2*(i+1)-1;
    }
    public int Right(int i) {
        return 2*(i+1);
    }
    public void swap(int A [], int first, int second){
        int temp = A[first];
        A[first] = A[second];
        A[second] = temp;
    }
    public void maxHeapify(int [] A,int n, int i) {
        int r = Right(i);
        int l = Left(i);
        int largest;
        if(l<n && A[l]>A[i]){
            largest = l;
        }else{largest=i;}
        if(r<n && A[r]>A[largest]){
            largest=r;
        }
        if(largest!=i){
            swap(A, largest, i);
            maxHeapify(A, n, largest);
        }
    }
    public int HeapMaximum(int []A) {
        return A[0];
    }
    public int HeapExtractMax(int []A) {
        if (A.length<1){
            return 0;
        }
        int max = A[0];
        A[0] = A[A.length-1];
        maxHeapify(A, A.length-1, 0);
        return max;
    }
    public void HeapIncreaseKey(int []A, int i, int key) {
        if (key>A[i]){
            A[i] = key;
            while(i>0 && A[Parent(i)]<A[i]){
                swap(A, i, Parent(i));
                i = Parent(i);
            }
        }
    }
    public void MaxHeapInsert(int []A, int key) {
        A = Arrays.copyOf(A, A.length+1);
        A[A.length-1] = Integer.MIN_VALUE;
        HeapIncreaseKey(A, A.length-1, key);
    }
    public void BuildMaxHeap(int [] A) {
        int size = A.length;
        for(int i=(size/2)-1; i>-1; i--){
            maxHeapify(A, size, i);
        }
    }
    public static void main(String[] args) {
        int [] A = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
        Priority_queues object = new Priority_queues();
        object.BuildMaxHeap(A);
        object.MaxHeapInsert(A, 15);
        System.out.println(object.HeapExtractMax(A));
        for(int i=0; i<A.length; i++){
            System.out.printf("%d\n", A[i]);
        }
    }
}