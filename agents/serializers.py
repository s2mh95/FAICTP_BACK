from rest_framework import serializers
from .models import Agent, Mission

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class MissionSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Mission
        fields = '__all__'
        extra_kwargs = {
            'mission_date': {'input_formats': ['%Y-%m-%d']}
        }

    def validate(self, data):
        if self.instance:
            return data  
        if 'assigned_agent' not in data or data['assigned_agent'] is None:
            raise serializers.ValidationError("Assigned agent is required.")
        return data

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop('created_by', None)
        return super().update(instance, validated_data)