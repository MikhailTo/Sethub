from datetime import datetime
import hashlib

class Users:
    users = [
        {
            "id": 101,
            "name": "JohnDoe",
            "email": "johndoe@example.com",
            "hashed_password": hashlib.sha256("password123".encode()).hexdigest()
        },
        {
            "id": 102,
            "name": "RemoteGuru",
            "email": "remoteguru@example.com",
            "hashed_password": hashlib.sha256("workfromhome".encode()).hexdigest()
        },
        {
            "id": 111,
            "name": "StartupFanatic",
            "email": "startupfanatic@example.com",
            "hashed_password": hashlib.sha256("entrepreneur123".encode()).hexdigest()
        },
        {
            "id": 112,
            "name": "TravelEnthusiast",
            "email": "travelenthusiast@example.com",
            "hashed_password": hashlib.sha256("wanderlust".encode()).hexdigest()
        },
        {
            "id": 113,
            "name": "HealthyEater",
            "email": "healthyeater@example.com",
            "hashed_password": hashlib.sha256("nutritious123".encode()).hexdigest()
        },
        {
            "id": 114,
            "name": "WebDevPro",
            "email": "webdevpro@example.com",
            "hashed_password": hashlib.sha256("javascript123".encode()).hexdigest()
        },
        {
            "id": 115,
            "name": "ProductivityNinja",
            "email": "productivityninja@example.com",
            "hashed_password": hashlib.sha256("efficient123".encode()).hexdigest()
        },
        {
            "id": 116,
            "name": "BookWorm42",
            "email": "bookworm42@example.com",
            "hashed_password": hashlib.sha256("readmore123".encode()).hexdigest()
        },
        {
            "id": 117,
            "name": "NatureExplorer",
            "email": "natureexplorer@example.com",
            "hashed_password": hashlib.sha256("hikingtrails".encode()).hexdigest()
        },
        {
            "id": 118,
            "name": "CinemaGeek",
            "email": "cinemageek@example.com",
            "hashed_password": hashlib.sha256("moviebuff123".encode()).hexdigest()
        }
    ]

    @classmethod
    def get_user_by_id(cls, user_id):
        return next((user for user in cls.users if user["id"] == user_id), None)

    @classmethod
    def get_user_by_email(cls, email):
        return next((user for user in cls.users if user["email"] == email), None)

# Example of token generation (you would typically use a more secure method in production)
def generate_token(user_id):
    return {
        "access_token": f"fake_token_{user_id}_{datetime.now().timestamp()}",
        "token_type": "bearer"
    }