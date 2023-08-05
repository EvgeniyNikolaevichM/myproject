from rest_framework import routers
from lawAPI.views import *


router = routers.SimpleRouter()
router.register(r'system', systemViewSet)
router.register(r'platform', platformViewSet)
router.register(r'law', lawViewSet)

