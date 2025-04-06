from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""
        for str in strs:
            result += str.replace("#","##") + " # "
        return result
    
    def decode(self, s: str) -> List[str]:

        strlist = []
        list1 = s.split(" # ")
        for index in range(0,len(list1)-1):
            strlist.append(list1[index].replace("##","#"))
        return strlist  
       

obj = Solution()
stringlist = ["neet","code","love","you"] 
encode = obj.encode(stringlist)
print(f" encode ={encode} ")

orig = obj.decode(encode)
print(orig)

stringlist = [""] 
encode = obj.encode(stringlist)
print(f" encode ={encode} ")
print(len(encode))

orig = obj.decode(encode)
print(orig)

