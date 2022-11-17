from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignUp, BulkUpload, TaskView, AllTaskView
# from rest_framework.simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('signIn/',SignIn.as_view(), name="signIn"),
    path("SignUp", SignUp.as_view(), name="SignUp"),
    path("BulkUpload", BulkUpload.as_view(), name="BulkUpload"),
    path("task/<int:pk>", TaskView.as_view(), name="task"),
    path("tasks", AllTaskView.as_view(), name="tasks"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # from rest_framework.simplejwt.views import TokenObtainPairView

]