import enota1
import enota2
import enota3
import enota4
import enota5
import enota6
import extra
import numbers
import time
import verbs

while 1:

    print("a: enota 1")
    print("b: enota 2")
    # print("c: enota 3")
    # print("d: enota 4")
    print("e: enota 5")
    print("f: enota 6")
    print("g: extra")
    print("h: numbers")
    print("i: time")
    print("l: verbs")
    # print("z: tutti i test")
    print("q: esci")

    cmd = input("scegli il test:")

    if cmd == 'q':
        print("bye!")
        exit(0)
    elif cmd == 'a':
        enota1.run_me()
    elif cmd == 'b':
        enota2.run_me()
    elif cmd == 'c':
        enota3.run_me()
    elif cmd == 'd':
        enota4.run_me()
    elif cmd == 'e':
        enota5.run_me()
    elif cmd == 'f':
        enota6.run_me()
    elif cmd == 'g':
        extra.run_me()
    elif cmd == 'h':
        numbers.run_me()
    elif cmd == 'i':
        time.run_me()
    elif cmd == 'l':
        verbs.run_me()
    else:
        print("non ho capito la scelta!")