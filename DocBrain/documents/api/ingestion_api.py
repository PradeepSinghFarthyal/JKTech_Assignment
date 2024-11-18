from rest_framework.views import APIView
from rest_framework.response import Response
from documents.tasks import generate_and_store_embeddings
from rest_framework import status

class DocumentIngestionView(APIView):
    """
    Document Ingestion API. For the time being we consider user can submit only submit the text.

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    Also we can use authentication_classes and permission_classes for authentaction and authorization
    """
    
    def post(self, request):
        try:
            document_data = request.data.get("document_data")
            if not document_data:
                return Response({"error": "No document data provided."}, status=status.HTTP_400_BAD_REQUEST)
            task = generate_and_store_embeddings.delay(document_data)
            return Response({"status": "Processing", "task_id": task.id}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"status":"failed","response": str(e)}, status = status.HTTP_404_NOT_FOUND)