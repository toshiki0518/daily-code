@rem docker run
docker-compose down
docker-compose up -d --build
echo start python
@for /f "usebackq delims=" %%A in (`docker ps -q`) do set HOGE=%%A
echo container id %HOGE%
docker exec -it %HOGE% /bin/bash