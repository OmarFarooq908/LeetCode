#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
	public:
		vector<vector<string>> groupAnagrams(vector<string>& strs) {
			vector<vector<string>> res;
			vector<string> strs_sorted = strs;
			unordered_map <string, int> umap;
			for (int i = 0; i < strs.size(); i++){
				sort(strs_sorted[i].begin(), strs_sorted[i].end());
				umap[strs[i]] = i;
			}
			for (auto x : umap){
				if(){
				}
			}
			return res;
		}
};


int main() {
	Solution solution;
	
	vector<string> strs1 = ["act","pots","tops","cat","stop","hat"];
	vector<string> strs2 = ["x"];
	vector<string> strs3 = [""];

	cout << "Group Anagrams (Test 1): " << solution.groupAnagrams(strs1) << endl;
	cout << "Group Anagrams (Test 2): " << solution.groupAnagrams(strs2) << enld;
	cout << "Group Anagrams (Test 3): " << solution.groupAnagrams(strs3) << endl;
	return 0;
}
