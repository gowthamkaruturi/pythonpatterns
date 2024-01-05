from collections import defaultdict,Counter
from typing import List
class TwoPointers(object):
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      required = {}
      for i ,n in enumerate(nums):
          if target -n in required:
              return [required[target - n],i]
          else:
              required[nums[i]]=i
      
  def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
  
  def validAnagram(self , s:str, t:str ) -> bool:
      if len(s) != len(t):
        return False
      if "".join(sorted(s)) == "".join(sorted(t)):
        return True
      return False  
      
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    sol = defaultdict(list)
    for s in strs:
      sorted_str = ''.join(sorted(s))
      sol[sorted_str].append(s)
           
    return sol.values() 
  
  def topKFrequent(self, nums:List[int], k :int) -> List[int]:
    frequency= dict(Counter(nums))
    frequency = dict(sorted(frequency.items(), key = lambda item:item[1], reverse=True))
    return list(frequency[:k])
        
  def productExceptItself(self,nums:List[int]) ->List[int]:
    n = len(nums)
    prefixProduct =1
    suffixProduct=1
    result = [0]*n
    for i in range(n):
      result[i]= prefixProduct 
      prefixProduct *= nums[i]
    for i in range(n-1,-1,-1):
      result[i] *= suffixProduct
      suffixProduct *= nums[i] 
    return result  
    
  def encode(self, words:List[str]) ->str:
      delimiter = "#"
      result = ""
      for word in words:
        result = str(len(word))+"#"+word
      return result
    
      
  def decode(self,s :str) -> List[str]:
    delimiter = "#"
    result,i = [],0
    while i < len(s):
      j=i
      while s[i] != delimiter:
          j+=1
      length = int(s[i:j])
      result.append(str[j+1:j+1+length])
      i = j+1+length
    return result
      
    
  def longestConsecutive(self, nums: List[int]) -> int:
      sort_nums = set(nums)
      maxCount =0
      for num in nums:
          if num-1 not in sort_nums:
              tmp =1
              while num+1 in sort_nums:
                  tmp +=1
                  num +=1
              maxCount = max(maxCount, tmp)
          
      return maxCount 
          
if __name__ == "__main__":
  twoPointers = TwoPointers()
  print(twoPointers.twoSum([2,7,11,15],9))
  print(twoPointers.productExceptItself([1,2,3,4]))
      