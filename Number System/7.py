# https://takeuforward.org/data-structure/convert-digits-numbers-to-words/


# Example 1:
# Input: 7824
# Output: seven thousand eight hundred twenty four
# Explanation: 7824 in words can be written as seven thousand eight hundred twenty four.
def number_to_words(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def helper(n, idx):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n] + " "
        elif n < 20:
            return teens[n - 10] + " "
        elif n < 100:
            return tens[n // 10] + " " + helper(n % 10, idx)
        else:
            return ones[n // 100] + " hundred " + helper(n % 100, idx)

    if num == 0:
        return "zero"

    result = ""
    idx = 0

    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000, idx) + thousands[idx] + " " + result
        num //= 1000
        idx += 1

    return result.strip()


# Example usage:
number_input = 7824
words_output = number_to_words(number_input)
print(words_output)