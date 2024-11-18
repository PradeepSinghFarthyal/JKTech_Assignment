# tasks.py
from celery import shared_task
from .models import Document, Embedding
from .rag_engine import generate_embedding

@shared_task
def generate_and_store_embeddings(document_data):
    embedding = generate_embedding(document_data)  # generates embedding
    doc = Document.objects.create(content=document_data)
    Embedding.objects.create(doc_id=doc.id, vector=embedding)
