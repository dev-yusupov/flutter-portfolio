import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.base import Base, get_db

# Create test database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create test database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override get_db dependency
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create tables for the tests
Base.metadata.create_all(bind=engine)

# Define the test class
class TestAuth:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        Base.metadata.create_all(bind=engine) # Create a testing database enging
        self.client = TestClient(app)
        yield

        Base.metadata.drop_all(bind=engine) # Drop testing database after test

    def test_user_signup(self):
        """
        Test case for sigup endpoint
        """
        payload = {
            "username": "newuser",
            "password": "1234test",
        }
        response = self.client.post(url="/api/v1/auth/signup/", json=payload)

        assert response.status_code == 201
        assert response.json()["username"] == "newuser"

    def test_signup_with_existing_username(self):
        payload = {
            "username": "newuser",
            "password": "1234test",
        }

        self.client.post(url="/api/v1/auth/signup/", json=payload) # Send request to enpoint to create a new user

        response = self.client.post(url="/api/v1/auth/signup/", json=payload)

        assert response.status_code == 400
        assert response.json()["detail"] == "Username already registered"

    def test_user_login(self):
        # First, sign up the user
        signup_payload = {
            "username": "newuser",
            "password": "1234test",
        }
        self.client.post(url="/api/v1/auth/signup/", json=signup_payload)

        # Then, log in the user
        login_payload = {
            "username": "newuser",
            "password": "1234test",
        }
        response = self.client.post(url="/api/v1/auth/login/", data=login_payload)

        assert response.status_code == 200
        assert "access_token" in response.json()
        assert "refresh_token" in response.json()
        assert "token_type" in response.json()

    def test_login_incorrect_password(self):
        # First, sign up the user
        signup_payload = {
            "username": "newuser",
            "password": "1234test",
        }
        self.client.post(url="/api/v1/auth/signup/", json=signup_payload)

        # Then, try to log in with an incorrect password
        login_payload = {
            "username": "newuser",
            "password": "wrongpassword",
        }
        response = self.client.post(url="/api/v1/auth/login/", data=login_payload)

        assert response.status_code == 401
        assert response.json()["detail"] == "Incorrect username or password"