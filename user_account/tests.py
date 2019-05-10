from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status 


class UserAccountTest(APITestCase):
    def setUp(self):
        self.test_user= User.objects.create_user('testcase','test@gmail.com','pwdtest13')
        self.create_url=reverse('account-create')

    def test_create_user(self):
        data={
            'username': 'aayush',
            'email':'test@abc.com',
            'password': 'pwdtest12'
        }
        #print (self.create_url)
        response= self.client.post(self.create_url, data, format='json')
        #print(response)
        '''its just for testing if the users are being successfully created
        here we try creating two users and returning indicators of the successful creation'''
        self.assertEqual(User.objects.count(),2)
        self.assertEqual(response.data['username'],data['username'])
        self.assertEqual(response.data['email'],data['email'])
        self.assertFalse('password' in response.data)


    #tests for password validation 
    def test_create_user_short_password(self):
        data={
            'username':'aayush1',
            'email':'testshortpwd@abc.com',
            'password':'short'
        }

        response=self.client.post(self.create_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(len(response.data['password']),1)


    def test_create_user_no_password(self):
        data={
            'username':'aayush2',
            'email':'testnopwd@abc.com',
            'password':''
        }

        response=self.client.post(self.create_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(len(response.data['password']),1)

    #tests for username validation 

    def test_create_user_long_username(self):
        data={
            'username':'aayush3'*20,
            'email':'longusername@abc.com',
            'password':'password1'
        }

        response=self.client.post(self.create_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(len(response.data['username']),1)

    def test_create_user_no_username(self):
        data={
            'username':'',
            'email':'nousername@abc.com',
            'password':'password2'
        }

        response=self.client.post(self.create_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(len(response.data['username']),1)


    def test_create_user_preexisting_username(self):
        data={
            #username put in same as the setUP function username 
            'username': 'testcase',
            'email':'preexisting_user@abc.com',
            'password': 'password3'
        }

        response=self.client.post(self.create_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(len(response.data['username']),1)


    #tests for email validation
    def test_create_user_preexisting_email(self):
        data={
            'username':'aayush4',
            'email':'test@gmail.com',
            'password':'password4'
        }

        response=self.client.post(self.create_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(len(response.data['email']),1)


    def test_create_user_invalid_email(self):
        data={
            'username':'aayush5',
            'email':'test',
            'password':'password5'    
        }

        response=self.client.post(self.create_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(len(response.data['email']),1)


    def test_create_user_no_email(self):
        data={
            'username':'aayush6',
            'email':'',
            'password':'password6'    
        }
        
        response=self.client.post(self.create_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(len(response.data['email']),1)
