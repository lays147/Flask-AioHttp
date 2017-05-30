## Flask x AioHttp
This project has the goal to test Async x Sync applications for web development.
I'm using [Flask](flask.pocoo.org/docs/0.12/) to test with Sync and [AioHttp](aiohttp.readthedocs.io) for Async.

### Part 1: Coding
##### Flask
The main code for Flask is the one below:
```
from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    time.sleep(2)
    return "Hello Lays"

if __name__ == "__main__":
    app.run()
```
That is a simple code to return a string for the GET request.
##### AioHttp
The main code for AioHttp is the one below:
```
from aiohttp import web
import asyncio

async def hello(request):
    await asyncio.sleep(2)
    return web.Response(text="Hello Lays")

app = web.Application()
app.router.add_get('/', hello)

if __name__ == "__main__":
    web.run_app(app)
```
Also the same idea of Flask, return a simple string on a GET request.

### Part 2: Benchmark
I used apache-utils [ab](http://httpd.apache.org/docs/current/programs/ab.html) command to run a benchmark of the HTTP requests.

##### Flask

Running 5 requests at the same time:
```
➜  ~ ab -c 5 -n 5 http://127.0.0.1:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
Benchmarking 127.0.0.1 (be patient).....done

Server Software:        Werkzeug/0.12.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        10 bytes

Concurrency Level:      5
Time taken for tests:   10.023 seconds
Complete requests:      5
Failed requests:        0
Total transferred:      825 bytes
HTML transferred:       50 bytes
Requests per second:    0.50 [#/sec] (mean)
Time per request:       10022.812 [ms] (mean)
Time per request:       2004.562 [ms] (mean, across all concurrent requests)
Transfer rate:          0.08 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:  2005 6014 3169.1   7016   10022
Waiting:     2004 6013 3169.1   7015   10022
Total:       2005 6014 3169.0   7016   10022

Percentage of the requests served within a certain time (ms)
  50%   6014
  66%   8018
  75%   8018
  80%  10022
  90%  10022
  95%  10022
  98%  10022
  99%  10022
 100%  10022 (longest request)
```

##### AioHttp

```
➜  ~ ab -c 5 -n 5 http://127.0.0.1:8080/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
Benchmarking 127.0.0.1 (be patient).....done

Server Software:        Python/3.5
Server Hostname:        127.0.0.1
Server Port:            8080

Document Path:          /
Document Length:        10 bytes

Concurrency Level:      5
Time taken for tests:   2.010 seconds
Complete requests:      5
Failed requests:        0
Total transferred:      805 bytes
HTML transferred:       50 bytes
Requests per second:    2.49 [#/sec] (mean)
Time per request:       2009.802 [ms] (mean)
Time per request:       401.960 [ms] (mean, across all concurrent requests)
Transfer rate:          0.39 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:  2009 2009   0.0   2009    2009
Waiting:     2006 2008   0.9   2008    2009
Total:       2009 2009   0.1   2010    2010
ERROR: The median and mean for the total time are more than twice the standard
       deviation apart. These results are NOT reliable.

Percentage of the requests served within a certain time (ms)
  50%   2009
  66%   2010
  75%   2010
  80%   2010
  90%   2010
  95%   2010
  98%   2010
  99%   2010
 100%   2010 (longest request)
```

### Part 3: Conclusion
