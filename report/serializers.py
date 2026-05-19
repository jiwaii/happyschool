from rest_framework import serializers
from report.models import *

# class ScholarYearSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     label = serializers.CharField()
#     dateStart = serializers.DateField()
#     dateEnd = serializers.DateField()

#     def create(self, validated_data):
#         return ScholarYear.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.label = validated_data.get('label',instance.label)
#         instance.dateStart = validated_data.get('dateStart',instance.dateStart)
#         instance.dateEnd = validated_data.get('dateEnd',instance.dateEnd)
#         return instance

class ScholaryearSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ScholarYear
        fields = ['id','label','dateStart','dateEnd']
        
class PeriodSerializer(serializers.ModelSerializer):
       class Meta:
        model = Period
        fields = ['id','periodNum','dateStart','dateEnd','scholarYear','classeGroup','classeGroupLabel']
        
class ClasseGroupSerializer(serializers.ModelSerializer):
    classes = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = ClasseGroup
        # fields = "__all__"
        fields = ['studyYear','title','classes']

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = "__all__"