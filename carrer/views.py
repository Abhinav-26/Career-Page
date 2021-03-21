from django.shortcuts import render, redirect
from django.http import HttpResponse
from carrer import models
from carrer import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'carrer/index.html')

def main(request):
    return render(request, 'carrer/jobsPage.html')

def jobsPgae(request,call="No"):
    data = []
    objs = models.Jobs.objects.all()
    for i in objs:
        data.append(i.educationLevel)

    return render(request, 'carrer/jobsPage.html', context={'levels':data,'call':call})


class getAllJobs(APIView):
    def get(self, request, *args, **kwargs):
        data = []
        objs=models.Jobs.objects.all()
        for i in objs:
            data.append(serializers.JobSerializer(i).data)
        return Response(data)


class getJob(APIView):
    def get(self, request, *args, **kwargs):
        _id = request.GET.get('id')
        obj = models.Jobs.objects.get(id=_id)
        print(serializers.JobSerializer(obj).data)
        return Response(dict(serializers.JobSerializer(obj).data))


class ApplicationView(View):
    def post(self, request, *args, **kwargs):
        obj = models.Application(resume=request.FILES.get('resume'),
            name=request.POST.get('name'),mob=request.POST.get('mobile'),
            mailID=request.POST.get('email'),job=models.Jobs.objects.get(id=request.POST.get('id')))
        obj.save()

    
        # return JsonResponse({'success':'true'}, safe=False)
        return jobsPgae(request,call="yes")
