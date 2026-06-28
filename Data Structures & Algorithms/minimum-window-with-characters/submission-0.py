class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)      # Wanted clues
        window = {}            # Clues collected in current window

        have = 0               # Number of clue types completely satisfied
        needCount = len(need)  # Number of different clue types required

        res = [-1, -1]         # Best window found so far
        resLen = float("inf")  # Length of best window

        l = 0                  # Left pointer

        for r in range(len(s)):

            c = s[r]           # Detective visits a new street

            window[c] = window.get(c, 0) + 1  # Collect clue

            # Have we collected enough of this clue?
            if c in need and window[c] == need[c]:
                have += 1

            # If all clue types are satisfied,
            # try to make the window smaller
            while have == needCount:

                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove leftmost clue
                window[s[l]] -= 1

                # Did removing it make us lose a required clue?
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""