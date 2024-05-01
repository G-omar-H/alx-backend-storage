# 0x02. Redis Basic

![Redis Logo](https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/Redis_Logo.svg/1200px-Redis_Logo.svg.png)

## Description

This project teaches the fundamentals of working with Redis in a Python environment. Learn how to interact with Redis to store and retrieve data, use Redis as a cache, track function calls, and more.

## Installation

1. Install Redis on Ubuntu 18.04 LTS:
   ```bash
   sudo apt-get -y install redis-server
   pip3 install redis
   sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
   ```

2. Clone the repository:

``` bash
git clone https://github.com/G-omar-H/0x02-redis_basic.git
```

4. Navigate to the project directory:

```bash

    cd 0x02-redis_basic
```

## Usage

Run the provided examples or test your implementations using the main files or create your own scripts.
Tasks

    Writing strings to Redis: Store data in Redis using Python.

    Reading from Redis and recovering original type: Retrieve data from Redis and convert it back to its original type.

    Incrementing values: Implement a system to count how many times methods of the Cache class are called.

    Storing lists: Store the history of inputs and outputs for a particular function in Redis.

    Retrieving lists: Display the history of calls of a particular function.

    Implementing an expiring web cache and tracker: Create a web cache with an expiration time and track URL access counts.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
