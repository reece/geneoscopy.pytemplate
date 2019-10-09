"""utilities used by geneoscopy.pytemplate"""


greetings = {
    "cn": "你好",
    "en": "hello",
    "es": "hola",
    "fr": "bonjour",
    "it": "ciao",
    }


def greeting(lang="en"):
    """returns "hello" or translation in specified language; returns in
    English by default or if language is not translated

    >>> greeting()
    'hello'
    
    >>> greeting("fr")
    'bonjour'

    >>> greeting("gr")          # Greek not supported
    'hello'

    """

    try:
        return greetings[lang]
    except KeyError:
        return greetings["en"]
