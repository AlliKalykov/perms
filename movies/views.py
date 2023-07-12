from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from .models import Movie, Saloon, Ticket
from .permissions import IsOwnerOrReadOnly, IsSuperuser, ReadOnly, IsStaff
from .serializers import MovieSerializer, SaloonSerilizer, TicketSerializer
from .pagination import CustomPagination
from .filters import MovieFilter


class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    pagination_class = CustomPagination
    permission_classes = [ReadOnly | IsSuperuser]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [ReadOnly | IsSuperuser]


class SaloonViewSet(ModelViewSet):
    serializer_class = SaloonSerilizer
    queryset = Saloon.objects.all()


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = [ReadOnly | IsStaff]

    def perform_create(self, serializer):
        # Assign the user who created the ticket
        serializer.save(creator=self.request.user)
