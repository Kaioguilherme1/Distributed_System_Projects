#!/bin/bash

sleep 5

rabbitmqctl add_user Consumer 1234
rabbitmqctl add_user Producer 1234
rabbitmqctl set_permissions -p / Consumer ".*" ".*" ".*" #seta permissões para o usuário Consumer
rabbitmqctl set_permissions -p / Producer ".*" ".*" ".*" #seta permissões para o usuário Producer
