from src.py_text_analyzer import PyTextAnalyzer
from src.data_requester import request_reddit_data

if __name__ == "__main__":
    processor = PyTextAnalyzer('I love this place, I really appreciate each moment of my life!!!')

    comments = request_reddit_data(25)

    for comment in comments:
        processor.process(comment.body)