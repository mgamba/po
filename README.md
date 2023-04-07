# Po

## installation
```
pip install -r requirements.txt
```

## running
```
docker run -it --rm -v "$(pwd)":/app -w /app -p 127.0.0.1:8000:8000/tcp amancevice/pandas:2.0.0-slim /bin/sh
```

```
gunicorn app:api -c /app/config/gunicorn.py
```

## python
save current setup to requirements.txt
```
pip freeze >> requirements.txt
```
