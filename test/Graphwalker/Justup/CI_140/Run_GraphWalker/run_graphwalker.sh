#!/bin/bash


BROWSER=`echo "$1" | awk -F"&" '{print $1}'`
PLATFORM=`echo "$1" | awk -F"&" '{print $2}'`
VERSION=`echo "$1" | awk -F"&" '{print $3}'`
SELENIUM_HUB="$2"
SELENIUM_FILE=`echo $SELENIUM_HUB | awk -F"/" '{print $NF}'`
SELENIUM_PORT="$3"
GRAPHWALKER="$4"
GRAPHWALKER_JAR_FILE=`echo $GRAPHWALKER | awk -F"/" '{print $NF}'`
GRAPHWALKER_COVERAGE="$5"
GRAPHML_FILE="$6"
MODEL_FILE="$7"

SLEEP_TIME=5

check_process() {
	kill $(ps aux | grep $GRAPHWALKER_JAR_FILE | grep -v grep | grep -v $0 | awk '{print $2}')
	kill $(ps aux | grep $SELENIUM_FILE | grep -v grep | grep -v $0 | awk '{print $2}')
	return $?
}

start_service() {
	java -jar "$SELENIUM_HUB" -role hub -port "$SELENIUM_PORT" -nodeTimeout 600000 -timeout 600000 &
	java -jar "$GRAPHWALKER" online --json --service RESTFUL -m "$GRAPHML_FILE" "$GRAPHWALKER_COVERAGE" &
	sleep $SLEEP_TIME
	return $?
}


run_model() {
	python "$MODEL_FILE" "$BROWSER" "$PLATFORM" "$VERSION"
}

check_process

start_service
retval=$?
if [ "$retval" -ne 0 ]
then
	echo "start service failed: $retval"
	exit
fi

run_model
retval=$?
if [ "$retval" -ne 0 ]
then
	echo "run model failed: $retval"
	exit
fi
