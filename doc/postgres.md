# install

- Postgresql Repository

        yum install https://yum.postgresql.org/9.6/redhat/rhel-7-x86_64/pgdg-redhat96-9.6-3.noarch.rpm
      
- install 

        yum install postgresql96-server postgresql96-contrib
        
- init database 

        /usr/pgsql-9.6/bin/postgresql96-setup initdb
        
- auto start service
        
        systemctl enable postgresql-9.6.service
        
- start service
    
        systemctl start postgresql-9.6.service
