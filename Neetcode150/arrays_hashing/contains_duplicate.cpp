#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
	bool containsDuplicate(vector<int>& nums){
		unordered_map<int, int> umap;
		for (int i = 0; i < nums.size(); i++){
			umap[i] = nums[i];
		}
	}
};

int main() {
	vector<int> nums = {1,2,3,1}; // True	
	return 0;
}
