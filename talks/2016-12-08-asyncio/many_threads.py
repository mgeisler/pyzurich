import threading
import time


def sleeper(stop):
    ident = threading.get_ident()
    with stop:
        #print('Thread %s waiting...' % ident)
        stop.wait()
    print('Thread %s stopping' % ident)


def spawn_threads(stop):
    while True:
        t = threading.Thread(target=sleeper, args=(stop,))
        t.start()

        print("Started %d threads" % threading.active_count())
        time.sleep(0.001)

if __name__ == '__main__':
    threading.stack_size(1 * 1024 * 1024)

    stop = threading.Condition()

    try:
        spawn_threads(stop)
    except KeyboardInterrupt:
        with stop:
            stop.notify_all()
