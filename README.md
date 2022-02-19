# Money Book API

<br>

### 개요


소비내역을 기록/관리하는 API

### 필요

- Python 3.9.x
- Docker
  <br>

## 서버 구동 방법

### 로컬환경 서버 구동

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

5. 서버 정상 구동 확인

웹 브라우저에서 http://127.0.0.1:8080 로 접속하여 페이지가 나온다면 정상적으로 서버 구동된 것입니다.

<br>

### 도커환경 서버구동

1. 이미지 빌드

```bash
docker build -t pay_here_server .
```

2. 컨테이너 실행

```bash
docker run -itd -p 8181:8080 pay_here_server
```

3. 서버 정상 구동 확인

웹 브라우저에서 http://127.0.0.1:8181 로 접속하여 페이지가 나온다면 정상적으로 서버 구동된 것입니다.



## API Specifications

### 회원가입

[요청]

- URL: POST /account/register-user/

- Body

```json
{
  "name" : "test",
  "email" : "email@email.com",
  "password" : "1234"
}
```

[응답]

- Body

```json
{
    "name" : "test",
    "email" : "email@email.com"
}
```

- Error

| 에러코드 | 설명                          |
| -------- | ----------------------------- |
| 400      | 파라미터 입력이 잘못된 경우   |
| 401      | 중복된 username이 입력된 경우 |



### 로그인

- [요청]

- URL: POST /account/login/

- Body

```json
{
  "email" : "email@email.com",
  "password" : "1234"
}
```

[응답]

- Body

```json
{
  "success": "로그인성공"
}
```

- Error

| 에러코드 | 설명                          |
| -------- | ----------------------------- |
| 400      | 등록된 user가 없는 경우       |
| 401      | Username or Password 틀릴경우 |



### 로그아웃

[요청]

- URL: POST /account/logout/

[응답]

- Body

```json
{
  "success": "로그아웃 되었습니다."
}
```





### 지출내역 입력

[요청]

- URL : POST /expense/



- Body

```json
{
  "amount": 100,
  "memo": "teset_memo"
}
```



- Body 파라미터 설명

  - amount : 지출한 금액을 의미합니다. 0 이상의 정수로만 입력해야 합니다.

  - memo : 메모를 의미합니다. 텍스트를 입력해야 합니다.



[응답]

- Body

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

- 응답에 대한 설명

  - 성공 응답시 상태코드 : 200

  - 응답 Body 설명 : 지출내역(expense) 이 생성된 결과가 반환됩니다.







### 나의 지출내역, 메모 수정

[요청]

- URL:PATCH /expense/:pk/
  - Path 파라미터 설명 : pk 는 expense의 식별 아이디를 입력합니다



- Body

```json
{
  "amount": 2,
  "memo": "test2"
}
```

- Body 파라미터 설명
  - amount : 지출한 금액을 의미합니다. 0 이상의 정수로만 입력해야 합니다.
  - memo : 메모를 의미합니다. 텍스트를 입력해야 합니다.

[응답]

- Body

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

- 응답에 대한 설명
  - 성공 응답시 상태코드 : 200
  - 응답 Body 설명 : 지출내역(expense) 이 수정된 결과가 반환됩니다.



### 나의 지출내역 삭제

[요청]

- URL: DELETE /expense/:pk/

  - Path 파라미터 설명 : pk 는 expense의 식별 아이디를 입력합니다

  

[응답]

- Body

```json
{
  HTTP 204 No Content
}
```

- Body 파라미터 설명

  - 내역이 삭제 됩니다.

    

### 나의 삭제된 지출내역 조회

[요청]

- URL: GET /expense/?is_deleted=true



[응답]

- Body

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

- 응답에 대한 설명

  - 성공 응답시 상태코드 : 200

  - 응답 Body 설명 : 삭제된 지출내역(expense)의 결과가 반환됩니다.

    

### 나의 삭제된 지출내역 복구

[요청]

- URL: POST /expense/:pk/restore/
  - Path 파라미터 설명 : pk 는 expense의 식별 아이디를 입력합니다

[응답]

-  Body

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

- 응답에 대한 설명

  - 성공 응답시 상태코드 : 200

  - 응답 Body 설명 : 복구된 지출내역(expense) 의 결과가 반환됩니다.

    

### 나의 지출내역 조회

[요청]

- URL: GET /expense/



[응답]

- Body

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "pk": 6,
      "amount": 100,
      "memo": "test_memo"
    }
  ]
}
```

- 응답에 대한 설명

  - 성공 응답시 상태코드 : 200

  - 응답 Body 설명 : 지출내역(expense) 의 결과가 반환됩니다.

    

### 나의 지출내역 상세조회

[요청]

- URL: GET expense/:pk/
  - Path 파라미터 설명 : pk 는 expense의 식별 아이디를 입력합니다

[응답]

- Body

```json
{
  "pk": 7,
  "amount": 2,
  "memo": "test2",
  "email": "email@email.com",
  "spent_at": "2021-11-25T03:11:27.185208Z",
  "updated_at": "2021-11-25T03:59:13.489565Z"
}

```

- 응답에 대한 설명
  - 성공 응답시 상태코드 : 200
  - 응답 Body 설명 : 지출내역(expense)상세 조회된 결과가 반환됩니다.
