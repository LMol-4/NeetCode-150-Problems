class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        answer = []
        
        for word in strs:
            sorted_word = tuple(sorted(word))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        for key in anagrams:
            answer.append(anagrams[key])
        
        return answer