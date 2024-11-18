# rag_engine.py
import openai
import os
import torch
from .models import Embedding
from .api.serializers import Embedding_serializer


# Set up OpenAI API Key
openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_embedding(text, provider="openai"):
    """
    This function is basically use for generate the embedding with the help of any API/Tool.
    So currently we are using openapi default. but if we need any others then will add the code in below methods
    if provider="openai":
        execute openai code
    else:
        execut other code
    """
    try:
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=text
        )

        embedding = response['data'][0]['embedding']
        return embedding
    except Exception as e:
        print("Error occur while generate embedding : ",e)



def generate_answer(question, context, provider="openai"):
    
    """This function is used for generate answers, currently openai is used for answer generations"""    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Answer questions based on context."},
                {"role": "user", "content": f"Context: {context}"},
                {"role": "user", "content": f"Question: {question}"}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return answer
    except Exception as e:
        print("Error while generate answer : ", e)



def retrieve_and_generate_answer(question, document_ids=None, provider="openai"):
    """
    This function is used for retrive the data form db if exists. Otherwise Generate the embeddings.
    Currently we use openai for default. if we have to use any other in future than will do it. 
    """
    try:
        if document_ids:
            embeddings = Embedding.objects.filter(doc_id__in=document_ids)
            embeddings = Embedding_serializer(embeddings)
            embeddings = embeddings.data
        else:
            embeddings = generate_embedding(question, provider=provider) #Embedding.objects.all()      
        return embeddings
    except Exception as e:
        print("Error while generate answer : ", e)