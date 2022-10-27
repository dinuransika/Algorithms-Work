public class sort {
    static void selection_Sort(int[] arr){
        for(int i = 0; i < arr.length - 1; i++){
            int min = i;
            for(int j=i+1; j < arr.length; j++){
                if(arr[j]<arr[min]) min = j;
            }
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
    }

    static void insertion_sort(int [] arr){
        // for(int i=0; i<arr.length - 1; i++){
        //     int key = arr[i+1];
        //     for(int j=i+1; j>0; j--){
        //         if(arr[j-1]>key){
        //             int temp = arr[j-1];
        //             arr[j-1] = arr[j];
        //             arr[j] = temp;
        //         }
        //     }
        //     // print_arr(arr);
        // }
        for(int j = 1; j<arr.length; j++){
            int key = arr[j];
            int i = j-1;
            while(i>=0 && arr[i]>key){
                arr[i+1] = arr[i];
                i--;
            }
            arr[i+1] = key;
            print_arr(arr);
        }
    }
    
    static void print_arr(int [] arr){
        for(int i=0; i<arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println(' ');
    }
    public static void main(String[] args) {
        int arr[] = {5, 2, 4, 6, 1, 3};
        // selection_Sort(arr);
        insertion_sort(arr);
        print_arr(arr);
    }
}