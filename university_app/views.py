from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
# from .modelserializer import *
from .serializer import *
import io
import copy


# def home(request):
# students = Student.objects.all()
# serializers = StudentSerializer(data=students, many=True)
# # json_data = JSONRenderer().render(serializers.data)
# if serializers.is_valid():
#     return Response(serializers.data, status=status.HTTP_200_OK)

# return HttpResponse(serializers.errors)
# return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# 
# def home(request):
#     course = Course.objects.all()
#     serializers = CourseSerializer(course, many=True)
#     json_data = JSONRenderer().render(serializers.data)
#     return HttpResponse(json_data, content_type='application/json')

def getFilterRecord(serializers):
    needed_list_main = []
    needed_item = {'name', 'course_name', 'college_name', 'department_name'}

    for s in serializers.data:
        in_dict = dict()
        for k, v in s.items():
            if k in needed_item:
                in_dict[k] = v
                # print(k, v)
        # print("----")
        # print(in_dict)     
        # new_dict = copy.deepcopy(in_dict)
        needed_list_main.append(copy.deepcopy(in_dict))
    
    return needed_list_main


@api_view() 
def get_all_student(request):
    students = Student.objects.all()
    serializers = StudentSerializer(students, many=True)
    # filtering only required fields
    needed_list_main = getFilterRecord(serializers)

    # print(needed_list_main)
    json_data = JSONRenderer().render(needed_list_main)
    return HttpResponse(json_data, content_type='application/json')


@api_view(['GET'])
def getStudent(request, pk=None):
    id = pk
    try:
        student = Student.objects.get(id=id)
        serializers = StudentSerializer(student)

        # needed_list_main = getFilterRecord(serializers)

        json_data = JSONRenderer().render(serializers.data)
        return HttpResponse(json_data, content_type='application/json')
    except Student.DoesNotExist:
        error = {"error": "Student does not exist"}
        json_data = JSONRenderer().render(error)
        return HttpResponse(json_data, content_type='application/json')
        # raise Http404("Student does not exist")


@api_view(['POST'])
def postStudent(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_native_data = JSONParser().parse(stream=stream)
    serializers = StudentSerializer(data=python_native_data)
    if serializers.is_valid():
        serializers.save()
        success = {"success": "Record created!"}
        json_data = JSONRenderer().render(success)
        return HttpResponse(json_data, content_type='application/json')
    error = {"error": "Error in the post data!"}
    json_error = JSONRenderer().render(error)
    return HttpResponse(json_error, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)


# -----------------------------------------------------------
"""
@api_view()
def get_all_student(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    return Response(serializer.data)
# class StudentListView(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

@api_view(['GET'])
def get_all_course(request):
    students = Course.objects.all()
    serializer = CourseSerializer()

"""
# -----------------------------------------------
""""
def home(request):
    query_set = Test.objects.all()
    context = {
        'queryset': query_set,
    }
    return render(request, 'index.html', context)


def success(request):
    return render(request, 'success.html')


def post(request):
    if request.method == "POST":
        name = request.POST["name"]
        if len(name) < 1:
            return render(request, 'error.html')
        obj = Test(name=name)
        obj.save()
        return HttpResponseRedirect('success')
    return render(request, 'error.html')
"""
