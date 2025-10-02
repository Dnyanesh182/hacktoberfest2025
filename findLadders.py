from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return []
    wordList.add(beginWord)
    neighbors = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            neighbors[word[:i] + '*' + word[i+1:]].append(word)
    queue = deque([(beginWord, [beginWord])])
    visited = set([beginWord])
    result = []
    found = False
    while queue and not found:
        level_visited = set()
        for _ in range(len(queue)):
            current_word, path = queue.popleft()
            for i in range(len(current_word)):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                for neighbor in neighbors[intermediate_word]:
                    if neighbor == endWord:
                        result.append(path + [endWord])
                        found = True
                    if neighbor not in visited:
                        level_visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))
        visited.update(level_visited)
    return result
