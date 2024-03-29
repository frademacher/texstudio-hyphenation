#!/usr/bin/env python3

# hyphen is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation in version 2 of the License.

# hyphen is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# hyphen. If not, see <https://www.gnu.org/licenses/old-licenses>.

# Copyright (c) 2018 Florian Rademacher <florian.rademacher@fh-dortmund.de>

import pyphen
import sys

DEFAULT_LANGUAGE = 'en_US'
NON_ALPHA_WORD_SEPARATORS = ['-', '_', '.', ' ']
NO_HYPHEN_WORD_SEPARATORS = [' ', '-']

def hyphen(word, language):    
    hyphenatedWords = []

    separatedWords = separateWord(word)
    hyphenator = pyphen.Pyphen(lang=language)
    for singleWord in separatedWords:
        if not singleWord in NON_ALPHA_WORD_SEPARATORS \
            and not singleWord in NO_HYPHEN_WORD_SEPARATORS:
            hyphenatedWord = hyphenator.inserted(singleWord)
            hyphenatedWords.append(hyphenatedWord.replace('-', '\-'))
        else:
            hyphenatedWords.append(singleWord)

    result = ''
    addHyphenationSign = False
    for hyphenatedWord in hyphenatedWords:
        if addHyphenationSign \
            and hyphenatedWord not in NO_HYPHEN_WORD_SEPARATORS:
            result += '\-'

        result += hyphenatedWord
        addHyphenationSign = hyphenatedWord not in NO_HYPHEN_WORD_SEPARATORS

    if result.endswith('\-'):
        result = result[:-2]

    return result

def getNonAlphaSeparator(word):
    for nonAlphaSeparator in NON_ALPHA_WORD_SEPARATORS:
        if nonAlphaSeparator in word:
            return nonAlphaSeparator
    return None

def separateWord(word):
    separatedWords = []
    nonAlphaSeparator = getNonAlphaSeparator(word)
    if nonAlphaSeparator is not None:
        for separatedWord in word.split(nonAlphaSeparator):
            separatedWords.append(separatedWord)
            separatedWords.append(nonAlphaSeparator)
        
        return separatedWords[:-1]

    lastLetterIndex = len(word) - 1
    index = 0
    letter = word[index]

    while index < lastLetterIndex:
        wordBuffer = ''

        while not letter.isalpha() and index < lastLetterIndex:
            wordBuffer += letter
            index += 1
            letter = word[index]

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
    if len(sys.argv) <= 1:
        sys.exit(0)

    wordToHyphen = None
    languageToHyphen = None
    if len(sys.argv) == 2:
        wordToHyphen = sys.argv[1]
        languageToHyphen = DEFAULT_LANGUAGE
    elif len(sys.argv) > 2:
        wordToHyphen = sys.argv[1]
        languageToHyphen = sys.argv[2]

    try:
        print(hyphen(wordToHyphen, languageToHyphen))
    except KeyError as ex:
        print()
