# create manifest that kills process named killmenow

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
