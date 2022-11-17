from django.shortcuts import render
from .serializers import SignUpSerializer, TaskSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# class SignIn(APIView):
#      def post(self, request, format=None):
#         print("IN POST")
        
#             return Response({"Toke Is ":get_tokens_for_user(request.user)}, status=status.HTTP_201_CREATED)
#         return Response({}, status=status.HTTP_400_BAD_REQUEST)


class SignUp(APIView):
    """
    List all snippets, or create a new snippet.
    """
    # def get(self, request, format=None):
    #     snippets = QuestionCategory.objects.all()
    #     serializer = QCSerializer(snippets, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
        print("IN POST")
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BulkUpload(APIView):
     def post(self, request, format=None):
        print("IN POST")
        file_obj = request.FILES['file']
        if file_obj:
            print("file")
        else:
            print("NO FILE")


class AllTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("IN GET ALL")
        q = Task.objects.all() 
        q = TaskSerializer(q, many=True)
        return Response(q.data)
    def post(self, request, format=None):
            print("IN POST")
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, pk):
        print("IN GET")
        try:
            q = Task.objects.get(pk=pk) 
            print(request.user)        
        except:
            return Response({"error":"No data found"},status=status.HTTP_404_NOT_FOUND)
        q = TaskSerializer(q)
        return Response(q.data)


    def post(self, request, format=None):
        print("IN POST")
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        q = Task.objects.get(pk=pk)
        q = TaskSerializer(q, request.data)
        if q.is_valid():
            q.save()
            return Response(q.data)
        else:
            return Response(q.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        q = Task.objects.get(pk=pk) 
        q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
