class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        unique_ele=list(freq.keys())
        unique_ele.sort(key=lambda x:freq[x],reverse='True')
        return unique_ele[:k]