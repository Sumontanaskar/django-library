#!/bin/bash
#LIST="newsumonts@gmail.com sumonta@mobilewalla.com"
LIST="sumonta@mobilewalla.com"
hostname=`hostname`
server_url="http://192.168.162.128:9192/myapp/Error_track/"
echo $hostname $server_url $LIST
tail -fn0  /var/log/auth.log| \
while read line ; do
        echo "$line" | egrep 'WinNotify Unable to send message|AMQP error for winNotify|configure exchanges are : 0 check config properties
 exchanges.path|AMQP error for bidId|Error sending msg to kafka|Error status send by mq event bus send|MWBidRequestHandler::Unable to send 
BID message|Error getting value from redis|Error deploying RabbitMQ|AMQP Deployment Error'>log_check.txt
        if [ $? = 0 ]
        then
#               echo Prepare to send email
#               mail -s "[Prod-Vertex-21] [ERROR] [US-EAST] [Error/Exceptions in Log File] [/home/wordster/deploy/logs/error.log]" $LIST < 
log_check.txt
#               echo Email sent
                log=$(cat "log_check.txt")
                echo ------ $log
                curl -I -G --data-urlencode "hostname=$hostname" --data-urlencode "log=$log" $server_url
#               echo log sent success

        fi
done
