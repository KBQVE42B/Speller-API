# Word Speller RESTful API
# date : 10/9/1402
from fastapi import FastAPI

# FastAPI Object
api = FastAPI()

# path operation decorator
@api.get('/speller/{word}')
def speller(word):

    # spelling that word and push it to a list and creating a response body
    spelled_word = [letter for letter in str(word)]
    response = {"Word" : word,
                "Spelled Word" : spelled_word}
    
    return response
