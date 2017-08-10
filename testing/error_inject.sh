#!/bin/bash
#
# Example error_injection.sh vpc-prod-vertex03
#
Inject_string="localhost:9192"
curl -G --data-urlencode "hostname=$1" --data-urlencode "log=MWBidRequestHandler::Unable to send BID message" http://$Inject_string/myapp/Error_track/
curl -G --data-urlencode "hostname=$1" --data-urlencode "log=WinNotify Unable to send message" http://$Inject_string/myapp/Error_track/
curl -G --data-urlencode "hostname=$1" --data-urlencode "log=Error deploying RabbitMQ" http://$Inject_string/myapp/Error_track/

 

