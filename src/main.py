import base36
import hmac, hashlib
from dotenv import load_dotenv
import os

def to_base36(decimal_number):
    return base36.dumps(decimal_number)

load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY not found in .env file")

if isinstance(SECRET_KEY, str):
    SECRET_KEY=SECRET_KEY.encode('utf-8')

def main():
    SEQUENTIAL_NUMBER=0 # This value should come from the database
    PREVIOUS = ""

    for i in range(200):
        base36 = to_base36(SEQUENTIAL_NUMBER)

        message = f"{base36}{PREVIOUS}".encode("utf-8")

        encrypted=hmac.new(SECRET_KEY,message,hashlib.sha256).hexdigest()
        
        print(f"Decimal: {SEQUENTIAL_NUMBER:>6} | Base36: {base36:>6} | HMAC: {encrypted[:12]}")

        SEQUENTIAL_NUMBER+=1
        PREVIOUS=encrypted

if __name__ == "__main__":
  main()
