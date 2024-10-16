from ninja import Schema

from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController


api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/users/", "users.api.router")

class UserSchema(Schema):
    country: str = None
    accountType: str = None
    email: str = None
    password: str = None
    username: str
    is_authenticated: bool


@api.get("/hello")
def hello(request):
    print(request)
    return {"message":"Hello World"}

@api.get("/me", response=UserSchema, auth=JWTAuth())
def me(request):
    return request.user