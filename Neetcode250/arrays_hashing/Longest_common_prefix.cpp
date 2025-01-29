#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
	public:
		string longestCommonPrefix(vector<string> strs) {
			if (strs.size() == 1){
				return strs[0];
			}
			// Getting the minimum string
			string min_string = *min_element(strs.begin(), strs.end(),
					[](const string& a, const string& b) {
					return a.size() < b.size();
					});

			// Getting the size of the minimum string
			int min_length = min_string.size();
			
			// Initializing the longest common prefix string
			string res = "";

			// Iterating through the vector
			for (int i = 0; i < min_length; i++){
				for (int j = 1; j < strs.size(); j++){
					if (strs[j][i] == strs[j-1][i] && j != strs.size() - 1){
						continue;
					}
					if (strs[j][i] == strs[j-1][i] && j == strs.size() - 1) {
						res += strs[j][i];
					}
					if (strs[j][i] != strs[j-1][i]) {
						return res;
					}
				}
			}
			return res;
		}
};

int main() {
	Solution solution;

	vector<string> strs1 = {"flower", "flow", "flight"};
	vector<string> strs2 = {"dog", "racecar", "car"};

	cout << "Longest Common Prefix (Test 1): " << solution.longestCommonPrefix(strs1) << endl;
	cout << "Longest Common Prefix (Test 2): " << solution.longestCommonPrefix(strs2) << endl;

	return 0;
}
