from django.contrib.auth import authenticate
import json

import base64
import csv

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import StudentSerializer,UserSerializer
from rest_framework.generics import ListAPIView

from .models import Student

def get_auth_for_user(user):
    tokens=RefreshToken.for_user(user)
    return {
        'user': UserSerializer(user).data
        # 'message':'hiii'
    }




# Create your views here.
class SignInView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')



        # number_a=int(request.data.get('number_a'))
        # number_b=int(request.data.get('number_b'))
        # sum_number=number_a+number_b
        message=str(request.data.get('new_message'))
        final_repy=str('')


        def image_to_json(image_path):
            with open(image_path, "rb") as image_file:
                # Encode the image as base64
                encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

            # Create a JSON object with the encoded image
            # json_data = {
            #     "image": encoded_image
            # }

            return encoded_image
        #
        #
        # # Example data
        # data_csv = [
        #     [message, "Age", "City"],
        #     ["om",20,"akola"]
        # ]
        #
        # # Specify the CSV file name
        # csv_file_name = "example.csv"
        #
        # # Write data to the CSV file
        # with open(csv_file_name, mode='a', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(data_csv)
        #
        # # if not username or not password:
        # #     return Response(status=400)
        # #
        # # user=authenticate(username=username,password=password)
        # # if not user:
        # #     return Response(status=401)
        # #
        # # user_data=get_auth_for_user(user)
        # data = {
        #     'sum':f'{'ye to work kr raha hai'}'
        # }
        # response_message={
        #     'message': f'{message}'
        # }
        # # print(image_to_json('D:/All Programing Information/pycharm all projects data/django_mark_1/Main/api/atom_logo.jpg'))
        # # return Response(image_to_json('D:/All Programing Information/pycharm all projects data/django_mark_1/Main/api/profile.png'))
        # # return Response(data)
        if(message=='Hii'):
            final_repy='Hello Sir How I can Help You'
            response_message = {
                'type': 'text',
                'message': f'{final_repy}'
            }
            pass
        elif(message=='send me image'):
            response_message = {
                'type': 'image',
                'message':image_to_json('D:/All Programing Information/pycharm all projects data/django_mark_1/Main/api/atom_logo.jpg')
            }
        elif(message=='what is your name'):
            final_repy='I am pre Train NLP model for GPM Collage'
            response_message = {
                'type': 'text',
                'message': f'{final_repy}'
            }
        elif (message == 'send other image'):
            response_message = {
                'type': 'image',
                'message': image_to_json(
                    'D:/All Programing Information/pycharm all projects data/django_mark_1/Main/api/energy.png')
            }

        else:
            final_repy='Sorry sir '
            response_message = {
                'type': 'text',
                'message': f'{final_repy}'
            }





        return Response(response_message)



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer