from ..src.py_text_analyzer import PyTextAnalyzer

analyzer = PyTextAnalyzer()

def test_py_text_analyzer_get_word_list():
    analyzer.process("test test test")
    assert analyzer.get_words_list() == ['test', 'test', 'test']


def test_py_text_analyzer_get_text():
    analyzer.process("test test test")
    assert analyzer.get() == "test test test"

def test_py_text_analyzer_map():
    map = analyzer.process("test test test").map_words(lambda element: '/' + element + '/').get_words_list()
    assert map == ['/test/', "/test/", "/test/"]

def test_py_text_analyzer_filter():
    filter = analyzer.process("test tall tisana").filter_words(lambda element: 'e' in element).get_words_list()
    assert filter == ['test']

def test_py_text_analyzer_reduce():
    reduce = analyzer.process("test tall tisana").reduce_words(lambda acc, element: acc + element + "1" if element == 'tisana' else acc).get()
    assert reduce == "tisana1"

def test_py_text_analyzer_chained_methods():
    chain = analyzer.process("test tast toast").map_words(lambda element: '/' + element + '/').filter_words(lambda element: 'e' in element).reduce_words(lambda acc, element: acc + element + "1" if element == '/test/' else acc).get()
    assert chain == "/test/1"

def test_py_text_analyzer_words_count():
    count = analyzer.process("test tall tisana").words_count()
    assert count == 3