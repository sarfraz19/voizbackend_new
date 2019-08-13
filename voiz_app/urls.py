from django.urls import path
from .import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usersbynum', views.UserViewSetByNum)
router.register(r'usersbyusername', views.UserViewSetByUsername)
router.register(r'users', views.UserViewSet)
router.register(r'customersbynum', views.Customer1ViewSetByNum)
router.register(r'plan', views.Plan1ViewSetByNum)
router.register(r'array', views.MyDBArrayViewSetByNum)
router.register(r'prepaid', views.PrepaidPlanViewSetByNum)
router.register(r'postpaid', views.PostpaidPlanVIewSetByNum)
router.register(r'dongle', views.Dongle2VIewSetByNum)

urlpatterns = [

    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('createaccount', views.createaccount, name="createaccount"),
    path('newconnection', views.newconnection, name="newconnection"),
    path('pay', views.pay, name="pay"),
    path('prepaid', views.prepaid, name="prepaid"),
    path('postpaid', views.postpaid, name="postpaid"),



    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
