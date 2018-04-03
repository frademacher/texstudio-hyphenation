#!/usr/bin/env python3

import pyphen
import sys

LANGUAGE = 'en_US'

def hyphen(word, language):    
    hyphenatedWords = []

    separatedWords = separateWordByUppercase(word)
    hyphenator = pyphen.Pyphen(lang=language)
    for singleWord in separatedWords:
        hyphenatedWord = hyphenator.inserted(singleWord)
        hyphenatedWords.append(hyphenatedWord.replace('-', '\-'))

    return '\-'.join(hyphenatedWords)
    
def separateWordByUppercase(word):
    separatedWords = []
    lastLetterIndex = len(word) - 1
    index = 0
    letter = word[index]

    while index < lastLetterIndex:
        wordBuffer = ''

        previousLetterWasUpper = False
        while letter.isupper() and index < lastLetterIndex:
            previousLetterWasUpper = True
            wordBuffer += letter
            index += 1
            letter = word[index]

        previousLetterWasLower = False
        while letter.islower() and index < lastLetterIndex:
            previousLetterWasUpper = False
            previousLetterWasLower = True
            wordBuffer += letter
            index += 1            
            letter = word[index]            

        if index == lastLetterIndex:
            lastLetterHasSameCase = \
                letter.isupper() and previousLetterWasUpper \
                    or letter.islower() and previousLetterWasLower

            if lastLetterHasSameCase:
                wordBuffer += letter
            else:
                separatedWords.append(wordBuffer)
                wordBuffer = letter

        separatedWords.append(wordBuffer)

    return separatedWords

if __name__ == '__main__':
    if len(sys.argv) > 1:
        wordToHyphen = sys.argv[1]
        print(hyphen(wordToHyphen, LANGUAGE))
