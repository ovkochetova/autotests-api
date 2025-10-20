import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()
print(f"Status code:", login_response.status_code)
access_token = login_response_data['token']['accessToken']
print(f"Access token:", access_token)

client = httpx.Client(headers = {"Authorization": f"Bearer {access_token}"})
response = client.get("http://127.0.0.1:8000/api/v1/users/me" )

print(f"Status code:", response.status_code)
print(f"Response json:", response.json())

