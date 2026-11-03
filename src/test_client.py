import requests

requests1 = requests.get('http://localhost:8080/')
requests2 = requests.get('http://localhost:8080/api/cars')
requests3 = requests.get('http://localhost:8080/api/manufacturers')
requests4 = requests.get('http://localhost:8080/api/cars/prices')

print(f"/api/cars:\n{requests1.json()}")
print(f"\n/api/cars:\n{requests2.json()}")
print(f"\n/api/manufacturers:\n{requests3.json()}")
print(f"\n/api/cars/prices:\n{requests4.json()}")