from django.db import models

#for string.ascii_uppercase
import string

#for random.choices
import random

# Create your models here.

def createCode():

    length = 6

    # keeps on generating code until break is called(which is when it is unique)

    while True:

        #random.choices takes k items(characters) from string list, then join method joins them together to form a string with 6 characters

        code = ''.join(random.choices(string.ascii_uppercase,k=length))

        if Room.objects.filter(code=code).count()==0:

            break #stops when the code generated is unique

    return code
        


class Room(models.Model):

    code = models.CharField(max_length=8,unique=True,default=createCode)
    host = models.CharField(max_length=50,unique=True)
    skipVotes = models.IntegerField(default=1,null=False)
    guestCanPause = models.BooleanField(default=False,null=False)
    timeCreated = models.DateTimeField(auto_now_add=True) #auto_now_add means set to the time it was created

    currentSong = models.CharField(max_length=50, null=True)
