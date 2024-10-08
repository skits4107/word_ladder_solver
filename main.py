from collections import deque
from colorama import Fore

def get_word_neighbors(words, word):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    neighbors = []
    for i in range(len(word)):
        for char in alphabet:
            new_word = word[:i] + char + word[i+1:] # mutate the word
            if new_word in words and new_word != word:
                neighbors.append(new_word)
    return neighbors

def get_ladder(predecessors, final_word):
    # builds path backwords by adding the predecessor of each word starting from final word until there isnt any
    ladder = [final_word]
    while predecessors[final_word] != None:
        final_word = predecessors[final_word]
        ladder.append(final_word)
    ladder.reverse()
    return ladder

def bfs_word_ladder_sovler(words, starting_word, final_word):

    # used to sotre next words to check
    queue = deque([starting_word]) 

    #will be used to generate the path or chain of words by keeping track of what words came before each other
    predecessors = { starting_word: None }

    #while there are still words to visit
    while queue:

        #get the word to visit from queue and check if it is the final word
        current_word = queue.popleft()
        if current_word == final_word:
            ladder = get_ladder(predecessors, current_word)
            return ladder
        
        #get the neighbors or words that are valid chains of the current word
        neighbors = get_word_neighbors(words, current_word)

        for neighbor in neighbors:
            if neighbor not in predecessors:
                #if we havent checked this word add it to queue to be checked and set its predeccessor
                predecessors[neighbor] = current_word
                queue.append(neighbor)

    #if no path or chain is found
    return None

def get_user_word(words, prompt):
    #keeps asking for a word until word is a valid word
    while True:
        word = input(prompt)
        if word not in words:
            print("invalid word")
            continue
        return word
    
def get_user_words(words):
    #keeps asking for set of words unitl the words are valid
    while True:
        starting_word = get_user_word(words, f"{Fore.WHITE}enter {Fore.GREEN}starting {Fore.WHITE}word: ")
        ending_word = get_user_word(words, f"{Fore.WHITE}enter {Fore.RED}final {Fore.WHITE}word: ")

        if starting_word == ending_word:
            print(f"{Fore.RED}words cant be the same{Fore.WHITE}")
            continue
        if len(starting_word) != len(ending_word):
            print(f"{Fore.RED}words have to be same length{Fore.WHITE}")
            continue
        return starting_word, ending_word


def main():

    with open("words.txt", "r") as file:
        file_content = file.read()
    words = set(file_content.strip().split("\n"))

    print('\n')# add white space
    start_word, end_word = get_user_words(words)

    # try get and print path
    ladder = bfs_word_ladder_sovler(words, start_word, end_word)

    if ladder:
        #color the first and last word
        ladder[0] = Fore.GREEN + ladder[0] + Fore.WHITE
        ladder[-1] = Fore.RED + ladder[-1] + Fore.WHITE

        print(f"{Fore.WHITE}the shortest word ladder is: " + " -> ".join(ladder))
    else:
        print(f"{Fore.RED}no path found{Fore.WHITE}")


    print('\n') # add white space

if __name__ == "__main__":
    main()

