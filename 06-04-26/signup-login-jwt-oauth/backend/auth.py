from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "secret"   
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _normalize_password(password: str) -> str:
    if not password:
        return ""
    
    password = str(password).strip()
    password_bytes = password.encode("utf-8")[:72]
    
    return password_bytes.decode("utf-8", errors="ignore")

def hash_password(password: str):
    password = _normalize_password(password)
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    plain = _normalize_password(plain)
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)