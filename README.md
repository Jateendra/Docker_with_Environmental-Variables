# Environmental Variable Setting in Docker

Environmental variables can be set in 2 ways in Docker .

* e

OR

* --env-file = .env

## Procedure 1 : --env-file = .env

1. Write the code for :
    * app.py
    * Dockerfile
    * .env

2. In Gitbash terminal of VSCode :

```bash
docker build . -t env1
docker run --env-file=.env env1
```

It will show the output as :

```bash
Running with user: aiuser
Running with password: aivision
```

3. You can try changing the details in .env file as :

```bash
MY_USER=aiuser123
MY_PASS=aivision123
```

- Run the docker again :

```bash
docker run --env-file=.env env1
```

It will show the new output as :

```bash
Running with user: aiuser123
Running with password: aivision123
```

## Procedure 2 : -e

1. In Gitbash terminal of VSCode :

```bash
docker run -e MY_USER=a89 -e MY_PASS=a90 env1
```

- It will show the output as :

```bash
Running with user: a89
Running with password: a90
```

## Conclusion :

* .env is the best way to set Environmental variable .
* This is because when the no. of environmental variables are increasing this is good to use .
