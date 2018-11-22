"""
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
"""

from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', include('repos.urls')),
]
