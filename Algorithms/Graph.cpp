// Program to print BFS traversal from a given
// source vertex. BFS(int s) traverses vertices
// reachable from s.
#include<iostream>
#include <list>
#include <bits/stdc++.h>
using namespace std;

// This class represents a directed graph using
// adjacency list representation
class Graph
{
    map<int, bool> visited;
    int V;
	// Pointer to an array containing adjacency
	// lists
	map<int, list<int>> adj;
public:
	Graph(int V); // Constructor

	// function to add an edge to graph
	void addEdge(int v, int w);

	// prints BFS traversal from a given source s
	void BFS(int s);

    void DFS(int s);

	void DFSUtill(int s, bool VISITED []);

	void FillOrder(int s, bool VISITED[], stack<int> &stack);

	void PrintSCC();

	Graph getTranspose();
};

Graph::Graph(int V)
{
	this->V = V;
	// adj = new list<int>[V];
}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w); // Add w to v’s list.
}

void Graph::BFS(int s)
{

	// Create a queue for BFS
	list<int> queue;

	// Mark the current node as visited and enqueue it
	visited[s] = true;
	queue.push_back(s);

	// 'i' will be used to get all adjacent
	// vertices of a vertex
	list<int>::iterator i;

	while(!queue.empty())
	{
		// Dequeue a vertex from queue and print it
		s = queue.front();
		cout << s << " ";
		queue.pop_front();

		// Get all adjacent vertices of the dequeued
		// vertex s. If a adjacent has not been visited,
		// then mark it visited and enqueue it
		for (i = adj[s].begin(); i != adj[s].end(); ++i)
		{
			if (!visited[*i])
			{
				visited[*i] = true;
				queue.push_back(*i);
			}
		}
	}
}

void Graph::DFS(int s){
    visited[s] = true;
    cout<<s<<" ";

    list<int>::iterator i;
    for(i = adj[s].begin(); i != adj[s].end(); ++i){
        if(!visited[*i])
            DFS(*i);
    }
}

Graph Graph::getTranspose()
{
    Graph g(V);
    for (int v = 0; v < V; v++)
    {
        // Recur for all the vertices adjacent to this vertex
        list<int>::iterator i;
        for(i = adj[v].begin(); i != adj[v].end(); ++i)
        {
            g.adj[*i].push_back(v);
        }
    }
    return g;
}

void Graph::DFSUtill(int s, bool VISITED[]){
    VISITED[s] = true;
    cout<<s<<" ";

    list<int>::iterator i;
    for(i = adj[s].begin(); i != adj[s].end(); ++i){
        if(!VISITED[*i])
            DFSUtill(*i, VISITED);
    }
}

void Graph::FillOrder(int s, bool VISITED[], stack<int> &stack){
	VISITED[s] = true;

    list<int>::iterator i;
    for(i = adj[s].begin(); i != adj[s].end(); ++i){
        if(!VISITED[*i])
            FillOrder(*i, VISITED, stack);
    }
	stack.push(s);
}

void Graph::PrintSCC(){
	stack<int> Stack;
	bool * VISITED= new bool[V];
	for(int i=0; i<V; i++)
		VISITED[i] = false;
	for(int i=0; i<V; i++){
		if(VISITED[i]==false)
			FillOrder(i, VISITED, Stack);
	}

	Graph gr = getTranspose();

	for(int i=0; i<V; i++)
		VISITED[i] = false;

	while(!Stack.empty()){
		int v = Stack.top();
		Stack.pop();
		if (VISITED[v] == false){
            gr.DFSUtill(v, VISITED);
            cout << endl;
        }
    }
}

// Driver program to test methods of graph class
int main()
{
	// Create a graph given in the above diagram
	Graph g(5);
	g.addEdge(1, 0);
    g.addEdge(0, 2);
    g.addEdge(2, 1);
    g.addEdge(0, 3);
    g.addEdge(3, 4);

	g.PrintSCC();
    // cout<<endl;
	return 0;
}
