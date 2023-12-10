from rest_framework import serializers
from .models import TransactionReport, TransactionReportType


class TransactionReportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionReportType
        fields = ['name']


class TransactionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionReport
        fields = "__all__"


class ReportSerializer(serializers.Serializer):
    user = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()
