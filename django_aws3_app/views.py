from rest_framework import viewsets, parsers
from .models import book_box
from .serializers import book_box_serializer


class book_box_view(viewsets.ModelViewSet):
    queryset = book_box.objects.all()
    serializer_class = book_box_serializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
