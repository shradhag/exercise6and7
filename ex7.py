#open the file and read it
def file_into_list(path):
    file_obj= open(path)
    words = []
    for l in file_obj:
        line = l.rstrip()
        words.extend(line.split(" "))
    return words 

#take the list of words, insert into dictionart and keep word count
def word_dict(alist):
    word_count = {}
    for word in alist:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def print_to_screen(dictionary):
    alist =  dictionary.items()
    for i in alist:
        print i[0], i[1] 



def main():
    output = word_dict(file_into_list("inputfile.txt"))
    print_to_screen(output)

main()