# install postgres

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
        systemctl restart postgresql-9.6.service
        
- 设置数据库
        
        su - postgres
        psql
        \password (zyd@...)
        alter user xx with password 'xxx';
        
        
# mac operation

- create a user

        createuser username -P
        
- create a database

        createdb -O username dabtabase_name
        
- connect a database
        
        psql -U username -d dbname
        
- drop a database

        dropdb dbname
        
# common comands

- \l  list database
- \d  show tables
- \d table_name  列出指定表的结构
- \c dbname 切换数据库
- \du 查看角色


# install psycopg2

        pip install psycopg2
        
        pip freeze > requirement.txt
        
# install gunicorn 

        pip install gunicorn
        
        
        gunicorn miracle_server.wsgi --bind 0.0.0.0:80
        
# 阿里云

## login 

        ssh root@47.93.237.94 (password hfy@...)


## application user

        sudo groupadd --system webapps
        sudo useradd --system --gid webapps --shell /bin/bash --home /webapps/miracle-serve miracle
        sudo passwd miracle (zyd@...)
- 查看组

        cat /etc/group
        

        

## python virtual enviroment

- pyenv

        pyenv install 3.6.1
        
- pyenv virtualenv

        git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
        echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
        source ~/.bashrc
        
- virtualenv

        pyenv virtualenv 3.6.1 miracle
        
        
# nginx

        cp dev/nginx.conf /etc/nginx/nginx.conf
        nginx -s reload

## mac

- install 
        
        brew install nginx
        docroot: /usr/local/var/www
        brew services start nginx(http://localhost:8080/)
        install dir: /usr/local/Cellar/nginx/1.12.0
        config:/usr/local/etc/nginx/nginx.conf
        user=root(第一步所有都在root用户下运行)
        
# supervisor

        supervisord -c dev/supervisord.conf
    
        

        
 
        
    
        
        
