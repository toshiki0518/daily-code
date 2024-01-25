#!/bin/bash

# Dockerコンテナ停止
docker-compose down --rmi all --volumes --remove-orphans
docker stop $(docker ps -q) && docker rm $(docker ps -aq)

# Dockerコンテナのビルドと起動
docker-compose -f ../docker-compose.yml up -d --build

echo "start linux and python"

# DockerコンテナのIDを取得
HOGE=$(docker ps -q)

echo "container id $HOGE"

# Dockerコンテナにbashで接続
docker exec -it $HOGE /bin/bash
