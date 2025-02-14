## About The Pwny Cup 2k24

The event is a 1v1 solo CTF competition organized by the Shellmates club last November .

## My Contribution

This repository contains four of my challenges, along with their solution scripts:

- fmt0
- fmt1
- heap0x0
- way2rome

## Playing the Challenges Locally

To play the challenges locally, follow these steps:

- Clone the repository:

```bash 
git clone https://github.com/Salsabilachattah/The-Pwny-Cup-2k24.git
```

- Navigate to the challenge folder:

```bash
cd ./path/to/challenge
```

- Build and run the challenge using Docker:

```bash
docker build -t challenge .
docker run --rm -it -p 3000:3000 challenge
```

- Connect to the challenge locally:

```bash
nc localhost 3000
```
