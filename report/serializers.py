from rest_framework import serializers
from report.models import PeriodModel


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodModel
        fields = [
            "id",
            "period_num",
            "date_start",
            "date_end",
            "scholar_year",
            "classe_group",
            # "classe_group_label",
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=["scholar_year", "classe_group", "period_num"],
                message="Periode déjà existante !",
            )
        ]

    def validate(self, attrs):
        # TODO : if modifying object exclude it from queryset.
        # overlaped = False
        data = self.initial_data
        print(f"SELF: {data}")
        print(f"current insert p-{data['period_num']}: {data['date_start']} => {data['date_end']}")
        num_of_periods = PeriodModel.objects.filter(
            classe_group=data["classe_group"], scholar_year=data["scholar_year"]
        ).count()
        period_exist = False if num_of_periods == 0 else True
        existingPeriods = PeriodModel.objects.filter(
            classe_group=data["classe_group"], scholar_year=data["scholar_year"]
        ).order_by("date_start")

        ## Test Overlaping when have periods
        if period_exist:
            for p in existingPeriods:
                print(
                    f"p-{p.period_num}: {p.date_start} => {p.date_end} WITH new : {data['date_start']} => {data['date_end']}"
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
