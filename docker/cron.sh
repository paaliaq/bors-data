#!/bin/sh

echo "PAALIAQ_RUN_ONCE is set to: ${PAALIAQ_RUN_ONCE}."

if [ "$PAALIAQ_RUN_ONCE" = true ] ; then

    echo "Only running once."

    echo "$@"
    echo "Command line arguments should have been printed."

    python main.py $@

    if [ $? != 0 ]; then
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