#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;

//Please note the file names have been change, these are present just
//for rafernce.

map<int,int> process_movies() {
    ifstream file("mLarge/movie.csv", ios::in);
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
            x[strtol(s,NULL,0)] = id;
            id++;
        } else {
            continue;
        }
    }
    file.close();
    return x;
} 

void process_ratings(map<int,int> &x) {
    ifstream in("mLarge/rating.csv", ios::in); // Obsolete
    ofstream out("mLarge/ratings.csv", ios::out);

    if (!in || !out) {
        std::cerr << "Could not create output file\n";
    }

    char s[200];
    in.getline(s,200);
    int it = 0;

    while(!in.eof()) {
        if(it % 5000 == 0) cout << "Done rating no:" << it << endl;
        it++;
        in.getline(s,200);
        char *a;
        out << strtol(s, &a, 0) - 1 << ",";
        out << x[strtol(a+1, &a, 0)] << ",";
        out << strtod(a+1,NULL) << endl;
    }
    in.close();
    out.close();
}

int main() {
    cout << "Processing movies\n";
    map<int,int> x = process_movies();
    //for(map<int,int>::iterator i = x.begin(); i != x.end(); ++i) {cout << i->first << " " << i->second << endl; } cout << "Processing ratings\n";
    process_ratings(x);
    return 0;
}