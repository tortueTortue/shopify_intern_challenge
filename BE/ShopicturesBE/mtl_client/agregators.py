import json
import queue

def parse_topic_msg(topic_msg):
    if str(topic_msg)[-1:] == "'":
        return json.loads("{"+str(topic_msg)[:-3].split("{")[1])
    else:
        return json.loads("{"+str(topic_msg).split("{")[1])


def minn(msg_list):
    msg_list.sort()
    return ("min", msg_list[0])

def maxx(msg_list):
    msg_list.sort()
    return ("max", msg_list[len(msg_list)-1])

def avg(msg_list):
    return ("avg", sum(msg_list) / len(msg_list))

def total(msg_list):
    return ("total", len(msg_list))

def median(msg_list):
    total = len(msg_list)
    msg_list.sort()
    if total % 2 == 0 :
        return ("median", (msg_list[int(total/2)] + msg_list[int(total/2)-1] )/2)
    else:
        return ("median", msg_list[int(total//2)])

agregator_map = {"min": minn, "max": maxx, "avg": avg, "median": median, "total": total} 