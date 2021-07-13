#!/bin/bash
if [ "$LOGFILE" == "" ]; then
    echo "Environment variable LOGFILE not set! Logfile will be called logfile by default."
    $LOGFILE = "logfile"
fi

# Dirty.
if [ ! -f "$LOGFILE" ]; then
    touch $LOGFILE
fi

# Check if task is running
runningtask=""
lastline=$(tail -n 1 $LOGFILE)
if [[ $lastline == *"LABEL"* ]]; then
    runningtask=$(echo $lastline| cut -d ' ' -f2-)
fi

if [ $# -gt 0 ]; then
    if [ "$1" == "start" ]; then
        if [ "$runningtask" != "" ]; then
            echo "There is already a running task!"
            exit
        elif [ $# -lt 2 ]; then
            echo "No label provided!"
            exit
        else
            shift;
            label=$1
            shift;
            
            for var in "$@"
            do
                label="${label} $1"
                shift;
            done
            echo "Started task: $label"
            echo "" >> $LOGFILE
            echo "START $(date)" >> $LOGFILE
            echo "LABEL $label" >> $LOGFILE
        fi
    elif [ "$1" == "stop" ]; then
        if [ "$runningtask" == "" ]; then
            echo "There is no running task to stop!"
            exit
        fi
        echo "END $(date)" >> $LOGFILE
    elif [ "$1" == "status" ]; then
        if [ "$runningtask" != "" ]; then
            echo "Currently running task: $runningtask"
        else
            echo "Currently not running any task"
        fi
    elif [ "$1" == "log" ]; then
        # Read all lines
        startdate=""
        enddate=""
        taskname=""
        while read line; do
            if [[ $line == *"LABEL"* ]]; then
                taskname=$(echo $line| cut -d ' ' -f2-)
            fi

            if [[ $line == *"START"* ]]; then
                startdate=$(echo $line| cut -d ' ' -f5-)
                startdate=$(echo $startdate| cut -d " " -f1)
            fi

            if [[ $line == *"END"* ]]; then
                enddate=$(echo $line| cut -d ' ' -f5-)
                enddate=$(echo $enddate| cut -d " " -f1)
                startdate=$(date -u -d "$startdate" +"%s")
                enddate=$(date -u -d "$enddate" +"%s")
                result=$(date -u -d "0 $enddate sec - $startdate sec" +"%H:%M:%S")
                echo "${taskname}: $result"
            fi
        done <$LOGFILE
    fi
else
    echo "Usage: track start [label]|stop|status|log"
fi
