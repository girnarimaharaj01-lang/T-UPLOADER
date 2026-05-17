import os

API_ID    = os.environ.get("API_ID", "29777466")
API_HASH  = os.environ.get("API_HASH", "a04b3df726520026f207079aec2f9879")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8463395750:AAEZwDq7gVps8YZvfm0g6kLHftQIIKqv3qw") 
TOTAL_USER = os.environ.get('TOTAL_USERS', '8399557684').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 10000 if not set
