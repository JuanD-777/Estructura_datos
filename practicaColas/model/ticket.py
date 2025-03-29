from pydantic import BaseModel

class Ticket(BaseModel):
    name: str # name of the person
    type: str # type of consultation
    identity: int # identity card
    case_description: str # description of the case
    age: int # age of the person
    priority_attention: bool = None # priority attention? True or False

   #contructor with default value for priority_attention
    # if age >= 60, priority_attention = True
    # if age < 60, priority_attention = False
    # if priority_attention is not provided, it will be set to True if age >= 60
    def __init__(self, **data):
        if "priority_attention" not in data or data["priority_attention"] is None:
            data["priority_attention"] = data["age"]>=60
        super().__init__(**data)