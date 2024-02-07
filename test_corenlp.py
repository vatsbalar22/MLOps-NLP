from nlplogic.corenlp import get_phrases,get_text_blob,summarize_wikipedia,search_wikipedia

def test_get_phrases():
    assert 'golden state' in get_phrases('Golden State Warriors')