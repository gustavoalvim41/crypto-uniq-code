import base36
import hmac, hashlib
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY not found in .env file")

if isinstance(SECRET_KEY, str):
    SECRET_KEY=SECRET_KEY.encode('utf-8')

SEQUENTIAL_NUMBER=0 # This value should come from the database

for i in range(50):
    to_base36=base36.dumps(SEQUENTIAL_NUMBER)

    encrypted=hmac.new(SECRET_KEY,to_base36.encode('utf-8'),hashlib.sha256).hexdigest()
    
    print(f"Decimal: {i:>6} | Base36: {to_base36:>6} | HMAC: {encrypted[:10]}")
    
    SEQUENTIAL_NUMBER+=1
