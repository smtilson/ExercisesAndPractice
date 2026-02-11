import time

def check_outer(word: str) -> bool:
    return word[0] == word[-1]

def truncate(word: str) -> str:
    return word[1:-1]

def is_palindrome_recursive(word: str) -> bool:
    if len(word) <=1:
        return True
    elif check_outer(word):
        return is_palindrome_recursive(truncate(word))
    return False

def process_word(word: str) -> str:
    # separated so that different levels of processing can be applied based on the test case requirements
    word = word.lower()
    word = word.replace(" ", "")
    word = "".join([char for char in word if char.isalnum()])
    return word

def make_palindrome(n):
    half = "abc" * (n )
    return half + half[::-1]

test_strings = [
    make_palindrome(10),
    make_palindrome(100),
    make_palindrome(1000),
    make_palindrome(10000),
]


palindrome_tests = {
    # Simple cases
    "racecar": True,
    "level": True,
    "madam": True,
    "noon": True,
    "civic": True,

    # Non-palindromes
    "hello": False,
    "python": False,
    "palindrome": False,

    # Case sensitivity
    "Racecar": True,
    "Level": True,

    # Single character / empty
    "a": True,
    "": True,

    # Numbers as strings
    "121": True,
    "12321": True,
    "123": False,

    # Spaces and punctuation (raw strings, no preprocessing)
    "nurses run": True,
    "A man a plan a canal panama": True,
    "racecar!": True,

    # Mixed alphanumeric
    "abcba123": False,
    "123abcba321": True ,

    # Repeated characters
    "aaaaaa": True,
    "aaaab": False,
}

def is_palindrome_2_pointer(word: str) -> bool:
    word = process_word(word)
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def main(method):
    start_time = time.time()
    for test, expected in palindrome_tests.items():
        processed = process_word(test)
        try:
            result = method(processed)
            assert result == expected, f"Test failed for test of length {len(test)}: expected {expected}, got {result}"
        except Exception as e:
            print(f"Test raised an exception for test of length {len(test)}: {e}")
        
    
    for test in test_strings:
        processed = process_word(test)
        try:
            result = method(processed)
            assert result == True, f"Test failed for test of length {len(test)}: expected True, got {result}"
        except Exception as e:
            print(f"Test raised an exception for test of length {len(test)}: {e}")
        
        
    end_time = time.time()
    print(f"All tests passed in {end_time - start_time:.6f} seconds")



if __name__ == "__main__":
    main(is_palindrome_2_pointer)
    main(is_palindrome_recursive)