import json
import time

class Dictionary:
    def __init__(self, file) -> None:
        self.dict = json.loads(open(file).read())

    def __contains__(self, word):
        if word in self.dict:
            return True
        return False
    
    def checkPrefix(self, prefix):
        for word in self.dict:
            if word[:len(prefix)] == prefix:
                return True
        return False

class PrefixTree:
    def __init__(self, val = None) -> None:
        self.value = val
        self.children = {}

    def typecheck(self, word):
        if not isinstance(word, str):
            raise TypeError
        
    def add(self, word):
        self.typecheck(word)

        if word == "":
            return
        
        if word[0] not in self.children:
            tree = PrefixTree(word[0])
            tree.add(word[1:])
            self.children[word[0]] = tree
        else:
            self.children[word[0]].add(word[1:])
    
    def __contains__(self, prefix):
        if prefix == "":
            return True
            # raise Exception("Invalid string")
        
        if len(prefix) == 1:
            if prefix[0] in self.children:
                return True
            return False

        if prefix[0] in self.children:
            return prefix[1:] in self.children[prefix[0]]


    def show(self):
        if not self.children:
            return None
        
        return {key : child.show() for key, child in self.children.items()}
    
    def get_words(self):
        # not accurate as prefix-words aren't returned (ex/ app if apple is a word)
        if not self.children:
            return [""]
        
        words = []
        for child, tree in self.children.items():
            words += [child + prefix for prefix in tree.get_words()]
        # print(words)
        return words

    def save(self, filename = "prefixtree.json"):
        with open(filename, "w") as json_file:
            json.dump(self.show(), json_file, indent=4)
    
    def deserialize(self, val, obj):
            if not obj:
                return PrefixTree(val) 
            
            new_branches = {}
            for letter, children in obj.items():
                new_branches[letter] = self.deserialize(letter, children)
            
            new_tree = PrefixTree(val)
            new_tree.children = new_branches
            return new_tree
    

    def load(self, filename):
        with open(filename, "r") as json_file:
            tree = json.load(json_file)
        
        return self.deserialize(None, tree)



def speed_test():
    file = 'words_dictionary.json'
    space = Dictionary(file)
    tree = PrefixTree()

    test = ["ab", "zywe", "tre", "bac", "zyy", "mzun"]
    check = [True, False, True, True, False, True]
    wordlist = json.loads(open(file).read())

    print("Initializing Tree")
    for word in wordlist:
        tree.add(word)
    print("Finished Tree")

    start = time.time()
    for word, ans in zip(test, check):
        if not space.checkPrefix(word) == ans:
            print("Dict failed")
            break
    print(time.time() - start)

    start = time.time()
    for word, ans in zip(test, check):
        if not (word in tree) == ans:
            print("Tree failed")
            break
    print(time.time() - start)
        


if __name__ == "__main__":
    pass


