
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('become-teacher/',views.become_teacher,name='become_teacher'),
    path('become-student/',views.become_student,name='become_student'),
    path('accounts/login/',views.signin,name='signin'),
    path('teachers/',views.teachers,name='teachers'),
    path('signout/',views.signout,name='signout'),
]