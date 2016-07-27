#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;

//Please note the file names have been change, these are present just
//for rafernce.

void process_movies() {
    ifstream in("mLarge/movie.csv", ios::in); // Obsolete
    ofstream out("mLarge/movies.csv", ios::out);
    if (!in) {
        std::cerr << "Could not create output file\n";
    }

    int id = 0;
    string s;
    getline(in, s);
    while(!in.eof()) {
        if(id % 50 == 0) cout << "Done movie no:" << id << endl;
        getline(in, s);
        //cout << s << endl;
        if('0' <= s[0] && s[0] <= '9') {
            out << id << "," << s.substr(s.find(',')+1) << endl;
            id++;
        } else {
            continue;
        }
    }
    in.close();
    out.close();
} 

int main() {
    cout << "Processing movies\n";
    process_movies();
    return 0;
}