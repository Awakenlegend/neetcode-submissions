class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force tc:o(nlogn) sc:O(n)
        # freq={}
        # for num in nums:
        #     freq[num]=freq.get(num,0)+1
        # unique_ele=list(freq.keys())
        # unique_ele.sort(key=lambda x:freq[x],reverse='True')
        # return unique_ele[:k]

        #optimal sol
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        bucket=[[] for _ in range(len(nums)+1)]
        for num,count in freq.items():
            bucket[count].append(num)
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return res