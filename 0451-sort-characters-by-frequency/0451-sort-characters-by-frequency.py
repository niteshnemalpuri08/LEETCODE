class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        # Count frequency
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Sort characters by frequency
        chars = sorted(freq, key=freq.get, reverse=True)

        ans = ""

        for ch in chars:
            ans += ch * freq[ch]

        return ans
        