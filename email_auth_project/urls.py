
from django.contrib import admin
from django.urls import path
from eoapp.views import home,viewtask,createtask,delete
from auapp.views import user_signup,user_login,user_logout,user_np,user_cp
from fbapp.views import user_fb
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path('viewtask/',viewtask,name = 'viewtask'),
    path('createtask/',createtask,name = 'createtask'),
    path('delete/<int:id>',delete,name = 'delete'),   
    path("user_signup/",user_signup,name="user_signup"),
    path("user_login/",user_login,name="user_login"),
    path("user_logout/",user_logout,name="user_logout"),
    path("user_np/",user_np,name="user_np"),
    path("user_fb/",user_fb,name="user_fb"),
    path("user_cp/",user_cp,name="user_cp"),
]
