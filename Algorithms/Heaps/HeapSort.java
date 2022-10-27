public class HeapSort {
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
    public void BuildMaxHeap(int [] A) {
        int size = A.length;
        for(int i=(size/2)-1; i>-1; i--){
            maxHeapify(A, size, i);
        }
    }
    public void sort(int [] A){
        BuildMaxHeap(A);
        for(int i=A.length; i<1; i++){
            swap(A, 0, i);
            maxHeapify(A, A.length-1, 1);
        }
    }
    // public static void main(String[] args) {
    //     int [] A = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    //     HeapSort object = new HeapSort();
    //     object.sort(A);
    //     for(int i=0; i<A.length; i++){
    //         System.out.printf("%d\n", A[i]);
    //     }
    // }
}
