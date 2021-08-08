from django.urls.conf import path
from .views import *
app_name="bookingapp"
urlpatterns = [
    path('home/',homepage,name='homepage'),
    path('about/',aboutpage,name='aboutpage'),
    path('signup/',signuppage,name="signuppage"),
    path('signin/',signin,name="signin"),
    path('signout/',signout,name="signout"),
    path('login_admin/',login_admin,name='login_admin'),
    path('loginpage/',loginpage,name='loginpage'),
    path('createAccount/',createAccount,name='createAccount'),
    path('adminhome/',adminhomepage,name='adminhome'),
    path('adddoctor/',adddoctorpage,name='adminaddDoctor'),
    path('viewdoctor/',viewdoctorpage,name='adminViewDoctor'),
    path('addreception/',addreceptpage,name='adminAddReceptionist'),
    path('viewreception/',viewreceptpage,name='adminViewreceptionist'),
    path('viewappointment/',viewappointpage,name='adminViewAppointment'),
    path('adminlogout/',adminlogoutpage,name='adminLogout'),
    path('logout/',logoutpage,name='logoutpage')
]
