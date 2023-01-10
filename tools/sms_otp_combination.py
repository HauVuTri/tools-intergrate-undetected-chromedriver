import requests,json,time
import re
import random

config = {
    'otpsim.com':{'url':'http://otpsim.com/api/service/request?token=','token':True,'Mobi':'1','Vina':'2','Viettel':'3','VNMB':'4','ITelecom':'5'},
    'codesim.net':{'url':' http://api.codesim.net/api/CodeSim/GetDS_DichVu','token':False,'Viettel':'VIETTEL','Mobi':'Mobi','Vina':'Vina','VNMB':'VNMB','ITelecom':'ITelecom'},
    'nanosim.vn':{'url':'https://access.nanosim.vn/api/ig/services?api_token=','token':True,'Viettel':'VIETTEL','Mobi':'Mobi','Vina':'Vina','VNMB':'VNMB','ITelecom':'ITelecom'},
    'otpvn.com':{'url':'','token':None,'Viettel':'VIETTEL','Mobi':'Mobi','Vina':'Vina','VNMB':'VNMB','ITelecom':'ITelecom'},
    'chothuesimcode.com':{'url':'https://chothuesimcode.com/api?act=app&apik=','token':True,'Viettel':'Viettel','Mobi':'Mobi','Vina':'Vina','VNMB':'VNMB','ITelecom':'ITelecom'}
}

def getinfo(loai,dv,key):
    s =  requests.session()
    s.trust_env = False
    s.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-A805N Build/LYZ28N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36'})
    if config[loai]['token'] == True:
        token = key.strip()
    else:
        token = ''
    if config[loai]['token'] != None:
        out = s.get(config[loai]['url']+token)
    else:
        return dv
    inttext = json.loads(str(out.text))
    try:
        loai = inttext['data']
    except:
        loai = inttext['Result']
    for i in range(len(loai)):
        dvsms = str(loai[i]).find(dv)
        if  dvsms > 0 :
            infodv = loai[i]
            break
        else:
            infodv = None
    return infodv

def get_phone(key,loai,networks,dv,number):
    infodv = getinfo(loai,dv,key)
    if  infodv != None:
        pass
    else:
        return 'Lỗi Dịch Vụ',False
    try:
        service = str(infodv['id'])
    except:
        try:
            service = str(infodv['Id'])
        except:
            service = dv
    print(service)
    network = config[loai][networks]
    while True:
        time.sleep(1)
        try:
            s =  requests.session()
            s.trust_env = False
            s.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-A805N Build/LYZ28N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36'})

            if loai == 'otpsim.com':
                if number == '':
                        so = ''
                else:
                    so = f'&number={number}'
                for kt  in range(10):
                    time.sleep(1)
                    try:
                        url = f'http://otpsim.com/api/phones/request?token={key}&service={service}&network={network}{so}'
                        phones = s.get(url,timeout=20)
                        sever_g = json.loads(phones.text)
                        phone = sever_g['data']['phone_number']
                        re.findall('[0-9]+', phone)[0]
                        id_sever = sever_g['data']['session']
                        break
                    except:
                        pass
                return  phone,id_sever

            if loai == 'codesim.net':
                for kt  in range(10):
                    time.sleep(1)
                    try:
                        url = f'http://api.codesim.net/api/CodeSim/DangKy_GiaoDich?apikey={key}&dichvu_id={service}&so_sms_nhan=1&oai_nha_mang={network}'
                        phones = s.get(url,timeout=20)
                        sever_g = json.loads(phones.text)
                        phone = sever_g['data']['phoneNumber']
                        re.findall('[0-9]+', phone)[0]
                        id_sever = sever_g['data']['id_giaodich']
                        break
                    except:
                        pass
                return  phone,id_sever

            if loai == 'nanosim.vn':
                url = f'https://access.nanosim.vn/api/ig/request?api_token={key}&serviceId={service}'
                phones = s.get(url,timeout=20)
                sever_g = json.loads(phones.text)
                id_sever = sever_g['data']['session_id']
                for kt  in range(10):
                    time.sleep(1)
                    try:
                        url = f'https://access.nanosim.vn/api/ig/code?api_token={key}&sessionId={id_sever}'
                        phoness = s.get(url,timeout=20)
                        sever = json.loads(phoness.text)
                        phone = sever['data']['phone']
                        re.findall('[0-9]+', phone)[0]
                        break
                    except:
                        pass
                return  phone,id_sever

            if loai == 'otpvn.com':
                for kt  in range(10):
                    time.sleep(1)
                    try:
                        url = f'http://api.otpvn.com/?Accesskey={key}&Method=GetNumber&App={service}'
                        phones = s.get(url,timeout=20)
                        phone = phones.text.strip()
                        re.findall('[0-9]+', phone)[0]
                        id_sever = service
                        break
                    except:
                        pass
                return  phone,id_sever

            if loai == 'chothuesimcode.com':
                if number == '':
                        so = ''
                else:
                    so = f'&number={number}'
                for kt  in range(10):
                    time.sleep(1)
                    try:
                        url = f'https://chothuesimcode.com/api?act=number&apik={key}&appId={service}&carrier={network}{so}'
                        phones = s.get(url,timeout=20)
                        sever_g = json.loads(phones.text)
                        phone = sever_g['Result']['Number']
                        re.findall('[0-9]+', phone)[0]
                        id_sever = sever_g['Result']['Id']
                        break
                    except:
                        pass
                return  phone,id_sever
        except:
            return phones.text,''

def get_sms(key,service,timeout,loai,phone):
    try:
        s =  requests.session()
        s.trust_env = False
        s.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-A805N Build/LYZ28N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36'})
    except:
        return False
    for isms in range(999999999999):
        time.sleep(1)
        if isms > int(timeout):
            return False
        if loai == 'otpsim.com':
            try:
                get_sms = f'http://otpsim.com/api/sessions/{service}?token={key}'
                phone = s.get(get_sms,timeout=20)
                out = json.loads(phone.text)
                sms = out['data']['messages'][0]['sms_content']
                code = re.findall('[0-9]+', sms)[0]
                return code
            except:
                print(out)
                continue

        if loai == 'codesim.net':
            try:
                url = f'http://api.codesim.net/api/CodeSim/KiemTraGiaoDich?apikey={key}&giaodich_id={service}'
                phones = s.get(url,timeout=20)
                out = json.loads(phones.text)
                sms = out['data']['listSms'][0]['smscontent']
                code = re.findall('[0-9]+', sms)[0]
                return code
            except:
                print(out)
                continue

        if loai == 'nanosim.vn':
            try:
                url = f'https://access.nanosim.vn/api/ig/code?api_token={key}&sessionId={service}'
                phoness = s.get(url,timeout=20)
                out = json.loads(phoness.text)
                sms = out['data']['sms']
                code = re.findall('[0-9]+', sms)[0]
                return code
            except:
                print(out)
                continue

        if loai == 'otpvn.com':
            try:
                url = f'http://api.otpvn.com/?Accesskey={key}&Method=ResponseKey&App={service}&Numberphone={phone}'
                phones = s.get(url,timeout=20)
                sms = phones.text.strip()
                code = re.findall('[0-9]+', sms)[0]
                return code
            except:
                print(sms)
                continue

        if loai == 'chothuesimcode.com':
            try:
                url = f'https://chothuesimcode.com/api?act=code&apik={key}&id={service}'
                phones = s.get(url,timeout=20)
                out = json.loads(phones.text)
                sms = out['Result']['SMS']
                code = re.findall('[0-9]+', sms)[0]
                return code
            except:
                print(out)
                continue






key = 'Q9twfBZ1fBy4McB9Gtu'

# otpsim.com , codesim.net , nanosim.vn , otpvn.com , chothuesimcode.com
loai = 'nanosim.vn'
#'Mobi':'1','Vina':'2','Viettel':'3','VNMB':'4','ITelecom':'5'
networks=random.choice(['Viettel','Vina'])
# {'Telegram','Gmail','Twitter'}
dv='google'
phone,service = get_phone(key,loai,networks,dv,number='')
print(phone,service)
if service != False:
    code = get_sms(key,service,'200',loai,phone)
    print(code)
