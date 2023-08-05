from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from lawAPI.serializers import *
from systemStewartPlatform.models import *


class systemViewSet(ModelViewSet):
    queryset = system_stewart_platform.objects.all()
    serializer_class = systemSerializer
    # permission_classes = (IsAuthenticated, ) определен в Settings глобально

class platformViewSet(ModelViewSet):
    queryset = stewart_platform.objects.all()
    serializer_class = platformSerializer
    # permission_classes = (IsAuthenticated, ) определен в Settings глобально

class lawViewSet(ModelViewSet):
    queryset = law_for_platform.objects.all()
    serializer_class = lawSerializer
    # permission_classes = (IsAuthenticated, ) определен в Settings глобально
