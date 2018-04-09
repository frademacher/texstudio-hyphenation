Hyphenation of technical Terms for [TeXstudio](https://www.texstudio.org/)
============================================

This repository contains a [Python 3](http://python.org/) script that hyphenates a single word
with respect to case sensitivity. As punctuation mark for the word breaks
[LaTeX's](https://www.latex-project.org/) "\\-" is used.

Respecting case sensitivity makes the script applicable especially for 
technical terms. For example, the script will partition technical 
term like "ServiceContract", which consists of two words separated by
the uppercase "C", first partition into two words "Service" and 
"Contract". Second, both words will be hyphenated separately. In a 
third step, the hyphenation results will be concatenated with a 
separating LaTeX hyphen "\\-". Hence, the hyphenated version of 
"ServiceContract" will read "Ser\\-vice\\-Con\\-tract", which is LaTeX
conform.

The script may then be embedded as a macro in TeXstudio (see installation step
3 below) to realize in-place hyphenation of a selected word. The default 
hyphenation is American English (`en_US`). However, if your TeX file contains 
the language identifier in the format expected by TeXstudio 
(`% !TeX spellcheck = [LANG_ID]`) in its first line, `[LANG_ID]` is used as
language for the hyphenation.

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
with the content of the `ts_macro.js` file that is part of the repository.
Replace `[HYPHEN_FOLDER]` in the file with the path of the folder where you 
previously cloned `hyphen.py` to.
