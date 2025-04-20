import bcrypt

def checkPwd(password: str, hashed_pwd: str) -> bool:
  return bcrypt.checkpw(password.encode(), hashed_pwd.encode())

def generatePwdHash(password: str | bytes):
  if isinstance(password, str): password = password.encode()
  salt = bcrypt.gensalt(14)
  pwd_hash = bcrypt.hashpw(password, salt).decode()
  return pwd_hash