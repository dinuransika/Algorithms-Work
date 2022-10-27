#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

class Edge{
    public:
    ll src, dest, weight;
};

class Graph{
    public:
    ll V, E;

    vector<Edge> edges;
    Graph(ll, ll);
};

Graph::Graph(ll V, ll E){
    this->V = V;
    this->E = E;
    this->edges.resize(E);
};

class subset{
    public:
    ll parent;
    ll rank;
};


ll find(subset subsets[], ll i){
    if(subsets[i].parent != i)
        subsets[i].parent = find(subsets, subsets[i].parent);
    return subsets[i].parent;
};

void Union(subset subsets[], int x, int y){
    ll xroot = find(subsets, x);
    ll yroot =  find(subsets, y);

    if(subsets[xroot].rank < subsets[yroot].rank)
        subsets[xroot].parent = yroot;
    else if(subsets[xroot].rank > subsets[yroot].rank)
        subsets[yroot].parent = xroot;
    else
    {
        subsets[yroot].parent = xroot;
        subsets[xroot].rank++;
    }
}

ll mycomp(const Edge &a, const Edge &b){
    return a.weight<b.weight;
}

ll KruskalMST(Graph graph){
    ll V = graph.V;
    Edge results[V];
    ll e = 0;
    ll i = 0;

    sort(graph.edges.begin(), graph.edges.end(), mycomp);
    subset subsets[V];
    for(ll v=0; v<V; v++){
        subsets[v].parent = v;
        subsets[v].rank = 0;
    }

    while(e<V-1){
        Edge next_edge  = graph.edges[i++];

        int x = find(subsets, next_edge.src);
        int y = find(subsets, next_edge.dest);

        if(x!=y){
            results[e++] = next_edge;
            Union(subsets, x, y);
        }
    }
    ll sm = 0;
    for (i = 0; i < e; ++i) {
        sm += results[i].weight;
        // printf("%lld %lld\n", results[i].src, results[i].dest);
    }
    return sm;

}

int main() {
    ios_base::sync_with_stdio(false);
    ll V, E;
    cin >> V >> E;
    Graph graph(V, E);
    for (ll j = 0; j < E; j++) {
        ll s, d, w;
        cin >> s >> d >> w;
        Edge edge;
        edge.src = s;
        edge.dest = d;
        edge.weight = w;
        edge.src = d;
        edge.dest = s;
        edge.weight = w;
        graph.edges.push_back(edge);
    }


    // ll V = 4; // Number of vertices in graph
    // ll E = 5; // Number of edges in graph
    // Graph graph(V, E);
 
    // // add edge 0-1
    // graph.edges[0].src = 0;
    // graph.edges[0].dest = 1;
    // graph.edges[0].weight = 10;
 
    // // add edge 0-2
    // graph.edges[1].src = 0;
    // graph.edges[1].dest = 2;
    // graph.edges[1].weight = 6;
 
    // // add edge 0-3
    // graph.edges[2].src = 0;
    // graph.edges[2].dest = 3;
    // graph.edges[2].weight = 5;
 
    // // add edge 1-3
    // graph.edges[3].src = 1;
    // graph.edges[3].dest = 3;
    // graph.edges[3].weight = 15;
 
    // // add edge 2-3
    // graph.edges[4].src = 2;
    // graph.edges[4].dest = 3;
    // graph.edges[4].weight = 4;
 
   
    // Function call
    // KruskalMST(graph);
    cout << KruskalMST(graph) << endl << endl;
    return 0;
}