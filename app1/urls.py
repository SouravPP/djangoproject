from operator import index
from django.urls import path
from . import views
app_name='app1'
urlpatterns=[ 
    path('hello/',views.hello,name='hello'),
    path('signup/',views.signup,name='signup'),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('display_table/',views.display_table,name='display_table'),
    path('update/<int:id>',views.update,name='update'),
    path('remove/<int:id>',views.remove,name='remove'),
]