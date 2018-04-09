%SCRIPT
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
