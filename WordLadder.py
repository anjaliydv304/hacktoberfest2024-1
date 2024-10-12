from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return []

    layers = {}
    layers[beginWord] = [[beginWord]]

    queue = deque([beginWord])
    found = False
    while queue and not found:
        next_layer = defaultdict(list)
        for word in queue:
            if word == endWord:
                found = True
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordList:
                        next_layer[new_word] += [j + [new_word] for j in layers[word]]

        wordList -= set(next_layer.keys())
        layers = next_layer
        queue = deque(next_layer.keys())

    return layers.get(endWord, [])
