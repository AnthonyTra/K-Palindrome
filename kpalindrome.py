def is_palindrome_iterative(string):
    """This function uses a for loop to compare the last letter and first letter to determine if it is a palindrome."""
    if string == "":  # If the string is empty then return false.
        return False

    counter = len(string) - 1
    last_letter = string[counter]
    half = (len(string) - 1) / 2
    for letter in string:
        if letter == last_letter and counter != half:
            counter = counter - 1
            last_letter = string[counter]  # Updates the last letter(moves a letter behind)if the if statement is met.
        elif counter == half:
            return True  # If the ending half of the string matches the starting half, then it is true.
        else:
            return False  # If the ending half of the string does not match the starting half, then it is false.
    return True


def is_palindrome_recursive(string):
    """This function uses a recursive step to find out if it is a palindrome or not."""
    if string == "":  # If the string is empty then return false.
        return False

    length = len(string) - 1
    if len(string) <= 1:  # Base case
        return True
    else:
        if string[0] == string[length]:  # If the letters match, then it calls the method again.
            return is_palindrome_recursive(string[1:length])  # returns the next first and last letter of the string.
        else:
            return False  # If the letters do not match then it returns false.


def is_k_palindrome(string, k):
    """This function determines if a certain string is of 'k-palindrome'."""
    if k < 0:
        return False  # If k is less then 0, then it returns false.

    if k == 0:
        return is_palindrome_iterative(string)
    if is_palindrome_iterative(string):  # If it is a palindrome, then it returns true.
        return True
    for i in range(len(string)):
        new_string = string[:i] + string[i + 1:]  # It updates the string with a character removed.
        if is_k_palindrome(new_string, k - 1):
            return True
    return False

