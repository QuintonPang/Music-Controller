from django.shortcuts import render

# Create your views here.

#def foo(*positional, **keywords): 

    #print "Positional:", positional

    #print "Keywords:", keywords 

#The *positional argument will store all of the positional arguments passed to foo(), with no limit to how many you can provide.

#>>> foo('one', 'two', 'three') 
#Positional: ('one', 'two', 'three') 
#Keywords: {} 

#The **keywords argument will store any keyword arguments:

# >>> foo(a='one', b='two', c='three')
#Positional: () 
#Keywords: {'a': 'one', 'c': 'three', 'b': 'two'} 

#And of course, you can use both at the same time:

#>>> foo('one','two',c='three',d='four') 
#Positional: ('one', 'two') 
#Keywords: {'c': 'three', 'd': 'four'}
#not neccessary

def App(response,*args,**kwargs):

    return render(response,'frontend/index.html')


