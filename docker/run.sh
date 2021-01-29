#!/bin/bash

sleeptime=86400

function finish() {
    echo "\nBye."
    exit
}

trap finish SIGINT

echo "PAALIAQ_RUN_ONCE is set to: ${PAALIAQ_RUN_ONCE}."

if [ "$PAALIAQ_RUN_ONCE" = true ] ; then

    echo "Only running once. Printing command line arguments:"
    echo "$@"
    echo "Running script now."

    poetry run python src/main.py $@

    if [ $? != 0 ]; then
    echo "Error occured while running application only once."
        exit 1
    fi

    exit 0
fi

while :; do

    echo "Running in loop. Printing command line arguments:"
    echo "$@"


    echo "Running script now."

    poetry run python src/main.py $@

    echo "Sleeping for ${sleeptime}s"

    sleep ${sleeptime} &
    wait
    
    if [ $? != 0 ]; then
    echo "Error occured, ending loop."
        exit 1
    fi

done
