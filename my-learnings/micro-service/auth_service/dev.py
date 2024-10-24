from app import application
from dotenv import load_dotenv
import os

load_dotenv()

if __name__=="__main__":
    application.run(host=os.getenv('HOST'),port=os.getenv('PORT'),debug=True)