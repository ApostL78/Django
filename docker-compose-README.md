# Run with `Docker Compose`
To run this app with docker compose clone repository:
```shell
git clone https://github.com/ApostL78/DjangoBlog.git
```
Then go to DjangoBlog to create and activate venv:
```shell
cd DjangoBlog
python -m venv venv
./venv/bin/activate
```
Then run following command:
```shell
docker compose up --build
```
After that, our services is working, but we need to migrate our project:
```shell
docker exec -it django_blog /bin/bash
python DjangoProject/manage.py migrate
```
Now you can navigate to `http://localhost:8000` in your web browser and see, that its working, but we dont have a content.
Run following commands to create 1 task:
```shell
python DjangoProject/manage.py shell
```
```pycon
a = Task.objects.create(title='Task1')
a.save()
exit()
```

# Expected Result && Clean Up
After all steps, you should see same image:
[result](https://github.com/ApostL78/DjangoBlog/blob/master/result.png?raw=true)
Now you can run following command to stop and delete containers:
```shell
docker compose down
```
To restart an app you can run this command and data that created in previous steps will be here:
```shell
docker compose up
```