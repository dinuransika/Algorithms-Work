#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll power_rec(ll a, ll k){
    if (k==1)
        return a;
    ll j = power_rec(a, k/2);
    if(k%2)
        return j * j * a;
    else
        return j*j;
}

ll power_rec_tail(ll a, ll k){
    if (k==1)
        return a;
    if(k%2)
        return power_rec_tail(a, k/2) * power_rec_tail(a, k/2) * a;
    else
        return power_rec_tail(a, k/2) * power_rec_tail(a, k/2);
}

int main(int argc, char const *argv[])
{
    // measure time for each funciton
    clock_t start, end;
    double cpu_time_used;
    start = clock();
    cout << power_rec(2, 20) << endl;
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    cout << "Time taken by function 1: " << cpu_time_used << endl;
    start = clock();
    cout << power_rec_tail(2, 20) << endl;
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    cout << "Time taken by function 2: " << cpu_time_used << endl;
    return 0;
}
