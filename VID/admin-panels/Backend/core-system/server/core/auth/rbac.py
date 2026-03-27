from fastapi import HTTPException, Security, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decodeJWT

auth_scheme = HTTPBearer()

async def get_current_user(token: HTTPAuthorizationCredentials = Security(auth_scheme)):
    payload = decodeJWT(token.credentials)
    if not payload:
        raise HTTPException(status_code=403, detail="Invalid token or expired token")
    return payload

class RoleChecker:
    def __init__(self, allowed_roles: list):
        self.allowed_roles = allowed_roles

    def __call__(self, user: dict = Depends(get_current_user)):
        if user["role"] not in self.allowed_roles:
            raise HTTPException(status_code=403, detail=f"Role '{user['role']}' is not allowed for this action")
        return user
