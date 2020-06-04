#Palindrome program

def isPalindrome(string):
     left,right=0,len(string)-1
     while right>=left:
             
             print(left)
             print(right)

             print(string[left])
             print(string[right])
             if not string[left]==string[right]:
                      return False
             left=left+1
             right=right-1
             return True

a=isPalindrome('AABAC')

print(a)