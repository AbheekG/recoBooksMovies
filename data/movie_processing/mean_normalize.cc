#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;

//Please note the file names have been change, these are present just
//for refernce.

int num_movies() {
    ifstream file("mLarge/movies.csv", ios::in);
    if (!file) {
        std::cerr << "Could not create output file\n";
    }
    map<int,int> x;
    int id = 0;
    char s[1000];
    file.getline(s,1000);
    while(!file.eof()) {
        if(id % 50 == 0) cout << "Done movie no:" << id << endl;
        file.getline(s,1000);
        //cout << s << endl;
        if('0' <= s[0] && s[0] <= '9') {
            id = strtol(s,NULL,0);
        } else {
            continue;
        }
    }
    id++;
    file.close();
    return id;
} 

void process_ratings(int x) {
    ifstream in("mLarge/ratings.csv", ios::in); // Obsolete
    ofstream out("mLarge/ratings_normalized.csv", ios::out);

    if (!in || !out) {
        std::cerr << "Could not create output file\n";
    }

    double A[x];
    int B[x];
    memset(A, 0, sizeof A);
    memset(B, 0, sizeof B);
    char s[200];
    in.getline(s,200);
    int it = 1;

    while(!in.eof()) {
        if(it % 50000 == 0) cout << "Done rating no:" << it << endl;
        it++;
        in.getline(s,200);
    	if('0' > s[0] || s[0] > '9') continue;
        char *a;
        strtol(s, &a, 0);
        int k = strtol(a+1, &a, 0);
        B[k]++;
        A[k] += (strtod(a+1,NULL) - A[k])/(B[k]);
    }

    in.clear();
    in.seekg(0, ios::beg);

    it = 0;

    while(!in.eof()) {
        if(it % 50000 == 0) cout << "Done rating no:" << it << endl;
        it++;
        in.getline(s,200);
    	if('0' > s[0] || s[0] > '9') continue;
        char *a;
        int p = strtol(s, &a, 0);
        int q = strtol(a+1, &a, 0);
        out <<p<<","<<q<<","<< strtod(a+1,NULL) - A[q] << endl;
    }
    in.close();
    out.close();

    out.open("mLarge/means.csv", ios::out);
    for(int i=0; i<x; ++i) out << A[i] << ",";
}

int main() {
    cout << "Getting number of movies\n";
    int x = num_movies();
    //for(map<int,int>::iterator i = x.begin(); i != x.end(); ++i) {cout << i->first << " " << i->second << endl; } cout << "Processing ratings\n";
    process_ratings(x);
    return 0;
}