from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SharewishEntry
from .serializers import SharewishEntrySerializer

@api_view(['POST'])
def create_sharewish_entry(request):
    try:
        serializer = SharewishEntrySerializer(data=request.data)
        print(request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)