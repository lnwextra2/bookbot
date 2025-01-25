# print("hello world")

def CountWords(texts):
    return len(texts.split())
    
def CountCharacters(texts):
    char = {}
    for s in texts.lower():
        if s.isalpha():
            char[s] = char.get(s,0) + 1
        # char[s] = num + 1
    return char
    
def getString(path):
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict["num"]

def dict_to_List_of_Dict(dictc):
    char_list = []
    for char, count in dictc.items():
        char_list.append({"char":char,"num":count})
        
    char_list.sort(reverse=True,key=sort_on)
    return char_list

def main():
    BookPath = 'books/frankenstein.txt'
    dictc = CountCharacters(getString(BookPath))
    list_dict = dict_to_List_of_Dict(dictc)

    for i in list_dict:
        print(f"'{i["char"]}' = {i["num"]}")
    
main()