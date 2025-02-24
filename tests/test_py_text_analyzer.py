
from ..src.py_text_analyzer import PyTextAnalyzer

def test_py_text_analyzer_init():
    analyzer = PyTextAnalyzer("test test test")
    assert analyzer.tokens() == ['test', 'test', 'test']

def test_py_text_analyzer_map():
    analyzer = PyTextAnalyzer("test test test")
    map = (analyzer.map(lambda element: '/' + element + '/'))
    assert map == ['/test/', "/test/", "/test/"]

def test_py_text_analyzer_filter():
    analyzer = PyTextAnalyzer("test tall tisana")
    filter = (analyzer.filter(lambda element: 'e' in element))
    assert filter == ['test']

def test_py_text_analyzer_reduce():
    analyzer = PyTextAnalyzer("test tall tisana")
    reduce = (analyzer.reduce(lambda acc, element: acc + element + "1" if element == 'tisana' else acc))
    assert reduce == "tisana1"