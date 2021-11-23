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

