
from passlib.context import CryptContext
import jwt
from fastapi.security import OAuth2PasswordBearer

"""
SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']
 
 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
def verify_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)
 
 
def get_password_hash(password):
   return pwd_context.hash(password)
 
def authenticate_user(db, email: str, password: str):
   user = crud.get_user_by_email(db, email)
   if not user:
   	return False
   if not verify_password(password, user.hashed_password):
   	return False
   return user




 
def create_access_token(*, data: dict, expires_delta: timedelta = None):
   to_encode = data.copy()
   if expires_delta:
   	expire = datetime.utcnow() + expires_delta
   else:
   	expire = datetime.utcnow() + timedelta(minutes=15)
   to_encode.update({"exp": expire})
   encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
   return encoded_jwt

def decode_access_token(db, token):
   credentials_exception = HTTPException(
   	status_code=HTTP_401_UNAUTHORIZED,
   	detail="Could not validate credentials",
   	headers={"WWW-Authenticate": "Bearer"},
   )
   try:
   	payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
   	email: str = payload.get("sub")
   	if email is None:
       	raise credentials_exception
   	token_data = schemas.TokenData(email=email)
   except PyJWTError:
   	raise credentials_exception
   user = crud.get_user_by_email(db, email=token_data.email)
   if user is None:
   	raise credentials_exception
   return user

   @app.post("/api/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db),
                      	form_data: OAuth2PasswordRequestForm = Depends()):
   #generate access token for valid credentials
   user = authenticate_user(db, form_data.username, form_data.password)
   if not user:
   	raise HTTPException(
       	status_code=HTTP_401_UNAUTHORIZED,
       	detail="Incorrect email or password",
       	headers={"WWW-Authenticate": "Bearer"},
   	)
   access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
   access_token = create_access_token(data={"sub": user.email},
                                  	expires_delta=access_token_expires)
   return {"access_token": access_token, "token_type": "bearer"}"""