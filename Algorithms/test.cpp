#include <bits/stdc++.h>
using namespace std;

// isPossible to convert (a, b) to (c, d) by performing the following operation:
// (a, b) -> (a, a+b) and (a, b) -> (a+b, b)
// return true if it is possible to convert (a, b) to (c, d) by performing above steps in any order zero or more times

bool isPossible(int a, int b, int c, int d){
    if(a==c && b==d) return true;
    if(a>c || b>d) return false;
    if(a==c) return isPossible(a, a+b, c, d);
    if(b==d) return isPossible(a+b, b, c, d);
    return isPossible(a+b, b, c, d) || isPossible(a, b+a, c, d);
}

int main(int argc, char const *argv[])
{
    int a, b, c, d;
    cin>> a >> b >> c >> d;
    if(isPossible(a, b, c, d)){
        cout<< "YES" << endl;
    }
    else{
        cout<< "NO" << endl;
    }
    return 0;
}