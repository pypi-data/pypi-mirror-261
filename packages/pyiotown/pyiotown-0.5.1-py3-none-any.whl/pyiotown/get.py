import requests
import datetime

def node(url, token, nid=None, group_id=None, verify=True, timeout=60):
    header = {'Accept':'application/json','token':token}

    # only for administrators
    if group_id is not None:
        header['grpid'] = group_id

    uri = url + "/api/v1.0/" + ("nodes" if nid is None else f"node/{nid}")
    
    try:
        r = requests.get(uri, headers=header, verify=verify, timeout=timeout)
    except Exception as e:
        print(e)
        return None
    
    if r.status_code == 200:
        return r.json()
    else:
        print(r)
        return None
    
def storage(url, token, nid=None, date_from=None, date_to=None, count=None, sort=None, lastKey="", group_id=None, verify=True, timeout=60):
    '''
    url : IoT.own Server Address
    token : IoT.own API Token
    nid : Node ID
    '''
                    
    header = {'Accept':'application/json','token':token}

    # only for administrators
    if group_id is not None:
        header['grpid'] = group_id

    uri_prefix = url + "/api/v1.0/storage"

    params = []
    
    if nid != None:
        params.append(f"nid={nid}")
        
    if date_from != None:
        params.append(f"from={date_from}")

    if date_to != None:
        params.append(f"to={date_to}")

    if count != None:
        params.append(f"count={count}")

    if sort != None:
        params.append(f"sort={sort}")

    if len(params) > 0:
        uri_prefix += '?' + '&'.join(params)
        
    result = None
    
    while True:
        try:
            uri = uri_prefix if lastKey == "" else uri_prefix + "&lastKey=" + lastKey
            r = requests.get(uri, headers=header, verify=verify, timeout=timeout)
        except Exception as e:
            print(e)
            return None
    
        if r.status_code == 200:
            if result is None:
                result = r.json()
                if 'lastKey' in result.keys():
                    del result['lastKey']
            else:
                result['data'] += r.json()['data']

            if 'lastKey' in r.json().keys():
                lastKey = r.json()['lastKey']
            else:
                return result
        else:
            print(r)
            return None

def command(url, token, nid, group_id=None, verify=True, timeout=60):
    uri = f"{url}/api/v1.0/command/{nid}"
    header = {
        'Accept': 'application/json',
        'token': token
    }

    if group_id is not None:
        header['grpid'] = group_id

    try:
        r = requests.get(uri, headers=header, verify=verify, timeout=timeout)
        if r.status_code == 200:
            return r.json()
        else:
            print(r)
            return None
    except Exception as e:
        print(e)
        return None

def downloadImage(url, token, imageID, verify=True, timeout=60):
    ''' 
    url : IoT.own Server Address
    token : IoT.own API Token
    imageID : IoT.own imageID ( using annotation's 'id' not '_id' ) 
    '''
    uri = url + "/nn/dataset/img/" + imageID
    header = {'Accept':'application/json', 'token':token}
    try:
        r = requests.get(uri, headers=header, verify=verify, timeout=timeout)
        if r.status_code == 200:
            return r.content
        else:
            print(r)
            return None
    except Exception as e:
        print(e)
        return None

def downloadAnnotations(url, token, classname, verify=True, timeout=60):
    ''' 
    url : IoT.own Server Address
    token : IoT.own API Token
    classname : Image Class ex) car, person, airplain
    '''
    uri = url + "/api/v1.0/nn/images?labels=" + classname
    header = {'Accept':'application/json', 'token':token}
    try:
        r = requests.get(uri, headers=header, verify=verify, timeout=timeout)
        if r.status_code == 200:
            return r.json()
        else:
            print(r)
            return None
    except Exception as e:
        print(e)
        return None
