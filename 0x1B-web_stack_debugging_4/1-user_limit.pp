#Enable user holberton to login without any error

exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '/^holberton soft/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
