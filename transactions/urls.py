from django.urls import path
from .views import (
    TransactionCreateView,
    TransactionListView,
    TransactionDetailView,
    TransactionUpdateView,
    TransactionDeleteView
)

urlpatterns = [
    path('create/', TransactionCreateView.as_view(), name='transaction-list-create'),
    path('list/', TransactionListView.as_view(), name='transaction-list'),
    path('detail/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction-detail'),

]
