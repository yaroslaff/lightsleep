# lightsleep
Lightsleep is sleep() you can interrupt with redis or websocket event

This is nice feature if you want to do some actions periodically AND immediately on some event.

## lightsleep 
`ltsleep.py` is very short simple CLI utility (better then `/usr/bin/sleep`) which is also demo how to use `sleep`.

Useless example where lsleep is identical to `/usr/bin/sleep` (sleep 60 seconds):
~~~
lsleep.py 60
~~~

### interrupt sleep with redis PUBLISH command

`lsleep.py 60 --hook redis` (defaults: local redis server, channel `sleep`)

Interrupt this sleep from redis-cli:
~~~
127.0.0.1:6379> PUBLISH sleep anything
(integer) 1
~~~

To override defaults parameters: 
~~~
lsleep.py 60 --hook redis url=redis://localhost:6379/0 msg=stop ch=sleep
~~~
(seting `msg` to any value will requre to PUBLISH exact this value. If `msg` is not set, any message will interrupt sleep)

### Interrupt sleep with websocket 
~~~
lsleep.py 300 --hook ws url=http://localhost:8899/ room=myapps::u1 secret=myapps-pass
~~~

You may use [ws-emit](https://github.com/yaroslaff/ws-emit) websocket application as server.

optional `secret` if room requires secret to join (when room name containts '::'). This should match ws-emit secret in redis, set with `SET ws-emit::secret::myapps myapps-pass`

If `event` and `data` specified, sleep will be interrupted only if websocket event name and data matches it.

## Using sleep in your package
See lsleep.py code, it's very small. Example:

~~~python
from lightsleep import Sleep

s = Sleep(hook=['redis','msg=stop', 'ch=sleep'])
s.sleep(60)
~~~
