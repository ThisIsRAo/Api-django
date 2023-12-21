from django.urls import path
from .views import StudentList,SignInView
urlpatterns=[
    path('signin/',SignInView.as_view()),
    # path('student/',StudentList.as_view())

]
