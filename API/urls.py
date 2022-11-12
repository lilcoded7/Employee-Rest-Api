from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




urlpatterns = [
    path('', views.RegisterAPIView.as_view(), name="register"), 
    path('registerEmployee/', views.EmployeeRegister.as_view(), name="registerEmployee"), 
    path('EmployeeDetails/<int:pk>/', views.EmployeeDetails.as_view(), name='EmployeeDetails'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh')
]