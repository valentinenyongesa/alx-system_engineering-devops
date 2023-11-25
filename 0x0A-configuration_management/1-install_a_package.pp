#!/usr/bin/pup
# Using puppet install Flask

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
