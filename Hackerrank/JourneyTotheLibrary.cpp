#include <bits/stdc++.h>
using namespace std;

vector<bool> visited;
vector<vector<int>> matrix;
long vertices;

void dfs(int src, vector<vector<int>> &matrix, vector<bool> &visited){
    visited[src] = true;
    vertices++;
    for(int i=0; i<matrix.size(); i++){
        if(matrix[src][i] == 1 && visited[i] == false){
            dfs(i, matrix, visited);
        }
    }
}

int journeyToMoon(int n, vector<vector<int>> astronaut) {
    long result = n*(n-1)/2;
    visited = vector<bool>(n, false);
    for(int i=0; i<astronaut.size(); i++){
        matrix[astronaut[i][0]].push_back(astronaut[i][1]);
        matrix[astronaut[i][1]].push_back(astronaut[i][0]);
    }
    for(int i=0; i<matrix.size(); i++){
        if(visited[i] == false){
            vertices = 0;
            dfs(i, matrix, visited);
            result -= vertices*(vertices-1)/2;
        }
    }
    return result;
}
