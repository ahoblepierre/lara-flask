from dotenv import load_dotenv
import os
from app import create_app



# Charger les variables d’environnement
load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run()
