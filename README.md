# payhere 과제
<br>

## 필요

- Python 3.9.x

<br>

## 서버 구동 방법

### Python 종속성 설치
```
pip install -r requirements.txt
```

### MySQL 5.7 컨테이너 실행
```bash
docker-compose up -d
```

## DB 마이그레이션 
설계된 모델에 대한 스키마를 데이터베이스에 반영

```bash
python manage.py migrate
```

## Dockerfile 이미지 생성
```bash
docker build -t <이미지 이름>
```

## Docker Container 실행
```bash
docker run -itd <이미지 이름>
```

## 가계부 api


## 계정

----
### 회원가입
```bash
http://127.0.0.1:8000/accounts/register-user/
```

### 로그인
```bash
http://127.0.0.1:8080/accounts/login/
```

## 가계부

----
### 금액과 메모 작성
```bash
http://127.0.0.1:8080/Expense/expense_list
```

### 금액과 메모 수정
```bash
http://127.0.0.1:8080/Expense/expense_list
```

### 내역 삭제
```bash
http://127.0.0.1:8080/Expense/<해당번호>/set_delete/
```

### 삭제 내역 복구
```bash
http://127.0.0.1:8000/Expense/<해당번호>/restore/
```

### 가계부 리스트
```bash
http://127.0.0.1:8080/Expense/expense_list
```


