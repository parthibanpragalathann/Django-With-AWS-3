from rest_framework import parsers
from .models import book_box
from .serializers import book_box_serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class book_box_list(APIView):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post']
    """
    List all book_boxes or create a new book_boxes.
    """
    def get(self, request, format=None):
        book_boxes = book_box.objects.all()
        serializer = book_box_serializer(book_boxes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = book_box_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class book_box_detail(APIView):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'put', 'delete']
    """
    Retrieve, update or delete a book_boxes instance.
    """
    def get_object(self, pk):
        try:
            return book_box.objects.get(pk=pk)
        except book_box.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book_boxes = self.get_object(pk)
        serializer = book_box_serializer(book_boxes)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book_boxes = self.get_object(pk)
        serializer = book_box_serializer(book_boxes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book_boxes = self.get_object(pk)
        book_boxes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)