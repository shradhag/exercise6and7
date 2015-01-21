
# read file and place contents in dictionary
def file_to_dict(path):
    file_obj = open(path)
    ratings_dict = {}
    for line in file_obj:
        line = line.rstrip()
        restaurant = line.split(":")
        ratings_dict[restaurant[0]] = restaurant[1]
    return ratings_dict

# sort and print out report it on the screen (print)
def sorted_results(dictionary):
    keys = dictionary.keys()
    keys.sort() 
    for k in keys:
        print "%s is rated at %s"  % (k,dictionary[k]) 


def main():
    sorted_results(file_to_dict("scores.txt"))

main()