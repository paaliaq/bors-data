#!/usr/bin/env bash

printenv | cat - /etc/cron.d/cronpy > ~/crontab.tmp \
    && mv ~/crontab.tmp /etc/cron.d/cronpy

chmod 644 /etc/cron.d/cronpy

tail -f /var/log/cron.log &

cron -f