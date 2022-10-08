from rest_framework import serializers
from api.models import Reviews

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    qty=serializers.IntegerField()
    def validate(self,data):
        price=data.get("price")
        print("price",price)
        if price not in range(50,1000):
            raise serializers.ValidationError("invalid price")
        return data



class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.DateField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"
        # exclude=("created_date",)
# fields=["book","user","comment","rated"]
