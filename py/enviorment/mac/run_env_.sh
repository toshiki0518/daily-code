#!/bin/bash

# Dockerコンテナ停止
docker-compose down

# Dockerコンテナのビルドと起動
docker-compose up -d --build

echo "start python"

# DockerコンテナのIDを取得
HOGE=$(docker ps -q)

echo "container id $HOGE"

# Dockerコンテナにbashで接続
docker exec -it $HOGE /bin/bash
