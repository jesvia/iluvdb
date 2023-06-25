from rest_framework import serializers
from watchlist.models import Watchlist, StreamPlatform


class WatchlistSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = Watchlist
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
class StreamPlatformSerializer(serializers.ModelSerializer):
     class Meta:
        model = StreamPlatform
        fields = '__all__'
    
    # def get_len_name(self, object):
    #     return len(object.name)
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name too short man")
    #     else:
    #         return value
        
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Desc can't be same")
    #     return data
    

# def name_length(value):
#     if len(value) < 2:
#             raise serializers.ValidationError("Name too short man")
#     return value 
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name =serializers.CharField(validators = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name too short man")
#     #     else:
#     #         return value
        
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Desc can't be same")
#         return data