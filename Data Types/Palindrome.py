class Palindrome:
    @staticmethod
    def is_palindrome(word):
        #Please write your code here.
        rev=''
        rev=word[::-1]
        if(rev == word):
            return True
        else:
            return False



word = input("Enter the word")
print(Palindrome.is_palindrome(word))