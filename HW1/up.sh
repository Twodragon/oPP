#!/usr/bin/env bash

docker-compose up -d db rabbit
sleep 10
docker-compose up consumer producer
