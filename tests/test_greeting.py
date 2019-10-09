from geneoscopy.pytemplate.utils import greeting

def test_greetings():
    assert "hello" == greeting()
    
    assert "bonjour" == greeting("fr")
    assert "hello" == greeting("en")
    assert "你好" == greeting("cn")

def test_greetings_failures():
    assert "hello" == greeting("bogus")
