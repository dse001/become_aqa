from pydantic import BaseModel
# Home work!
class GenderData(BaseModel):
    name_male: str
    name_female: str
    name_number: int

gender_providers = """{
"name_male" : "ben",
"name_female" : "clara",
"name_number" : 999999
}
"""
name = GenderData.parse_raw(gender_providers)





#print(out.name_female)