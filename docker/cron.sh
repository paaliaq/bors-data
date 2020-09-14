#!/bin/sh

echo "PAALIAQ_RUN_ONCE is set to: ${PAALIAQ_RUN_ONCE}."

if [ "$PAALIAQ_RUN_ONCE" = true ] ; then

    echo "Only running once."

    echo "$@"
    echo "Command line arguments should have been printed."

    # TODO: Add call to run your application only ONCE during testing
    # $@ holds all command line arguments added to docker run container...
    # So there must be a way to pass a different connection string to your
    # application for testing. An environment variable would also work
    # the test is okay, if your application returns 0, therefor this parts
    # runs your application ocnce and if there was no error, it returns 0.

    #./bors-data/main.py $@

    if [[ $? != 0 ]]; then
    echo "Error occured while running application only once."
        exit 1
    fi

    exit 0
fi

printenv | cat - /etc/cron.d/cronpy > ~/crontab.tmp \
    && mv ~/crontab.tmp /etc/cron.d/cronpy

chmod 644 /etc/cron.d/cronpy

tail -f /var/log/cron.log &

cron -f