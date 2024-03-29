from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Transactions, UserBalance
from .serializers import TransactionSerializer, UserBalanceSerializer


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response({"detail": "Transaction created successfully."},
                        status=status.HTTP_201_CREATED
                        )


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Transactions.objects.filter(user=self.request.user)

        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__name=category)

        ordering = self.request.query_params.get('ordering', None)
        if ordering is not None:
            queryset = queryset.order_by(ordering)

        return queryset


class TransactionDetailView(generics.RetrieveAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transactions.objects.filter(user=self.request.user)


class TransactionUpdateView(generics.UpdateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transactions.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
        updated_data = serializer.data
        return Response({"detail": "Transaction updated successfully.",
                         "updated_data": updated_data},
                        status=status.HTTP_200_OK
                        )


class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transactions.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Transaction deleted successfully."},
                        status=status.HTTP_200_OK
                        )


class UserBalanceAPIView(generics.RetrieveAPIView):
    serializer_class = UserBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserBalance.objects.filter(user=self.request.user)