#!/usr/bin/env python

try:
    from urllib import request as urllib_request
except ImportError:
    import urllib2 as urllib_request
import json
import sys

class slbAPI(object):

    def __init__(self, endpoint):
        self._endpoint = endpoint

    def ExecCmnd(self,cmnd_data):
        try:
            request = urllib_request.Request(self._endpoint,cmnd_data)
            reader = urllib_request.urlopen(request)
            api_response = reader.read()
            resp = json.loads(api_response)
            return resp
        except urllib_request.HTTPError:
            #TODO: more meaningfull comment; more errors handling
            return {"result":"error during api urllib_request"}
        except:
            return {"result":"generic error"}

        


def main():
        '''
        examples of supported commands(lots of copy paste right now while i'm writing new features
        and testing the output; gona remove it later)
        '''
        url = sys.argv[1]
        slb = slbAPI(url)
        data = json.dumps({"Command":"GetInfo","service":"192.168.1.1"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"AddService","VIP":"192.168.1.2","Port":"80","Proto":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"AddReal","VIP":"192.168.1.2","Port":"80","Proto":"tcp",
                           "RIP":"87.250.242.147","RealPort":"22","Check":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"GetInfo","service":"192.168.1.1"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"RemoveReal","VIP":"192.168.1.1","Port":"22","Proto":"tcp",
                           "RIP":"192.168.132.1","RealPort":"22","Check":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        '''
        data = json.dumps({"Command":"AddReal","VIP":"192.168.1.1","Port":"22","Proto":"tcp",
                           "RIP":"192.168.132.1","RealPort":"22","Check":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        '''

        '''
        data = json.dumps({"Command":"AddService","VIP":"192.168.1.2","Port":"80","Proto":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"AddService","VIP":"[fc12:1::2]","Port":"80","Proto":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"AddService","VIP":"[fc12:1::2]","Port":"80","Proto":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"AddService","VIP":"[sdasdadasd]","Port":"80","Proto":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"GetInfo","service":"192.168.1.1"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"RemoveService","VIP":"[fc12:1::2]","Port":"80","Proto":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"RemoveService","VIP":"192.168.1.2","Port":"80","Proto":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"GetInfo"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"RemoveService","VIP":"[fc12:1::1]","Port":"22","Proto":"tcp"})
        resp = slb.ExecCmnd(data)
        print(resp)
        data = json.dumps({"Command":"GetInfo"})
        resp = slb.ExecCmnd(data)
        print(resp)
        '''








if __name__ == "__main__":
    main()

    