# Python Redis Caching Exercise

## Versions

- docker-compose version `1.23.1, build b02f1306`
- docker version `19.03.1, build 4484c46d9d`

## Quick start

Clone the repo:

```sh
git clone https://github.com/vilaverde/redis-caching-api.git
cd redis-caching-api
```

Build the container

```sh
docker-compose build
```

Run the project
```
docker-compose up
```

## Information

- `GET /starwars/movies?id=<id>` endpoint fetches data from [SWAPI](https://swapi.dev/) to return movies data (id parameter is optional)


## Testing
To run unittest
```
docker-compose run redis-caching-api python3 -m unittest tests/*_test.py tests/**/*_test.py
```

## Removing docker image

*** DO NOT RUN THE FOLLOWING IF YOU HAVE MORE APPS THAT WOULD MATCH redis-caching-api GREP ***

On project folder run the following commands
```
docker-compose down
docker rmi $(docker image ls | grep redis-caching-api | awk '{print $1}') -f
```

## Author

__Name:__ Lucas Vilaverde Machado

__E-mail:__ lucasvmachado@gmail.com

__Github:__ https://github.com/vilaverde
