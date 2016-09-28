def computeLongestPalindrome(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)
    def is_palindrome(text):
        if len(text) < 2:
            return True
        if text[0] != text[-1]:
            return False
        return is_palindrome(text[1: -1])

    if is_palindrome(text):
        return len(text)
    else:
        d = collections.defaultdict(int)
        for ch in text:
            d[ch] += 1
        i, j = 0, len(text) - 1
        while text[i] == text[j]:
            i += 1
            j -= 1
        split = i if d[text[i]] < d[text[j]] else j if d[text[j]] < d[text[i]] else i
        text = text[:split] + text[split + 1:]
        return computeLongestPalindrome(text)


print computeLongestPalindrome("animal")
print computeLongestPalindrome("")
print computeLongestPalindrome("aa")
print computeLongestPalindrome("a")
print computeLongestPalindrome("ab")
print computeLongestPalindrome("GGABZXVYCCDBA")
print computeLongestPalindrome("ABGBAD")


