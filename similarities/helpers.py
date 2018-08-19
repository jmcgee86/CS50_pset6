from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    aLineSet = set(a.splitlines())
    bLineSet = set(b.splitlines())
    matchLineSet = aLineSet & bLineSet
    matchList = []
    matchList+=matchLineSet

    return matchList


def sentences(a, b):
    """Return sentences in both a and b"""
    aSentenceSet = set(sent_tokenize(a))
    bSentenceSet = set(sent_tokenize(b))
    matchSentenceSet = aSentenceSet & bSentenceSet
    matchSentenceList = []
    matchSentenceList += matchSentenceSet

    return matchSentenceList

def getSubstrings(string, n):
    """Return set of substrings of n length"""

    substringSet = set()
    i=0
    while i <= len(string)-n:
        j=i+n
        substringSet.add(string[i:j])
        i+=1
    return substringSet


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    aSubstringSet = getSubstrings(a,n)
    bSubStringSet = getSubstrings(b,n)
    matchSubStringSet = aSubstringSet & bSubStringSet
    matchSubstringList = []
    matchSubstringList += matchSubStringSet
    # TODO
    return matchSubstringList
