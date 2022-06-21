from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    login: str
    first_name: str
    last_name: str
    password: str
    email: EmailStr | None


class UserOut(BaseModel):
    login: str
    first_name: str
    last_name: str
    email: EmailStr | None

