from rest_framework import serializers
from report.models import PeriodModel, CotationModel, NoteModel
from core.models import ResponsibleModel, StudentLevelCourseModel


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodModel
        fields = [
            "id",
            "period_label",
            "date_start",
            "date_end",
            "scholar_year",
            "classe_group",
            # "classe_group_label",
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=["scholar_year", "classe_group", "period_label"],
                message="Periode déjà existante !",
            )
        ]

    def validate(self, attrs):
        data = self.initial_data
        num_of_periods = PeriodModel.objects.filter(
            classe_group=data["classe_group"], scholar_year=data["scholar_year"]
        ).count()
        period_exist = False if num_of_periods == 0 else True

        if hasattr(self.instance, "pk"):
            existingPeriods = (
                PeriodModel.objects.filter(
                    classe_group=data["classe_group"], scholar_year=data["scholar_year"]
                )
                .order_by("date_start")
                .exclude(id=self.instance.pk)
            )
        else:
            existingPeriods = PeriodModel.objects.filter(
                classe_group=data["classe_group"], scholar_year=data["scholar_year"]
            ).order_by("date_start")

        ## Test Overlaping for each periods with same classe_group & scholar_year
        if period_exist:
            for p in existingPeriods:
                print(
                    f"p-{p.period_label}: {p.date_start} => {p.date_end} WITH new : {data['date_start']} => {data['date_end']}"
                )
                if (
                    data["date_start"] >= str(p.date_start)
                    and data["date_start"] <= str(p.date_end)
                ) or (
                    data["date_end"] <= str(p.date_end) and data["date_end"] >= str(p.date_start)
                ):
                    # overlaped = True
                    print("overlaps !")
                    raise serializers.ValidationError(
                        "ATTETION: Un enchevauchement avec les dates de périodes a été detecté !"
                    )
                    # break

        return attrs


class CotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotationModel
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ["id","note","comment","cotation","student_level","student_name","max_note"]
        # depth = 2

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=["cotation", "student_level"],
                
                message="élève déjà ajouté(e) dans la cotation",
            )
        ]
    
    def validate(self, attrs):
        print(attrs)
        if attrs["note"] > attrs["cotation"].max_note:
            raise serializers.ValidationError("La note est supérieur à la note maximale")
        elif attrs["note"] < 0:
            raise serializers.ValidationError("La note ne dois pas être inferieur à zéro")
        else:
            return attrs

class ResponsibleGivenCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsibleModel
        fields = ["id","first_name","last_name","courses"]
        # fields = "__all__"  
        depth = 2
            
class StudentLevelCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLevelCourseModel
        fields = ["id","date_start","date_end","student_level"]
        depth = 2