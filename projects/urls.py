
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    # Agrega los elementos de router.urls a la lista urlpatterns usando el operador de concatenación '+'
] + router.urls