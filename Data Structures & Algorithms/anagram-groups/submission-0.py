class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for word in strs:
            s = "".join(sorted(word))
            if s not in anagram:
                anagram[s] = []
            anagram[s].append(word)

        return list(anagram.values())

        