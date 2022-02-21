from rest_framework import viewsets, filters
from core.models import Profile
from core.serializer import ProfileSerializer

class CustomSearchFilter(filters.SearchFilter):
    search_param = "name"

class ProfileViewSet(viewsets.ModelViewSet):
    #search_fields = ['first_name']
    #filter_backends = (CustomSearchFilter)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer