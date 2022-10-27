#include <bits/stdc++.h>
using namespace std;

int LCS_Length(char* X, char* Y){
    int m = strlen(X);
    int n = strlen(Y);
    int c[m+1][n+1];
    for(int i=1; i<m+1; i++)
        c[i][0] = 0;
    for(int j=1; j<n+1; j++)
        c[0][j] = 0;
    for(int i=1; i<m+1; i++){
        for(int j=1; j<n+1; j++){
            if(X[i+1]==Y[j+1])
                c[i][j] = c[i-1][j-1]+1;
            else
                c[i][j] = max(c[i-1][j], c[i][j-1]);            
        }
    }
    return c[m][n];
}


int main(int argc, char const *argv[])
{
    char X[] = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"; 
    char Y[] = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"; 
      
    cout << "Length of LCS is " 
         << LCS_Length( X, Y)<<endl;
    return 0;
}
