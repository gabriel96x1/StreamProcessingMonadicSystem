from src.py_text_analyzer import PyTextAnalyzer
from src.data_requester import request_reddit_data

if __name__ == "__main__":
    processor = PyTextAnalyzer()

    comments = request_reddit_data(25)

    for comment in comments:
        text = processor.process(comment.body).get()
        print(text)