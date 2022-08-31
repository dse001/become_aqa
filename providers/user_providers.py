from pydantic import BaseModel
# Home work!
class UsersExists(BaseModel):
    username : str
    id: int
    fakeusername : str
user_providers = """{
"username" : "defunkt",
"id" : 2,
"fakeusername" : "fghfhyfhgjgjg78ugjyujh"
}
"""
out = UsersExists.parse_raw(user_providers)





print(out.id)

