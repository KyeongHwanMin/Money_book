import requests

# TOKEN = '2c7cceae5684da55cd452871665ed77ad609233f'
JWT_TOKEN = ('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFt'
             'ZSI6InVzZXIyIiwiZXhwIjoxNjM3NDYxNzI3LCJlbWFpbCI6IiJ9.jyDNNcrZHxGQ'
             'KP7Q_zWbW6Fnr5Pzk8AzFHu5Fw6F3jU'
             )
#'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNjM3N드DYxNzI3LCJlbWFpbCI6IiJ9' 페이로드
headers = {
    # 'Authorization': f'Token {TOKEN}', # Token 인증
    'Authorization': f'JWT {JWT_TOKEN}',  # JWT 인증

}

res = requests.get('http://localhost:8000/Expense/', headers=headers)
print(res.json())
