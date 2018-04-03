Hyphenation of technical Terms for [TeXstudio](https://www.texstudio.org/)
============================================

This repository contains a [Python 3](http://python.org/) script that hyphenates a single word
with respect to case sensitivity. As punctuation mark for the word breaks
[LaTeX's](https://www.latex-project.org/) "\\-" is used.

Respecting case sensitivity makes the script applicable especially for 
technical terms. For example, the script will partition of technical 
term like "ServiceContract", which consists of two words separated by
the uppercase "C", first partition into two words "Service" and 
"Contract". Second, both words will be hyphenated separately. In a 
third step, the hyphenation results will be concatenated with a 
separating LaTeX hyphen "\\-". Hence, the hyphenated version of 
"ServiceContract" will read "Ser\\-vice\\-Con\\-tract", which is LaTeX
conform.

The script may then be embedded as a macro in TeXstudio to realize
in-place hyphenation of a selected word.

## Installation Steps

The following steps are required to install the script, make it runnable
and executable from TeXstudio as a macro:

1. Install [`pyphen`](http://pyphen.org/) package for Python3:
```shell
    pip3 install pyphen
```

2. `git clone` the repository to your favorite folder on your harddrive 
(preferably somewhere under your home directory `~`).

3. Create a new [TeXstudio macro](http://texstudio.sourceforge.net/manual/current/usermanual_en.html#SECTION33)
with the following content (replace [HYPHEN_FOLDER] with the path of the 
folder where you previously cloned ``hyphen.py'' to):
```js
    %SCRIPT
    var selectedText = cursor.selectedText()
    var hyphenProc = system("python3 [HYPHEN_FOLDER]/hyphen.py " + selectedText)
    hyphenProc.standardOutputRead.connect(
        function(hyphenated) {
            editor.write(hyphenated)
        }
    )
    hyphenProc.waitForFinished()
```

For the purpose of self-containment, the script content is also part of
the repository (see file ``ts_macro.js'').