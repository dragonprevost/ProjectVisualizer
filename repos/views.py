from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from repos.models import Repo
from repos.serializers import RepoSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def repo_list(request):
    if request.method == 'GET': 
        repos = Repo.objects.all()
        serializer = RepoSerializer(repos, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RepoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.erros, status=400)


@csrf_exempt
def repo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        repo = Repo.objects.get(pk=pk)
    except Repo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RepoSerializer(repo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RepoSerializer(repo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        repo.delete()
        return HttpResponse(status=204)
