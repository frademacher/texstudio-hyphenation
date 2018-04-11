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
