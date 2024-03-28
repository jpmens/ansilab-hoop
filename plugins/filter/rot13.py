import codecs

# ROT13 of string `s' 
def rot13(s):
    return codecs.encode(s, 'rot_13')

# Word Count of `s'; `cl' is class: 'chars', 'words', or 'lines'
def wc(s, cl='c'):
    
    if cl.startswith("l"):
        return s.count('\n')
    elif cl.startswith("w"):
        return len(s.split())
    return len(s)

class FilterModule(object):

    def filters(self):
        return {
            'rot13'     : rot13,
            'wc'        : wc,
            'wordcount' : wc,
        }
