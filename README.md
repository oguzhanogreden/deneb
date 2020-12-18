# deneb

A container that generates Altair graphs for you, a wrapper for altair_saver, the missing piece of the trio.

Once run, it will monitor files in a folder for Vega specifications and generate PNG images.

## Installation

There is no installation.
But you need [Docker](https://docs.docker.com/get-docker/).

```
git clone https://github.com/oguzhanogreden/deneb

cd deneb 
docker build . -t deneb
```

## Usage

In the directory where you'll save Vega specifications, simply:

```
docker run --volume="$PWD:/watch deneb /watch"
```
