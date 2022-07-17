class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_length =[]
        sub_letter =[]
        
        for letter in s:
             if letter in sub_letter:
                 sub_length.append(len(sub_letter))
                 sub_letter =[letter]
             else:
                 sub_letter.append(letter)
  
        return(max(sub_length))
            
