def number_of_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    count = {}
    lowercase = text.lower()

    for letter in lowercase:
        if letter not in count:
            count[letter] = 1 
        else:
            count[letter] += 1


    return count

def sort_dict(items):
    return items["num"]

def sort_list(dict_nums):
    sorted_list = []
    for letter in dict_nums:
        sorted_list.append({"letter": letter, "num": dict_nums[letter]})
    sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list




