##docker images

docker pull grafana/grafana
docker pull mysql/mysql-server

##clone repository to your working directory

git clone /ArmenMadoyan/coolina

##change grafana-volume permissions

chmod 777 grafana-volume

##run docker compose and access Grafana via web

docker compose up -d

http://{your_ip}:3000

user- admin

pass- admin
