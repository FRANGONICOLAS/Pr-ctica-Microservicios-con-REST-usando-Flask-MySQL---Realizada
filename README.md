# To Run application

## Start and SSH into Vagrant VM 

```
vagrant up
vagrant ssh
```

## Run in /home/vagrant

```
consul agent -ui -dev -bind=192.168.60.3 -client=0.0.0.0 -data-dir=.
```

## Run the webApp

```
cd /home/vagrant/frontend
python3 run.py
```

## Run the Users Microservice

```
cd /home/vagrant/microUsers
python3 run.py
```

## Run the Products Microservice

```
cd /home/vagrant/microProducts
python3 run.py
```

## Para ver las funcionalidades ingrese en su buscador 192.168.60.3:8500 aqui se puede visualizar el descubridor de servicios y el estado de cada servicio. Y para las otras funcionalidades 192.168.60.3:5001.
