def contains_vowel(s):
    vowels = 'aeiouAEIOU'
    s = s.strip()  # Remove any leading or trailing whitespace
    for char in s:
        if char in vowels:
            print("The string contains a vowel.")
            return
    print("The string does not contain any vowel.")

s= input()
contains_vowel(s)  # This should output "The string contains a vowel."