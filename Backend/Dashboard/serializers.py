from rest_framework import serializers
from Dashboard.models import Parta,Partb


class PartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parta
        fields = ('PartaId',
                  'TotalIncome',
                  'TotalLoss',
                  'Year')


class PartbSerializer(serializers.ModelSerializer):
     class Meta:
        model = Partb
        fields = ('PartbId',
                  'TotalExpenditure',
                  'BookingScore',
                  'Year')