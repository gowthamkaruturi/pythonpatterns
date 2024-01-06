from collections import defaultdict,Counter,OrderedDict
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
      print(result[i])
      prefixProduct *= nums[i]
    for i in range(n-1,-1,-1):
      result[i] *= suffixProduct
      print(result[i])
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
  
  def merge_lists(self, lst1:List, lst2:List) -> List:
    result = []
    i,j=0,0
    while i<=len(lst1)-1 and j<=len(lst2)-1:
       if lst1[i] < lst2[j]:
        result.append(lst1[i])
        i +=1 
       else:
        result.append(lst2[j])
        j +=1
    
    while i <=len(lst1)-1:
        result.append(lst1[i])
        i +=1
    while j <=len(lst2)-1:
        result.append(lst2[j])
        j +=1
    return result
          
  def sumOfTwoNumbers(self , lst1:list, k:int) ->list:
    seen = {}
    for i in range(len(lst1)):
       diff = k -lst1[i]
       if diff in seen:
          return [i,seen[diff]]
       else:
          seen[lst1[i]]=i
    return []
       
  def sumOfTwoNumbersIndices(self , lst1:list, k:int) ->list:
     lst1.sort()
     left,right =0,0
     found = False
     result =[]
     while left < right:
        sum = lst1[right]+lst1[left]
        if sum > k:
           left +=1
        elif sum < k :
           right +=1
        else:
           result.append(lst1[right],lst1[right])
           return result
           
     return result
           
           
  def firstNonRepeating(self, arr):
      
      numberDict = {}

      for element in arr:
          numberDict[element] = numberDict.get(element,0)+1
      
      for m in numberDict:
          if numberDict[m]==1:
            return m
      return -1

  def firstNonRepeatingVersion2(self, arr):
    numberDict = OrderedDict()

    for element in arr:
        numberDict[element] = numberDict.get(element,0)+1
      
    for m in numberDict:
        if numberDict[m]==1:
          return m
    return -1
  
  def findTheSecondLargestelement(self, lst :list) -> int:
    if len(lst)<2:
       return list[0]
    maximum = max(lst[0],lst[1])
    second_maximum = min(lst[0],lst[1])
    for i in range(2, len(lst)):
       if lst[i]> maximum:
        second_maximum = maximum
        maximum = lst[i]
       elif lst[i]>second_maximum:
          second_maximum = lst[i]
    return second_maximum
    
  def findTheNLargestelement(self, lst:list,N:int)-> int:
     if len(lst)<2:
       return list[0]
    
     while N>1:
         max = lst.remove(max(lst))
         N -=1
     return max(lst)

     
      

if __name__ == "__main__":
  twoPointers = TwoPointers()
  #print(twoPointers.twoSum([2,7,11,15],9))
  # print(twoPointers.productExceptItself([1,2,3,4,5]))
  #print(twoPointers.merge_lists([1,3,4,5],[2,6,7,8] ))
  #print(twoPointers.sumOfTwoNumbers([1,2,3,4],5))
  #print(twoPointers.firstNonRepeating([4, 5, 1, 2, 0, 4]))
  print(twoPointers.findTheSecondLargestelement([4, 5, 1, 2, 0, 4]))
  print(twoPointers.findTheNLargestelementV2([4, 5, 1, 2, 0, 4]))
      