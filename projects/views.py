from django.shortcuts import render
from rest_framework import viewsets
from projects.models import Profile, Project
from projects.serializers import ProfileSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
            profile = self.get_object()

            return render(
                request,
                'profile_detail.html',
                {
                    'profile': profile,
                }
            )
        return super().retrieve(request, *args, **kwargs)
        



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
