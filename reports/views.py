from datetime import date

from rest_framework.permissions import IsAuthenticated

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from reports.models import TransactionReport, TransactionReportType

from .serializers import ReportSerializer, TransactionReportSerializer, TransactionReportTypeSerializer


class TransactionReportTypeCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionReportTypeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "TransactionReportType created successfully."}, status=status.HTTP_201_CREATED,
                        headers=headers)


class TransactionReportTypeDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TransactionReportType.objects.all()
    serializer_class = TransactionReportTypeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "TransactionReportType deleted successfully."}, status=status.HTTP_200_OK)


class TransactionReportCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionReportSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "TransactionReport created successfully."}, status=status.HTTP_201_CREATED,
                        headers=headers)


class TransactionReportDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TransactionReport.objects.all()
    serializer_class = TransactionReportSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "TransactionReport deleted successfully."}, status=status.HTTP_200_OK)


class MonthlySummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        report = TransactionReport.generate_monthly_summary(user, date.today().year, date.today().month)
        serializer = ReportSerializer(report)
        return Response({"message": "Monthly summary retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)


class CategoryExpenseReportAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        report = TransactionReport.generate_category_expense_report(user, date.today().year, date.today().month)
        serializer = ReportSerializer(report)
        return Response({"message": "Category expense report retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
