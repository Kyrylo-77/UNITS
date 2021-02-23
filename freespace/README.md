The checker & logger for free space on mounted disks

Unit:
/lib/systemd/system/freespace.service
Script:
/usr/local/freespace/freespace.sh


vim /etc/rsyslog.conf 
local2.!=info         /var/log/messages

/etc/cron.d/freespace
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

/etc/logrotate.d/freespace
/var/log/freespace {
  daily
  missingok
  rotate 2
  compress
  delaycompress
  notifyempty
  create 644 root root
  sharedscripts
  postrotate
  [ -f /var/run/freespace.pid ] && kill -HUP `cat /var/run/freespace.pid`
  endscript
}

	
           install upgrade uninstall
%pretrans   $1 == 0 $1 == 0 (N/A)
%pre        $1 == 1 $1 == 2 (N/A)
%post       $1 == 1 $1 == 2 (N/A)
%preun      (N/A)   $1 == 1 $1 == 0
%postun     (N/A)   $1 == 1 $1 == 0
%posttrans  $1 == 0 $1 == 0 (N/A)

%postun
if [ $1 -eq 0 ]; then
    ### Выполнение действий, специфичных для удаления пакета
fi
if [ $1 -eq 1 ]; then
    ### Выполнение действий, специфичных для обновления пакета
fi

