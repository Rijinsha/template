from.import views
from django.urls import path

urlpatterns = [

    path('register/',views.register,name='register'),  # if use single cods ,means print o/p in first,view.name means views page
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")
]