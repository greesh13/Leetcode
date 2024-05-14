class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=s.lower()
        space=re.sub(r'[^a-zA-Z0-9]', '', new)
        

        if str(space)==str(space[::-1]):
            return True 
        return False



#     s= re.sub(r'[^a-zA-Z0-9]', '', s)
#         s=s.lower()
#         rev_s=s[::-1]
        
#         if s==rev_s:
#             return True
#         else:
#             return False
    
    
    
    
            
            
            
             

        
        
        

        
        
        
        
        