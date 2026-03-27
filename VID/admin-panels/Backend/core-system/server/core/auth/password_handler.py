from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_token, hashed_token):
    return pwd_context.verify(plain_token, hashed_token)

def get_password_hash(token):
    return pwd_context.hash(token)
