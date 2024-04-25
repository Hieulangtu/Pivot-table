from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


# the query
query= gql("""query{
  result: publicationPage{
    id
    name
    publicationtype {
      id
      name

    }
    authors{
      id
      order
      lastchange
      share
      valid
      user{
        id
        name
        surname
        email
      }
    }
    place
    publishedDate
    valid
    reference
    subjects {
      id
      name
    }
    
  }
  
}""")


#cookie Authorization 
cookie_auth_value = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiYWNjZXNzX3Rva2VuIjoiQUNDVC1ZeUVUdklwSTZ5cnBvMk40aDQwSWJmQmZ5T2kySjFUaCIsImV4cGlyZXNfaW4iOjM2MDAsInJlZnJlc2hfdG9rZW4iOiJSRUZULUNYV2JnblFZdk9uakdYMlV5N0ZKMG40b1JJNHhHckhJIiwidXNlcl9pZCI6IjJkOWRjNWNhLWE0YTItMTFlZC1iOWRmLTAyNDJhYzEyMDAwMyJ9.RgyPqjzVdvWOXUACO10uqwxQX77GnAND2QYf0HDI1AHzlByR_Xx8WDgWqFK8ILShDhwdNtPY-VgVe07rsLu2baNMl-C3zH2tx_lH2NrD5tBGU4lFMXKc83AVriskJK22uqPS22qMzixU0jUqpLBJYBfA_fM_DCpHDfxJfcZdp0J4DIV_obAUG83C_ES9mQk1gn2V8SUcHc-BeZVbPc9Z0BkJSB9R0xx4aXw7QDI_Tfy4ilaNDyqwm5_nq6Q3XIMqdd5NJcFngpP-u1owfN1Ll3VqAZfLi5I2upr1D6oMhdX-Z3lS8-xtHv2EHdud7U3c6QImiqCbqmXTqL69PSJShQ"

#refresh_token
refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1ODE4ZWYwMmI4Mjk5MzlhNWUyNTNlOSIsImlhdCI6MTcxMzIyMjc0NywiZXhwIjoxNzE1ODE0NzQ3fQ.LEvxwdPUC32nfkUt9cwzmivPNxrhD0S4a_6ylVhBnvA"



# the endpoint
transport = AIOHTTPTransport(url="http://localhost:33001/graphiql",headers={"Content-Type": "application/json", "Authorization": f"Bearer {refresh_token}"})

# Graphql Client
client = Client(transport=transport, fetch_schema_from_transport=True)

try:
    publication_data = client.execute(query)
    print(publication_data)
except Exception as e:
    print(f"Error: {e}")