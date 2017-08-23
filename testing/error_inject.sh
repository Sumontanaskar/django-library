#!/bin/bash
#
# Example error_injection.sh vpc-prod-vertex03
#
Inject_string="52.86.0.96:9192"
#Inject_string="localhost:9192"
function curl_post() {
	log_1='WinNotify Unable to send message'
	log_2='AMQP error for winNotify'
	log_3='configure exchanges are : 0 check config properties exchanges.path'
	log_4='AMQP error for bidId'
	log_5='Error sending msg to kafka'
	log_6='Error status send by mq event bus send'
	log_7='MWBidRequestHandler::Unable to send BID message'
	log_8='Error getting value from redis'
	log_9='Error deploying RabbitMQ'
	log_10='AMQP Deployment Error'

	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_1" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_2" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_3" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_4" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_5" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_6" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_7" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_8" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_9" http://$Inject_string/myapp/Error_track/
	curl -G --data-urlencode "hostname=$1" --data-urlencode "log=$log_10" http://$Inject_string/myapp/Error_track/

}

for var in "$@"
do
    echo "$var"
    curl_post "$var"
done 
