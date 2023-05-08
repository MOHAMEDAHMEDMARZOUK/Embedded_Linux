import facebook


# Set your access token and Facebook Page ID
access_token = 'EAADXGSQOFOcBAC3ZBTqs4ad8ZAGZB6nf6qUfQc0EMgxQJFiJA6bZBhZBCEBg0XYcgkId6nv5hyXBmoeBCwh1IZBEESaJG0DLXbZCmAN0NJYZCEiX0ZCd0PXtsnT5WnTN1VABTmZC1U4ZC98JEW5rblLmimzCykAhvCn1xR23Tt6JSZCkIukGsnAEcMZBoRVkoZCg6ZCyBlow1XnryJOZC6rZAVgJBUtMS'
page_id = '101208126012046'

# Create a GraphAPI object
graph = facebook.GraphAPI(access_token)

# Post to the page
graph.put_object(page_id, "feed", message="keep going...")





















'''
# Set up the access token and graph API object
access_token = 'EAAHdcz0fx9kBAMyy1wFmbZCg1mZBOic3hBKR87woZCf8HzVGjyg1OCpJ4tOW8Nb2zItUIqW1VH7W32kgM5xbyqp5WwDQqf2TXXtlJhAb1ZCOqos4fR5H2mypYbdZB75Uv2YojEtresQrzUUGp8kjXOWg1W48KIrTh3k6YkNjKBlRWtMiqweqxYOELwc8tOe2jmGBKTU0iSJW0rDA1Lmj0'
fb = facebook.GraphAPI(access_token)

# Define the message and post it to Facebook
message = 'Hello, world!'
fb.put_object(parent_object='me', connection_name='feed', message=message)
'''