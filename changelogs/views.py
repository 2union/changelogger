from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer


def index(request):
    template = loader.get_template("changelogs/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def all_projects(request):
    template = loader.get_template("changelogs/all_projects.html")
    all_projects_list = Project.objects.all()
    context = {"all_projects_list": all_projects_list}
    return HttpResponse(template.render(context, request))


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
