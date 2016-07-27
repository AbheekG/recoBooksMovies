#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;

//Please note the file names have been change, these are present just
//for reference.

map<int,int> process_movies() {
    ifstream file("mLarge/movie.csv", ios::in);
    if (!file) {
        std::cerr << "Could not get file\n";
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

void process_links(map<int,int> x) {
    ifstream in("mLarge/link.csv", ios::in); // Obsolete
    ofstream out("mLarge/links.csv", ios::out);
    if (!in || !out) {
        std::cerr << "Could not create output file\n";
    }

    int id = 0;
    char *a;
    char s[1000];
    in.getline(s, 1000);
    while(!in.eof()) {
        if(id % 50 == 0) cout << "Done movie no:" << id << endl;
        id++;
        in.getline(s, 1000);
        if('0' <= s[0] && s[0] <= '9') {
            out << x[strtol(s, &a, 0)] << ",";
            out << string(a+1) << endl;
        } else {
            continue;
        }
    }
    in.close();
    out.close();
} 

int main() {
    cout << "Processing movies\n";
    map<int,int> x = process_movies();
    //for(map<int,int>::iterator i = x.begin(); i != x.end(); ++i) {cout << i->first << " " << i->second << endl; } cout << "Processing ratings\n";
    cout << "Processing links\n";
    process_links(x);
    return 0;
}