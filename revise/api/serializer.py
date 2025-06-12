from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     city = serializers.CharField(max_length=200)
#     roll = serializers.IntegerField()
    
#     def validate_roll(self,value):
#         if value>100:
#             raise serializers.ValidationError("Roll cannot be greater than 100!")
#         return value
    
#     def validate(self, data):
#         name = data.get('name')
#         city = data.get('city')
#         if name.lower() == 'rohit' and city.lower()!= 'india':
#             raise serializers.ValidationError("Rohit is an Indian!")
#         return data
        
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        read_only_fields = ['id']
    
    def validate_roll(self,value):
        if value > 200:
            raise serializers.ValidationError("Can not admit more than 200 students")
        return value
    
    def validate(self,data):
        name = data.get('name')
        city = data.get('city')
        if city.lower() == 'israel':
            raise serializers.ValidationError("There is no country named Israel")
        return data