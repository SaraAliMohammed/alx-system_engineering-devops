# Update package repositories
exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure => installed,
  require => Exec['update'],
}

# Add custom HTTP header to Nginx configuration
file_line { 'header_served_by':
  path     => '/etc/nginx/sites-enabled/default',
  line     => 'server {',
  match    => '^server {',
  after    => true,
  multiple => false,
  notify   => Exec['nginx_restart'],
}

# Restart Nginx service after configuration changes
exec {'nginx_restart':
  command => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
