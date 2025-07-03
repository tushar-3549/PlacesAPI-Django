from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaceNestedView(APIView):
    def get(self, request):
        districts = District.objects.prefetch_related(
            'subdistricts__unions__semi_metros'
        ).all()
        data = {
            district.name: DistrictCustomSerializer(district).data
            for district in districts
        }
        return Response(data)


class DistrictViewSet(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class SubDistrictViewSet(ModelViewSet):
    queryset = SubDistrict.objects.all()
    serializer_class = SubDistrictSerializer


class UnionViewSet(ModelViewSet):
    queryset = Union.objects.all()
    serializer_class = UnionSerializer


class SemiMetroAreaViewSet(ModelViewSet):
    queryset = SemiMetroArea.objects.all()
    serializer_class = SemiMetroAreaSerializer

