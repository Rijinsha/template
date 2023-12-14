from.import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),  # if use single cods ,means print o/p in first,view.name means views page
    # chek  demo name
   # path('xyz/',views.xyz,name='xyz'), # if use any name and / ,prit o/p in this section only use urlcode+xyz
   # path('passing/',views.passing,name='passing value'),
    #path('abc/',views.abc,name='abc'),
   # path('add/',views.result,name='result')
]