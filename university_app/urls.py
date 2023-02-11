from django.urls import path, include
from . import views
from .classview import *
from . import functionview
from . import new_view
from .functionview import *
from .new_view import StudentView
from . import generic_mixins_views
from .generic_mixins_views import *
from . import concrete_api_views

# from .views import StudentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('student', new_view.StudentView, basename='student')
# router.register('student', generic_mixins_views.StudentList, basename='stu')

urlpatterns = [
    # path('success', views.success, name='success'),
    # path('', new_view.StudentView.as_view(), name='getAll'),
    # path('', include(router.urls)),
    # path('', StudentAPI.as_view()),
    # path('', functionview.getAll),
    # path('api/student/<int:pk>', StudentAPI.as_view()),
    # path('', generic_mixins_views.StudentList.as_view()),
    # path('get/<int:pk>', generic_mixins_views.StudentRetrieve.as_view()),
    # path('post', generic_mixins_views.StudentCreate.as_view()),
    # path('patch/<int:pk>', generic_mixins_views.StudentPartial.as_view()),
    # path('put/<int:pk>', generic_mixins_views.StudentUpdate.as_view()),    
    # path('delete/<int:pk>', generic_mixins_views.StudentDelete.as_view())
    path('', concrete_api_views.StudentList.as_view()),
    path('get/<int:pk>', concrete_api_views.StudentRetrieve.as_view()),
    path('post', concrete_api_views.StudentCreate.as_view()),
    path('patch/<int:pk>', concrete_api_views.StudentUpdate.as_view()),
    path('put/<int:pk>', concrete_api_views.StudentUpdate.as_view()),    
    path('delete/<int:pk>', concrete_api_views.StudentDelete.as_view())
    # path('api/<int:pk>', functionview.getStudent),
    # path('post', functionview.post),
    # path('put/<int:pk>', functionview.put),
    # path('patch/<int:pk>', functionview.patch),
    # path('delete/<int:pk>', functionview.delete)
    # path('getStudent/<int:pk>', views.getStudent, name='getStudent'),
    # path('post', views.postStudent, name='post'),
    # path('students', views.get_all_student, name='getAll'),
    # path('update/<int:pk>', views.partial_data, name='put')
]