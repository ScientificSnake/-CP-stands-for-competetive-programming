"""Farmer John is trying to teach his cows to read by giving them a set of N
 spelling boards typically used with preschoolers (1≤N≤100
). Each board has a word and an image on each side. For example, one side might have the word 'cat' along with a picture of a cat, and the other side might have the word 'dog' along with a picture of a dog. When the boards are lying on the ground, N
 words are therefore shown. By flipping over some of the boards, a different set of N
 words can be exposed.
To help the cows with their spelling, Farmer John wants to fashion a number of wooden blocks, each embossed with a single letter of the alphabet. He wants to make sufficiently many blocks of each letter so that no matter which set of N
 words is exposed on the upward-facing boards, the cows will be able to spell all of these words using the blocks. For example, if N=3
 and the words 'box', 'cat', and 'car' were facing upward, the cows would need at least one 'b' block, one 'o' block, one 'x' block, two 'c' blocks, two 'a' blocks, one 't' block, and one 'r' block.

Please help the Farmer John determine the minimum number of blocks for each letter of the alphabet that he needs to provide, so that irrespective of which face of each board is showing, the cows can spell all N
 visible words.
 
From USACO.org and USACO.guide
"""
import string

import sys

sys.stdin = open("blocks.in", 'r')
sys.stdout = open("blocks.out", "w")

NBlocks = int(input())

lettersNeeded = [0] * 26

def toNum(s: str) -> int:
    return string.ascii_lowercase.index(s.lower())

runnningLetters1 = [0] * 26
runnningLetters2 = [0] * 26
for _ in range(NBlocks):
    word1, word2 = input().split()

    for char in word1:
        index = toNum(char)
        runnningLetters1[index] += 1
    for char in word2:
        index = toNum(char)
        runnningLetters2[index] += 1
    
    for i in range(26):
        letter_count = max(runnningLetters1[i], runnningLetters2[i])
        lettersNeeded[i] += letter_count
    runnningLetters1 = [0] * 26
    runnningLetters2 = [0] * 26

for i in lettersNeeded:
    print(i)