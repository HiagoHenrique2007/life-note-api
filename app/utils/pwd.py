import bcrypt

def checkPwd(username: str, password: str) -> bool:
  pass

def generatePwdHash(password: str | bytes):
  if isinstance(password, str): password = password.encode()
  salt = bcrypt.gensalt(14)
  pwd_hash = bcrypt.hashpw(password, salt).decode()
  return pwd_hash