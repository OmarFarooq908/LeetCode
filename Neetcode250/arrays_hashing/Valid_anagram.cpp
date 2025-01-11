#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
        public:
                bool isAnagram(string s, string t) {
                    int n;
                    if (s.size() != t.size()){
                            return false;
                    }
                    else {
                        n = s.size();
                    }
                    unordered_map <char, int> umap;
                    unordered_map <char, int> umap2;
                    for (int i = 0; i < n; i++) {
                        if (umap.find(s[i]) == umap.end()) {
                            umap[s[i]] = 1;
                        }
                        else {
                            umap[s[i]]++;
                        }

                        if (umap2.find(t[i]) == umap2.end()) {
                            umap2[t[i]] = 1;
                        }
                        else {
                            umap2[t[i]]++;
                        }
                    }
                    for (auto i : umap) {
                        if (umap2.find(i.first) != umap2.end()){
                            if (umap2[i.first] != i.second){
                                return false;
                            }
                        }
                        else {
                            return false;
                        }
                    }
                        return true;
                }
};  
