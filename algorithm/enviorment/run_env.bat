@rem docker run
docker-compose up -d
echo Hello World
@for /f "usebackq delims=" %%A in (`docker ps -q`) do set HOGE=%%A
echo %HOGE%
docker exec -it %HOGE% /bin/bash