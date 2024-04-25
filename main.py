import random
import json
import threading
import msvcrt
try: 
    with open('cursing.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
except:
    with open('libs\\cursing.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
cursing:list[str] = data['content']
event = threading.Event()

def curse():
    unused = [x for x in cursing]
    while not event.is_set():
        try:
            try:
                element = random.choice(unused)
                print(element)
                unused.remove(element)
            except:
                unused = [x for x in cursing]
                print('-' * 50)
            event.wait(0.5)
        except:
            break

def stop():
    while True:
        if msvcrt.getch() == b'\r':
            event.set()
            break
        else:
            pass

def init():
    print('按下 Q 开始祖安。按 ESC 退出。祖安过程中按 ENTER 停止。')
    main = threading.Thread(target=curse)
    watcher = threading.Thread(target=stop)
    while True:
        key = msvcrt.getch()
        if key == b'q':
            watcher.start()
            main.start()
            watcher.join()
            main.join()
            break
        elif key == b'\x1b': 
            break
        else:
            pass


if __name__ == '__main__':
    init()
# if init():
#     watcher.start()
#     main.start()
#     watcher.join()
#     main.join()


    