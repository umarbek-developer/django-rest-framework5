from rest_framework.viewsets import ModelViewSet
from .models import Vazifa5
from .serializers import Vazifa5Serializer


class Vazifa5ViewSet(ModelViewSet):
    queryset = Vazifa5.objects.all()
    serializer_class = Vazifa5Serializer
