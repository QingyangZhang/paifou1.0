#from django.conf.urls import url
from django.urls import path
from catalog import views

urlpatterns = [
    path('',views.index,name="index"),#主页
    path("page/<pindex>", views.indexp, name="page"),
    path('categories/<int:pk>/', views.category, name='category'),
    path('good/<pk>', views.GoodDetailView.as_view(), name='good-detail'),
    path('saler/<pk>', views.SalerDetailView.as_view(), name='saler-detail'),
]

urlpatterns += [
    path('viewCustomer',views.viewCustomer,name="viewCustomer"),
]

urlpatterns += [
    path('viewSaler',views.viewSaler,name="viewSaler"),
]

urlpatterns += [   
    path('registerCustomer', views.registerCustomer, name='registerCustomer'),
]