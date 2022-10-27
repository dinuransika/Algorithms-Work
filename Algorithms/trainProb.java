public class trainProb {

    // There are N stations on a train route numbered from 0 to N-1. The ticket cost between two stations (say i, j) is
    // given in a global, two dimensional matrix called cost. The ticket cost between two stations can be represented
    // by cost[i][j]. Further, the train travels only in one direction from station 0 to N-1.
    // Your task is to implement a function called int minCost(int fromStation, int toStation) which returns the
    // minimum possible cost to travel between given two stations.
    public int [][] cost = {{0, 1, 2, 3, 4},
                           {1, 0, 3, 2, 5},
                           {2, 3, 0, 1, 6},
                           {3, 2, 1, 0, 7},
                           {4, 5, 6, 7, 0}};
    // using dijs algorithm to find the minimum cost to travel between two stations
    public int minCost(int fromStation, int toStation) {
        int [][] cost = this.cost;
        int N = cost.length;
        int [] dist = new int[N];
        int [] prev = new int[N];
        for (int i = 0; i < N; i++) {
            dist[i] = Integer.MAX_VALUE;
            prev[i] = -1;
        }
        dist[fromStation] = 0;
        for (int i = 0; i < N; i++) {
            int u = -1;
            for (int j = 0; j < N; j++) {
                if (dist[j] < dist[u]) {
                    u = j;
                }
            }
            if (u == -1) {
                break;
            }
            for (int v = 0; v < N; v++) {
                if (dist[u] + cost[u][v] < dist[v]) {
                    dist[v] = dist[u] + cost[u][v];
                    prev[v] = u;
                }
            }
        }
        int minCost = dist[toStation];
        return minCost;
    }
}