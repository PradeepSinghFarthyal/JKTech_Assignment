from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from documents.models import *
from .serializers import Embedding_serializer

class DocumentSelectionView(APIView):
    def post(self, request):

        try:
            doc_ids = request.data.get("doc_ids") # user provide multiple doc id's
            if not doc_ids:
                return Response({"error": "No document IDs provided."}, status=status.HTTP_400_BAD_REQUEST)
            data = Embedding.objects.filter(doc__in = doc_ids)
            if data.exists():
                serializer = Embedding_serializer(data,many=True)
                return Response({"status": "Selection updated", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Document ID's not exists."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":"failed","response":str(e)},status = status.HTTP_400_BAD_REQUEST)
