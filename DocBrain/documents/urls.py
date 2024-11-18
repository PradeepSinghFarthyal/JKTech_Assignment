from django.urls import path
from .api.ingestion_api import DocumentIngestionView
from .api.qa_api import QAView
from .api.selection_api import DocumentSelectionView


urlpatterns = [
    path('ingest-document/', DocumentIngestionView.as_view(), name='ingest-document'),
    path('qa/', QAView.as_view(), name='qa'),
    path('select-documents/', DocumentSelectionView.as_view(), name='select-documents'),
]