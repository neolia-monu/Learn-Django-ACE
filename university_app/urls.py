from django.urls import path, include
from . import views
from .classview import *
from . import functionview
from . import new_view
from .functionview import *
from .new_view import StudentView

# from .views import StudentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student', new_view.StudentView, basename='student')


urlpatterns = [
    # path('success', views.success, name='success'),
    # path('', new_view.StudentView.as_view(), name='getAll'),
    # path('', include(router.urls)),
    # path('', StudentAPI.as_view()),
    path('', functionview.getAll),
    # path('api/student/<int:pk>', StudentAPI.as_view()),
    path('api/<int:pk>', functionview.getStudent),
    path('post', functionview.post),
    path('put/<int:pk>', functionview.put),
    path('patch/<int:pk>', functionview.patch),
    path('delete/<int:pk>', functionview.delete)
    # path('getStudent/<int:pk>', views.getStudent, name='getStudent'),
    # path('post', views.postStudent, name='post'),
    # path('students', views.get_all_student, name='getAll'),
    # path('update/<int:pk>', views.partial_data, name='put')
]