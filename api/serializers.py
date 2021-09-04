from rest_framework import serializers
from .models import Room


#creating data in json format

class RoomSerializer(serializers.ModelSerializer):

    #'anything that's not a field'

    class Meta:

        model = Room

        #id is auto generated
        fields = ('id','code','host','skipVotes','guestCanPause','timeCreated')


class CreateRoomSerializer(serializers.ModelSerializer):

    class Meta:

        model = Room

        fields = ('guestCanPause','skipVotes')

class UpdateRoomSerializer(serializers.ModelSerializer):


    #redefine code field to bypass room code is unique error

    code = serializers.CharField()

    class Meta:
                
         model = Room

         fields = ('guestCanPause','skipVotes','code')
              
