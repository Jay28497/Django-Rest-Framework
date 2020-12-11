from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ClassBaseAPIView.views import EmployeeViewSet

router = DefaultRouter()
router.register('employee_list', EmployeeViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
