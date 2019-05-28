from datetime import datetime
import socket
import time

def process_event_message(message):
    timestamp = datetime.now()
    return timestamp.strftime('%b %d %H:%M:%S') + " GigamonInsightApp " + message

def syslog(hostname, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, 10000))
    message = process_event_message(content) + '\n'
    s.send(message.encode())
    print message
    s.shutdown(socket.SHUT_WR)
    s.close()

def send_event(content):
    syslog('127.0.0.1', content)

if __name__ == '__main__':
    send_event("Test Event")
