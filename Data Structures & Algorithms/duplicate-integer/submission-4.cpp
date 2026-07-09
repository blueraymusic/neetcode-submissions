#include <iostream>
#include <vector>
#include <algorithm> 

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::vector<int> l;

        for(auto n:nums){
            auto element = std::find(l.begin(), l.end(), n);
            if (element != l.end()){
                return true;
            }
            l.push_back(n);
        }
        return false;
    }   
};