import requests

# Test /degrees endpoint
r = requests.get('http://127.0.0.1:5000/degrees')

# Check status code (should be 200 for success)
print(f"Status code: {r.status_code}")  # Should print 200

# Check raw content
print(f"Content type: {type(r.content)}")  # Should be bytes
print(f"Content: {r.content}")  # Will show raw bytes

# Check JSON decoded content
print(f"JSON type: {type(r.json())}")  # Should be list
print(f"JSON content: {r.json()}")  # Will show Python list of dictionaries

print(f"Headers: {r.headers}")  # Will show all headers including Content-Type: application/json

# # Test /degrees/<id>/degrees endpoint
# r2 = requests.get('http://127.0.0.1:5000/degrees/1/degrees')

# print(f"\nFor /degrees/1/degrees:")
# print(f"Status code: {r2.status_code}")  # Should be 200
# print(f"Content type: {type(r2.content)}")  # Should be bytes
# print(f"JSON content: {r2.json()}")  # Should show {'degrees': 5725}
# print(f"Headers: {r2.headers}")

# # Test invalid ID
# r3 = requests.get('http://127.0.0.1:5000/degrees/99/degrees')
# print(f"\nFor invalid ID:")
# print(f"Status code: {r3.status_code}")  # Should be 404
# print(f"JSON content: {r3.json()}")  # Should show error message






