def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def string_with_most_vowels(strings):
    max_vowels = 0
    max_string = ""

    for string in strings:
        num_vowels = count_vowels(string)
        if num_vowels > max_vowels:
            max_vowels = num_vowels
            max_string = string

    return max_string


L = ["Prakriti","Manocha","Branch","Computer"]
result = string_with_most_vowels(L)
print("String with the most vowels:", result)
