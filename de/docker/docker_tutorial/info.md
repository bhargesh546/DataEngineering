### Cloning the getting-started-app repository from github using the following command:
`git clone https://github.com/docker/getting-started-app.git`

### Create the Dockerfile 

### Build the image
`docker build -t getting-started .`

### Container run
`docker run -d -p 127.0.0.1:3000:3000 getting-started`

###  list all containers
`docker ps`


# To Persist the DB

### Create a volume
`docker volume create todo-tb`

### specify the volume mount to the container
`docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started`

### info of volume
`docker volume inspect todo-db`

# Multi container apps

### Create a network
`docker network create todo-app`



>docker run -d \
    --network todo-app --network-alias mysql \
    -v todo-mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=todos \
    mysql:8.0


### To confirm you have the database up and running

`docker exec -it <mysql-container-id> mysql -u root -p`

docker run -dp 127.0.0.1:3000:3000 \
  -w /app -v ".:/app" \
  --network todo-app \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=secret \
  -e MYSQL_DB=todos \
  node:24-alpine \
  sh -c "npm install && npm run dev"


