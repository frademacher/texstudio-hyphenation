%SCRIPT
var selectedText = cursor.selectedText()
var hyphenProc = system("python3 [HYPHEN_FOLDER]/hyphen.py " + selectedText)
hyphenProc.standardOutputRead.connect(
    function(hyphenated) {
        editor.write(hyphenated)
    }
)
hyphenProc.waitForFinished()
