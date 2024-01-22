@rem docker run
docker-compose down --rmi all --volumes --remove-orphans
docker stop $(docker ps -q) && docker rm $(docker ps -aq)
docker-compose -f ../docker-compose.yml up -d --build
echo start python
@for /f "usebackq delims=" %%A in (`docker ps -q`) do set HOGE=%%A
echo container id %HOGE%
docker exec -it %HOGE% /bin/bash
