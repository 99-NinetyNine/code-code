"""

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

"""
"""
Solution Working:
  for BFS.
    Make a Q(a doubly ended queue)
    and a set visited
 
  while doing search, we pop from the left of Q the word current_word CW.

  Each character of CW is replaced with the alphabets to see if it matches the endWord, and return it, Else, if next_word is in WordSet and we have not visisted yet, push the NW  from the right into the Q.

  A Brute force search. but using graph, hence its breath first search


"""
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + char + current_word[i+1:]
                    
                    if next_word == endWord:
                        return level + 1
                    
                    if next_word in wordSet and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
        
        return 0  # If no transformation sequence found
