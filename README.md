# Money Book API
<br>

### 개요
소비내역을 기록/관리하는 API

### 필요

- Python 3.9.x
- Docker
  <br>

## 서버 구동 방법

1. Python 종속성 설치
```
pip install -r requirements.txt
```

2. MySQL 5.7 컨테이너 실행
```bash
docker-compose up -d
```

3. DB 마이그레이션
> 설계된 모델에 대한 스키마를 데이터베이스에 반영

```bash
python manage.py migrate
```

4. 서버실행
```bash
python manage.py runserver
```

### Dockerfile 이미지 생성
```bash
docker build -t <이미지 이름>
```

### Docker Container 실행
```bash
docker run -itd <이미지 이름>
```


### API Specifications
##### 회원가입
- Request

POST /account/register-user
```json
{
  "name" : "test",
  "email" : "email@email.com",
  "password" : "1234"
}
```
- Response
```json
{
    "name" : "test",
    "email" : "email@email.com"
}
```

- Error

| 에러코드 | 설명 |
| --- | --- |
| 400 | 파라미터 입력이 잘못된 경우  |
| 401 | 중복된 username이 입력된 경우|

##### 로그인
- Request

POST /account/register-user
```json
{
  "email" : "email@email.com",
  "password" : "1234"
}
```
- Response
```json
{
  "success": "로그인성공"
}
```

- Error

| 에러코드 | 설명 |
| --- | --- |
| 400 | 등록된 user가 없는 경우  |
| 401 | Username or Password 틀릴경우 |


##### 로그아웃
- Request

POST /account/register-user

- Response
```json
{
  "success": "로그아웃 되었습니다."
}
```
##### 금액, 메모 삽입
- Request

POST /expense/

```json
{
  "amount": 100,
  "memo": "teset_memo"
}
```
- Response
```json
{
  "pk": 6,
  "email": "email@email.com",
  "amount": 100,
  "memo": "test_memo",
  "spent_at": "2021-11-25T02:48:20.048201Z",
  "updated_at": "2021-11-25T02:48:20.048440Z"
}    
```

##### 나의 지출내역 목록조회
- Request

GET /expense/

- Response
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "pk": 6,
      "email": "email@email.com",
      "amount": 100,
      "memo": "test_memo",
      "spent_at": "2021-11-25T02:48:20.048201Z",
      "updated_at": "2021-11-25T02:48:20.048440Z"
    }
  ]
}
```

##### 나의 지출내역 상세조회
- Request
  GET /account/register-user
```json
{

}
```
- Response
```json
{
    
}
```

- Error

| 에러코드 | 설명 |
| --- | --- |
| |   |
|  | |
##### 나의 지출내역, 메모 수정
- Request

PATCH /expense/'pk'/
```json
{
  "amount": 2,
  "memo": "test2"
}
```
- Response
```json
{
  "pk": 7,
  "email": "email@email.com",
  "amount": 2,
  "memo": "test2",
  "spent_at": "2021-11-25T03:11:27.185208Z",
  "updated_at": "2021-11-25T03:27:05.634965Z"
}
```

##### 나의 지출내역 삭제
- Request

DELETE /expense/'pk'/

- Response
```json
{
  HTTP 204 No Content
}
```
##### 나의 삭제된 지출내역 목록조회
- Request

GET /expense/?is_deleted=true
- Response
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "pk": 6,
      "email": "email@email.com",
      "amount": 100,
      "memo": "test_memo",
      "spent_at": "2021-11-25T02:48:20.048201Z",
      "updated_at": "2021-11-25T03:17:23.373457Z"
    }
  ]
}
```

##### 나의 삭제된 지출내역 복구
- Request

POST /expense/'pk'/restore/

- Response
```json
{
  "pk": 7,
  "email": "email@email.com",
  "amount": 2,
  "memo": "test2",
  "spent_at": "2021-11-25T03:11:27.185208Z",
  "updated_at": "2021-11-25T03:59:13.489565Z"
}
```