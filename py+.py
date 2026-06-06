import requests

session = requests.Session()

data = {
     "username": "im mr robot",
     "password": "10105"
}
try:
 for i in range(999):
     r = session.get(
         "https://ujian.smkmuhapen.sch.id",
          params=data
     )
     print(i)

except requests.RequestException:
    print("POST gagal, lanjut aja")

print(r.status_code)



