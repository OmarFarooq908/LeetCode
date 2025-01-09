#include <iostream>
#include <vector>

using namespace std;

// Approach 1

class Solution {
	public:
		vector<int> getConcatenation(vector<int>& nums) {
			int n = nums.size();
			vector<int> ans(2*n);
			int counter = 0;
			for (int i = 0; i < 2*n; i++){
				ans[i] = nums[counter];
				counter++;
				if (counter == n){
					counter = 0;
				}
			}
			return ans;
		}
};
