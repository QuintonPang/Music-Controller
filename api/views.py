from django.shortcuts import render
from rest_framework import generics,status
from .serializers import RoomSerializer, CreateRoomSerializer, UpdateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import time


# Create your views here.

#ListCreateAPIView shows json data and form to insert data 
#CreateAPIView shows form to insert data
#ListAPIView shows data ONLY

class RoomView(generics.ListAPIView):

    #overriding two methods


    #get all rooms from database

    #queryset is necessary, name cannot be changed

    queryset = Room.objects.all()

    #serializer_class is necessary, name cannot be changed

    serializer_class = RoomSerializer

class GetRoomView(APIView):

    serializer_class = RoomSerializer

    #obtain code from url
    #The URL keyword argument that should be used for object lookup. The URL conf should include a keyword argument corresponding to this value. 

    lookup_url_kwargs = 'code'

    #format : You use them in your URLs to append a suffix content type format(HTML, JSON or API), for example, you want 'html' format of response

    def get(self, request, format=None):

        code = request.GET.get(self.lookup_url_kwargs)

        #if there is a code
        
        if code!=None:

            room = Room.objects.filter(code=code)

            #if room which that code exists

            if len(room)>0:

                #get data from json
                data = RoomSerializer(room[0]).data

                #set value using key (just like dict)
                #check if the person in current session is the owner of said room
                data['isHost'] = self.request.session.session_key==room[0].host

                return Response(data, status=status.HTTP_200_OK)

            #no such room

            return Response({'Room not found':'Invalid room code'},status=status.HTTP_404_NOT_FOUND)


        #no code in url

        return Response({'Bad request':'Code parameter not found in url'},status=status.HTTP_404_NOT_FOUND)



                
class JoinRoomView(APIView):
 
                                                  
         
        def post(self, request, format=None):  
            

                    if not self.request.session.exists(self.request.session.session_key): 

                        self.request.session.create()


                    code = request.data.get('code')            
                

                    if code!=None:                                                                                                                          
                        room = Room.objects.filter(code=code)                       
                         
                        if len(room)>0:


                            self.request.session['roomCode'] = code

                            return Response({'message':'Room Joined'},status=status.HTTP_200_OK)

                    #no such room                                                                                                                  
                    
                        return Response({'Room not found':'Invalid room code'},status=status.HTTP_404_NOT_FOUND)                                

                                   

                     #no code in url                                                                                                                 
                
                    return Response({'Bad request':'Code not obtained'},status=status.HTTP_404_NOT_FOUND)

class CreateRoomView(APIView):

    queryset = Room.objects.all()

    #not neccessary

    serializer_class = CreateRoomSerializer

    def post(self,request,format=None):

        #if a session with the key(host) doesn't exist, create one

        if not self.request.session.exists(self.request.session.session_key):

            self.request.session.create()

        #insert data
        
        serializer = self.serializer_class(data=request.data)
            
        if serializer.is_valid():

            guestCanPause = serializer.data.get('guestCanPause')
            skipVotes = serializer.data.get('skipVotes')
            #host is key name of session
            host = self.request.session.session_key
            
            #check to see if it exists before or not
            queryset = Room.objects.filter(host=host)

            #if exists, update fields

            if queryset.exists():

                room = queryset[0]
                room.guestCanPause = guestCanPause
                room.skipVotes = skipVotes
                room.save(update_fields=['guestCanPause','skipVotes'])

                self.request.session['roomCode'] = room.code

                #redirect to updated data
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)

            else:

                room = Room(host=host,guestCanPause=guestCanPause,skipVotes=skipVotes)
                room.save()

                self.request.session['roomCode'] = room.code
            
                #redirect to created data

                return Response(RoomSerializer(room).data, status = status.HTTP_200_OK)

        #if everything fails
       
      
        return Response({'Bad request':'Invalid data!'},status = status.HTTP_400_BAD_REQUEST)

class UserInRoom(APIView):

    def get(self,request,format=None):

        print("userinroom")

        if not self.request.session.exists(self.request.session.session_key):

            self.request.session.create()

           
        data = { 'code' : self.request.session.get('roomCode') }

            

        return JsonResponse(data,status=status.HTTP_200_OK)


class UserLeaveRoom(APIView):

     def post(self,request,format=None):

        print("userleaveRoom")

        if 'roomCode' in self.request.session:
            
            print(self.request.session.get('roomCode'))

            self.request.session.pop('roomCode')

            host = self.request.session.session_key

            roomToDelResults = Room.objects.filter(host=host)

            if len (roomToDelResults) > 0:

                roomToDel = roomToDelResults[0]
                roomToDel.delete()

                print("done deleting")

        return Response({'message','You have left the room'},status=status.HTTP_200_OK)



class UpdateRoomView(APIView):

        

            
        #not neccessary

                
        serializer_class = UpdateRoomSerializer

        #patch is for update

                   
        def patch(self,request,format=None):


                                


        #if a session with the key(host) doesn't exist, create one

                                        


              if not self.request.session.exists(self.request.session.session_key):

                                                        

              
                    
                  self.request.session.create()

                

                                                                      

              

                
              serializer = self.serializer_class(data=request.data)
              print (serializer.initial_data)
              
                                                                               

              if serializer.is_valid():

                       
                        # a host may have two codes so must search based on code

                                           
                        code = serializer.data.get('code')
                        
                        
                        guestCanPause = serializer.data.get('guestCanPause')
                                                                                                               
                                                                                                                                  
                        skipVotes = serializer.data.get('skipVotes')
                                                                                                                                 
                                                                                                                #host is key name of session
                                                                                                                                       
                                                                                                                                  
                        host = self.request.session.session_key

                                                                                                                #check to see if it exists before or not
                                                                              

                        queryset = Room.objects.filter(code=code)


                        if queryset.exists():

                                                
                                           



    
                                                room = queryset[0]


                                                if room.host != host: 

                                                    return Response({'msg': 'You are not the host of this room.'}, status=status.HTTP_403_FORBIDDEN)

                                                                                                                                                                                                                         
                                                room.guestCanPause = guestCanPause
                                                
                                                room.skipVotes = skipVotes
                                                                                                                                                                                                                                                    
                                                room.save(update_fields=['guestCanPause','skipVotes'])                                                                               
                                                                                                                                                                                                                                                        
                                                self.request.session['roomCode'] = room.code

                                                                                                                                                                                                                                
                                                                                                                               
                                                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)

                                                                                                                                                                                                                           
                        return Response({'Error','Room not found'}, status=status.HTTP_404_NOT_FOUND)

                                                                                                                                    


                                                                                                                                                                                              
              print (serializer.errors)
              return Response({'Bad request':'Invalid data!'},status = status.HTTP_400_BAD_REQUEST)

