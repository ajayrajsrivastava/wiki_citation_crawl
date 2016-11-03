The user provides the URL of the Wiki article he wants to crawl.
He is provided with two queries :

1-Get Lines which have the given citation.
2-Get Citations of a particular lines.

For query of type '1': All the a-tags which have 'href' attribute of type -> '#cite_note-*\w*-+'+citation+'\$' (Reference Link)
are taken and the text portion of their parent's parent ('sup'->'p'-paragraph) is converted to type 'str' from unicode.The sentence from paragraph('para') is then extracted using another regex pattern 'citPattern'.

NOTE:
The extracted text is added to a set (unique elements) and then printed(unordered) since a paragraph may contain more than one same citation. Also, a defintion setLink() is used in the beginning to add an element '$' in the end of 'href' of all a-tags to denote end of the regex pattern 'refPattern'. Example: Regex for '#cite_note-\w-+' + '1' gives #cite_note-Kruger-11,#cite_note-Kruger-12,#cite_note-Kruger-13 etc , therefore,#cite_note-Kruger-1$ is used.

```html
<p> 
    " Paragraph Containing Citation "
    <sup class="reference"> 
        <a href="#cite_note-*\w*-+'+citation+'\$"> </a> 
    </sup> 
</p> 

```
For query of type '2' : Format assumption -> "Lines"(.," anything)[1] or "Lines"(.," anything)[1][2][3]..(Multiple Citations) . Function getCitation(lines) calculates startIndex( denoting '[' ) = index of lines in paragraph (if found) + skips 1 index(for .," or anything ) and passes it to function printCitation(startIndex,para) which calculates endIndex (denoting ']' ) & prints the citation number enclosed within square brackets. NOTE : Function printCitation(startIndex,para) extracts text table 'td' if not found in 'p' element. The function is recursively called in case of multiple citations.
