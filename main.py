from src.py_text_analyzer import PyTextAnalyzer
from src.data_requester import request_reddit_data
import random
import asyncio

async def main():
    processor = PyTextAnalyzer()

    #comments = request_reddit_data(30)
    for i in range(5):
        with open('comments_to_read.txt', 'r') as f:

            for line in f.readlines():
                text = processor.process(line).get()
                print(text)

            rn = random.choice([7,8,9,10,1])
            print(f"time to sleep {rn}")
            await asyncio.sleep(rn)

if __name__ == "__main__":
    asyncio.run(main())