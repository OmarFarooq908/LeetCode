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
			int min = min_string.size();

			// Initializing the longest common prefix string
			string res = "";

			// Flag for consecutive occurance of letter
			bool consec = true;

			// Iterating through the vector
			for (int i = 0; i < min; i++){
				for (int j = 0; j < strs.size(); j++){
					if (j ==0 || (j > 0 && strs[j][i] == strs[j-1][i]) && j != strs.size() - 1){
						consec = true;
						continue;
					}
					if (consec && strs[j][i] == strs[j-1][i] && j == strs.size() - 1) {
						res += strs[j][i];
						consec = false;
					}
					else {
						consec = false;
						i = min;
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
