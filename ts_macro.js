SCRIPT

/*
    ts_macro is free software: you can redistribute it and/or modify it under 
    the terms of the GNU General Public License as published by the Free 
    Software Foundation in version 2 of the License.

    hyphen is distributed in the hope that it will be useful, but WITHOUT ANY
    WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
    FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
    details.

    You should have received a copy of the GNU General Public License along 
    with hyphen. If not, see <https://www.gnu.org/licenses/old-licenses>.

    Copyright (c) 2018 Florian Rademacher <florian.rademacher@fh-dortmund.de>
*/

const HYPHENATION_SCRIPT = 
    "[HYPHEN_FOLDER]/hyphen.py"

const LANGUAGE_ID_PATTERN = 
	/%\s*!TeX\s*spellcheck\s*=\s*(.*)/

var firstLine = editor.text(0)
var languageToHyphen = null

if (firstLine) {
	var languageIdMatch = firstLine
		.match(LANGUAGE_ID_PATTERN)
	if (languageIdMatch)
		languageToHyphen = 
			languageIdMatch[1]
}

var wordToHyphen = cursor.selectedText()
var hyphenationCommand = null

if (wordToHyphen) {
	hyphenationCommand = "python3 " +
		HYPHENATION_SCRIPT + " " +
	wordToHyphen

	if (languageToHyphen)
		hyphenationCommand += " " +
			languageToHyphen
}

if (hyphenationCommand) {
	var hyphenationProc = 
		system(hyphenationCommand)
	hyphenationProc.standardOutputRead
		.connect(function(hyphenated) {
			if (hyphenated)
				editor.write(hyphenated)
		}
	)

	hyphenationProc.waitForFinished()
}
