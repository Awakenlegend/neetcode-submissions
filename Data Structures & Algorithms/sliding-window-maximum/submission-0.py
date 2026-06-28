from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  #to show strogest warrior front
        ans = []     #final ans all strogest warrior in kingdom

        l = 0

        for r in range(len(nums)):

            #remove weaker warrior from back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            #add new warrior
            q.append(r)

            #remove warrior who left window
            if q[0] < l:
                q.popleft()

            #window complete
            if r + 1 >= k:
                ans.append(nums[q[0]])
                l += 1

        return ans