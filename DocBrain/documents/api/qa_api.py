from rest_framework.views import APIView
from rest_framework.response import Response
from documents.rag_engine import retrieve_and_generate_answer
from rest_framework import status

class QAView(APIView):

    def post(self, request):
        try:
            question = request.data.get("question")
            document_ids = request.data.get("document_ids", [])
            if not question:
                return Response({"error": "Question not provided."}, status=status.HTTP_400_BAD_REQUEST)
            answer = retrieve_and_generate_answer(question, document_ids)
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"failed","response":str(e)},status = status.HTTP_400_BAD_REQUEST)
