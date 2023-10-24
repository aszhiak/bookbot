
def main():
    file_path = "./books/frankenstein.txt"    
    content = get_book_content(file_path)
    words_counted = word_count(content)
    char_count = get_character_count(content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_counted} words was found in the document\n")
    alpha_list = remove_non_alpha(char_count)
    for a in alpha_list:        
        print(f"The {a['char']} character was found {a['num']} times")
        
    
    
def word_count(content):
    words = content.split()
    return len(words)

def get_book_content(path):
    with open(path) as f:
        return f.read()
        
def get_character_count(content):
    content = content.lower()
    char_count = {}
    for char in content:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def remove_non_alpha(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char":char, "num": char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    
    for i in range(len(char_list)- 1, 0-1, -1):        
        if not char_list[i]["char"].isalpha():            
            del char_list[i]
    return char_list

def sort_on(d):
    return d["num"]
    


main()
    