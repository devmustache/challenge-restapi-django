from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from core.models import Profile
from core.serializer import ProfileSerializer

class ProfileList(APIView):
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        queryset = Profile.objects.all()
        name_query_param = self.request.query_params.get('name', None)
        if name_query_param is not None:
            queryset = queryset.filter(first_name__icontains=name_query_param)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile_detailed = self.get_object(pk)
        serializer = ProfileSerializer(profile_detailed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile_detailed = self.get_object(pk)
        serializer = ProfileSerializer(profile_detailed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile_detailed = self.get_object(pk)
        profile_detailed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)