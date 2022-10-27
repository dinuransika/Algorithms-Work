#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll minKey(vector<ll> key, vector<bool> mstSet, ll V){
    ll min = LONG_LONG_MAX;
    ll min_index;

    for(ll v=0; v<V; v++){
        if(mstSet[v]==false && key[v]<min){
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

void printMST(vector<ll> parent, ll V, vector<vector<ll> > &graph){
    for(ll i=0; i<V; i++)
        printf("%lld - %lld %lld \n", parent[i], i, graph[i][parent[i]]);
    ll  sm=0;
    for(ll i=1; i<V; i++){
        sm+=graph[i][parent[i]];
    }
    cout<< sm << endl;            
}

void primMST(vector<vector<ll>> &graph, ll V){
    vector<ll> parent;
    vector<ll> key;
    vector<bool> mstSet;

    for(ll i=0; i<V; i++)
        key.push_back(LONG_LONG_MAX), mstSet.push_back(false), parent.push_back(0);

    key[0] = 0, parent[0] = -1;

    for(ll i=0; i<V; i++){
        ll u = minKey(key, mstSet, V);

        mstSet[u] = true;

        for(ll v=0; v<V; v++){
            if(graph[u][v] && !mstSet[v] && graph[u][v] < key[v])
                parent[v] = u, key[v] = graph[u][v];
        }
    }
    printMST(parent, V, graph);
}

int main(int argc, char const *argv[])
{
    ll n, m;
    cin>> n >> m;

    vector<vector<ll>> graph;

    for(ll i=0; i<n; i++){
        vector<ll> temp;
        for(ll k=0; k<m; k++)
            temp.push_back(0);
        graph.push_back(temp);
    }
    for(ll i=0; i<m; i++){
        ll x, y, r;
        cin >> x >> y >> r;
        graph[x-1][y-1] = r;
        graph[y-1][x-1] = r;
    }

    primMST(graph, n);
    return 0;
}
