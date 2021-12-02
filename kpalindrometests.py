from kpalindrome import is_k_palindrome, is_palindrome_recursive, is_palindrome_iterative

# is_palindrome_iterative tests
assert is_palindrome_iterative("abcdcba") == True
assert is_palindrome_iterative("a") == True
assert is_palindrome_iterative("abcdecba") == False
assert is_palindrome_iterative("ab") == False

# Your additional is_palindrome_iterative tests go here
assert is_palindrome_iterative("acdca") == True
assert is_palindrome_iterative("aa") == True
assert is_palindrome_iterative("civic") == True
assert is_palindrome_iterative("") == False  # Added an if statement if it was an empty string.
assert is_palindrome_iterative("abcdcbaba") == False
assert is_palindrome_iterative("bacdcba") == False

# is_k_palindrome tests
assert is_k_palindrome("a", 0) == True
assert is_k_palindrome("abcdecba", 1) == True
assert is_k_palindrome("abcdecba", 2) == True
assert is_k_palindrome("abcdecba", 0) == False

# Your additional is_k_palindrome tests go here
assert is_k_palindrome("abcdcfba", 1) == True
assert is_k_palindrome("aa", 0) == True
assert is_k_palindrome("racecar", 3) == True
assert is_k_palindrome("", 1) == False  # Empty String, so it should return false.
assert is_k_palindrome("abcdcfba", 0) == False
assert is_k_palindrome("b", -1) == False  # Added an if statement if the k was negative.

# is_palindrome_recursive tests
assert is_palindrome_recursive("abcdcba") == True
assert is_palindrome_recursive("a") == True
assert is_palindrome_recursive("abcdecba") == False
assert is_palindrome_recursive("ab") == False

# Your additional is_palindrome_recursive tests go here
assert is_palindrome_iterative("aa") == True
assert is_palindrome_iterative("noon") == True
assert is_palindrome_iterative("racecar") == True
assert is_palindrome_iterative("") == False  # Added an if statement if it was an empty string.
assert is_palindrome_iterative("afdfda") == False
assert is_palindrome_iterative("abc") == False

# Keep this at the bottom
print("If you are reading this, all tests passed!")
