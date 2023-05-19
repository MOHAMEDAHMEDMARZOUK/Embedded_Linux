import os


def star ( size1 ) :
     os.system("cls")
     size = size1
     st = "*"
     sp = " "
     print( )
     print( )
     
     for x in range(size):
         print(( sp* (5*size - x )) + (st*(2*x+1)) )
     
     for x in range(size):
         print(( sp* (5*size)) + (st) )


def rotate_star(size1):
     os.system("cls")
     size = size1
     st = "*"
     sp = " "
     print( )
     print( )
     
     for x in range(size):
         print(( sp* (size)) + (st) )
     
     
     for x in range(size):
         print(( sp*x ) + (st*(2*x+1)) )


star(8) 
'''while True:
    z = 3
'''
















'''
# Set up the access token and graph API object
access_token = 'EAAHdcz0fx9kBAMyy1wFmbZCg1mZBOic3hBKR87woZCf8HzVGjyg1OCpJ4tOW8Nb2zItUIqW1VH7W32kgM5xbyqp5WwDQqf2TXXtlJhAb1ZCOqos4fR5H2mypYbdZB75Uv2YojEtresQrzUUGp8kjXOWg1W48KIrTh3k6YkNjKBlRWtMiqweqxYOELwc8tOe2jmGBKTU0iSJW0rDA1Lmj0'
fb = facebook.GraphAPI(access_token)

# Define the message and post it to Facebook
message = 'Hello, world!'
fb.put_object(parent_object='me', connection_name='feed', message=message)
'''