Name:           freespace
Version:        0.1
Release:        1%{?dist}
Summary:        Free space checker & logger

Group:          Monitoring
License:        MIT
Source0:        freespace-%{version}.tar.gz
Requires:       /bin/bash
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
Utilites for monitoring and logging free space on mounted disks.

%description -l uk
Утиліта для моніторінгу та логування вільного місця на примонтованих дисках.

%description -l ru
Утилита для мониторинга и логирования свободного места на примонтированных дисках.

%prep
%setup -q

%install
mkdir -p  %{buildroot}/usr/local/freespace

cp freespace.service %{buildroot}/usr/local/freespace
cp freespace.sh %{buildroot}/usr/local/freespace
#/etc/logrotate.d/freespace
cp freespace %{buildroot}/usr/local/freespace

%files

%defattr(-,root,root)
/usr/local/freespace/freespace.service
/usr/local/freespace/freespace.sh
/usr/local/freespace/freespace
%doc

%changelog
* Tue Feb 23 2021 Kyrylo Lohvynenko <Kyrylo.Lohvynenko@gmail.com>
 - So far, the first version...

%post -p /bin/bash
if [ $1 -eq 0 ]; then
  ### Clean install package
  ln -s /usr/local/freespace/freespace.service /lib/systemd/system/freespace.service 
  ln -s /usr/local/freespace/freespace /etc/logrotate.d/freespace

  for i in `cat /etc/rsyslog.conf && cat /etc/rsyslog.d/*.conf | grep "^local" | cut -c6 `; do
    arr[${#arr[*]}]=$i
  done
  for((i=2,br=0; i < 7 ; i++));do
    for n in ${arr[*]};do
      if [ $i =  $n ]; then
        br=1 #boolean
        break
      fi
    done
    if [ $br -eq 1 ];then
      br=0
    else
      break
    fi
  done
  if [ $i -eq 7 ];then
    i=1
  fi 

  echo -e "local$i.*\t\t\t\t\t\t/var/log/freespace" >/etc/rsyslog.d/freespace.conf
  echo -e "SHELL=/bin/bash\nMAILTO=root\n*/2\t*\t*\t*\t*\troot\tsystemctl start freespace.service\n" >/etc/cron.d/freespace
  %systemd_post rsyslog.service
fi

exit 0

%postun -p /bin/bash
if [ $1 -eq 0 ]; then
  ### Will be removed packege
  sed -i "\/var\/log\/freespace/d" /etc/rsyslog.conf
  unlink /lib/systemd/system/freespace.service
  rm /etc/rsyslog.d/freespace.conf 2>/dev/null
  rm /etc/cron.d/freespace 2>/dev/null
  unlink etc/logrotate.d/freespace
  %systemd_postun_with_restart rsyslog.service
fi
exit 0
