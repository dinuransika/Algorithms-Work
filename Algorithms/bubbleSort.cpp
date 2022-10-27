// Optimized implementation of Bubble sort
#include <bits/stdc++.h>
using namespace std;

// Function to print an array
void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout <<" "<< arr[i];
}

// An optimized version of Bubble Sort
void bubbleSort(int arr[], int n)
{
int i, j;
bool swapped = false;
for (i = 0; i < n-1 & !swapped; i++)
{
	swapped = true;
	for (j = 0; j < n-i-1; j++)
	{
		if (arr[j] > arr[j+1])
		{
		swap(arr[j], arr[j+1]);
		swapped = false;
		}
		printArray(arr, n);
		cout<<endl;
	}
}
}

float findMedian(float arr[]){
	int n = sizeof(arr)/sizeof(arr[0]);
	bool swapped = false;
	for (int i = 0; i < n-1 & !swapped; i++)
	{
		swapped = true;
		for (int j = 0; j < n-i-1; j++)
		{
			if (arr[j] > arr[j+1])
			{
			swap(arr[j], arr[j+1]);
			swapped = false;
			}
		}
	}
	if(n%2==0){
		return (arr[n/2]+arr[n/2-1])/2.0;
	}
	else{
		return arr[n/2];
	}
}


// Driver program to test above functions
int main()
{
	int arr[] = {5, 3, 1, 9, 8, 2, 4, 7};
	float arrf[] = {5, 3, 1, 9, 8, 2, 4};
	int N = sizeof(arr)/sizeof(arr[0]);
	bubbleSort(arr, N);
	cout <<"Sorted array: \n";
	printArray(arr, N);
	cout<<endl;
	cout<<"Median: "<<findMedian(arrf)<<endl;
	return 0;
}

