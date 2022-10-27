#include <bits/stdc++.h>
using namespace std;

vector<bool> visited;

int dfs(vector<vector<int>> &matrix, int src, vector<bool> &visited){
    visited[src] = true;
    int count = 1;
    for(int i=0; i<matrix.size(); i++){
        if(!visited[i]){
            count += dfs(matrix, i, visited);
        }
    }
    return count;
}

long roadsAndLibraries(int n, int c_lib, int c_road, vector<vector<int>> cities) {
    vector<vector<int>> matrix(n+1);
    for(int i=0; i<cities.size(); i++){
        matrix[cities[i][0]].push_back(cities[i][1]);
        matrix[cities[i][1]].push_back(cities[i][0]);
    }
    visited = vector<bool>(n+1, false);
    vector<int> counts;
    for(int i=1; i<=n; i++){
        if(matrix[i].size()>0 && !visited[i]){
            counts.push_back(dfs(matrix, i, visited));
        }else if(matrix[i].size()==0){
            counts.push_back(1);
        }
    }
    long long int ans = 0;
    for(int i=0; i<counts.size(); i++){
        ans += min((counts[i]-1)*c_road + c_lib, c_lib*counts[i]);
    }
    return ans;
}