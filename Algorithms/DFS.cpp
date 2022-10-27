#include <bits/stdc++.h>
using namespace std;

// Solution for Connected Cells in a Grid Hackerrank

int visited[100][100];
int totArea;
int r, c, maxArea;

bool check(int x, int y){
    if(x<0 || x>=r || y<0 || y>=c) return false;
    return true;
}

void dfs(int x, int y, matrix){
    int dx[] = {1, 1, 0, -1, -1, -1, 0, 1};
    int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};

    totArea++;
    visited[x][y] = 1;
    for(int i=0; i<8; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(check(nx, ny) && matrix[nx][ny] == 1 && visited[nx][ny] == 0){
            dfs(nx, ny, matrix);
        }
    }
}

int connectedCell(vector<vector<int>> matrix){

    for(int i=0; i<r; i++){
        for(int j=0; j<c; j++){
            if(matrix[i][j] == 1 && visited[i][j] == 0){
                totArea = 0;
                dfs(i, j, matrix);
                if(totArea > maxArea) maxArea = totArea;
            }
        }
    }
    return maxArea;
}