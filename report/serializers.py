from rest_framework import serializers
from report.models import *
from core.models import StudentModel

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

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['first_name','last_name']

class ScholaryearSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ScholarYear
        fields = ['id','label','dateStart','dateEnd']
        
class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['id','periodNum','dateStart','dateEnd','scholarYear','classeGroup','classeGroupLabel']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['scholarYear', 'classeGroup','periodNum'],
                message="Periode déjà existante !"
            )
        ]
    def validate(self,attrs):
        # overlaped = False
        data = self.initial_data
        print(f"SELF: {data}")
        print(f"current insert p-{data['periodNum']}: {data['dateStart']} => {data['dateEnd']}")
        num_of_periods = Period.objects.filter(classeGroup=data['classeGroup'],scholarYear=data['scholarYear']).count()
        period_exist = False if num_of_periods == 0 else True
        existingPeriods = Period.objects.filter(classeGroup=data['classeGroup'],scholarYear=data['scholarYear']).order_by('dateStart')
       
        ## Test Overlaping when have periods
        if (period_exist):
            for p in existingPeriods:
                print(f"p-{p.periodNum}: {p.dateStart} => {p.dateEnd} WITH new : {data['dateStart']} => {data['dateEnd']}")
                if (data['dateStart'] >= str(p.dateStart) and data['dateStart'] <= str(p.dateEnd)) or (data['dateEnd'] <= str(p.dateEnd) and data['dateEnd'] >= str(p.dateStart)):
                    # overlaped = True
                    print("overlaps !")
                    raise serializers.ValidationError("ATTETION: Un enchevauchement avec les dates de périodes a été detecté !")
                    # break 
            
        return attrs
        
class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = "__all__"
        
class ClasseGroupSerializer(serializers.ModelSerializer):
    # classes = serializers.StringRelatedField(many=True)
    classes = ClasseSerializer(many=True,read_only=True)
    
    class Meta:
        model = ClasseGroup
        # fields = "__all__"
        fields = ['id','studyYear','title','classes']
 
class StudentLevelSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    scholarYear = serializers.StringRelatedField()
    classe = serializers.StringRelatedField()
    
    class Meta:
        model = StudentLevel
        fields = ['id','student','classe','scholarYear']