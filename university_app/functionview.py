from rest_framework.decorators import api_view
# from .serializer import *
from .modelserializer import * 
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io

@api_view(['GET'])
def getStudent(request, pk=None):
    id = pk
    try:
        student = Student.objects.get(id=id)
        serializers = StudentSerializer(student)
        json_data = JSONRenderer().render(serializers.data)
        return HttpResponse(json_data, content_type='application/json')
    except Student.DoesNotExist:
        error = {"error": "Student does not exist"}
        json_data = JSONRenderer().render(error)
        return HttpResponse(json_data, content_type='application/json')

@api_view(['GET'])
def getAll(request):
    students = Student.objects.all()
    serializers = StudentSerializer(students, many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['POST'])
def post(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    student = JSONParser().parse(stream=stream)
    serializers = StudentSerializer(data=student)
    if serializers.is_valid():
        serializers.save()
        success = {'success' : 'Successfully record inserted'}
        return HttpResponse(success, content_type='application/json')
    error = {'error': 'post data is not valid'}
    return HttpResponse(error, content_type='application/json')

@api_view(['PUT'])
def put(request, pk=None):
    student = Student.objects.get(id=pk)
    serializers = StudentSerializer(student, request.data)
    if serializers.is_valid():
        serializers.save()
        success = {'success' : 'Successfully record updated'}
        return HttpResponse(success, content_type='application/json')
    error = {'error': 'update data is not complete'}
    return HttpResponse(error, content_type='application/json')


@api_view(['PATCH'])
def patch(request, pk=None):
    students = Student.objects.get(id=pk)
    serializers = StudentSerializer(students, request.data, partial=True)
    if serializers.is_valid():
        serializers.save()
        success = {'success' : 'Successfully partial record updated'}
        return HttpResponse(success, content_type='application/json')
    error = {'error': 'parital update data is not complete'}
    return HttpResponse(error, content_type='application/json')


@api_view(['DELETE'])
def delete(request, pk=None):
    student = Student.objects.get(id=pk)
    student.delete()
    return HttpResponse({'success': "Record deleted successfully"})
