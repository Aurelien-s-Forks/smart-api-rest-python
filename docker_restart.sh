#!/bin/bash

docker stack rm bai-systems-api && docker stack deploy -c docker-compose.yml bai-systems-api