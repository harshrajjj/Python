from pydantic import BaseModel, field_validator,model_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def validate_username(cls, value):
        if len(value) < 5:
            raise ValueError('Username must be at least 5 characters long')
        return value
    

class signup(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')#after validation of all fields
    def check_passwords_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values
        