#include <bits/stdc++.h>
using namespace std;
#include <chrono>
using namespace std::chrono;

int CutRod(int p[], int n){
    if(n==0)
        return 0;
    int q = INT_MIN;
    for(int i=1; i<n+1; i++){
        q = max(q, p[i-1]+CutRod(p, n-i));
    }
    return q;
}
int MemorizedCutRodAux(int p[], int n, int r[]){
    if(r[n]>=0)
        return r[n];
    int q;
    if(n==0)
        q=0;
    else
    {
        q = INT_MIN;
        for(int i=1; i<n+1; i++)
            q = max(q, p[i-1]+MemorizedCutRodAux(p, n-i, r));
    }
    r[n] = q;
    return q; 
}

int MemorizedCutRod(int p[], int n){
    int r[n];
    for(int i=0; i<n+1; i++)
        r[i] = INT_MIN;
    return MemorizedCutRodAux(p, n, r);
}

int BottumUpCutRod(int p[], int n){
    int r[n], q;
    r[0] = 0;
    for(int j=1; j<=n; j++){
        q = INT_MIN;
        for(int i=1; i<=j; i++)
            q = max(q, p[i-1]+r[j-i]);
        r[j] = q;
    }
    return r[n];
}

void ExtendedBottumUpCutRod(int p[], int n, int r[], int s[]){
    r[0] = 0;
    s[0] = 0;
    int q;
    for(int j=1; j<=n; j++){
        q = INT_MIN;
        for(int i=1; i<=n; i++){
            if(q<p[i]+r[j-i-1]){
                q = p[i]+r[j-i-1];
                s[j] = i;
            }
        }
        r[j] = q;
    }
}

void PrintCutRodSol(int p[], int n){
    int r[n+1], s[n+1];
    ExtendedBottumUpCutRod(p, n, r, s);
    while(n>0){
        cout<<s[n]<<" ";
        n = n - s[n-1];
    }
    cout<<endl;
}

int main(int argc, char const *argv[])
{
    auto start = high_resolution_clock::now();
    int p[] = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
    // cout<<BottumUpCutRod(p, 10)<<endl;

    PrintCutRodSol(p, 10);


    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Time Elapsed :" << duration.count() << endl;
    return 0;
}


