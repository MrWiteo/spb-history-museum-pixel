import json,urllib.request,os,re
T=["Peter_and_Paul_Fortress","Peter_the_Great","Treaty_of_Nystad","Decembrist_revolt","Emancipation_reform_of_1861","Saint_Petersburg","February_Revolution","Russian_Revolution"]
os.makedirs('www/img',exist_ok=True)
H={'User-Agent':'museum-app/1.0 (https://github.com/MrWiteo/spb-history-museum-pixel)'}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40).read()
for i,t in enumerate(T):
    try:
        d=json.loads(get('https://en.wikipedia.org/api/rest_v1/page/summary/'+t))
        src=(d.get('thumbnail') or {}).get('source')
        src=re.sub(r'/\d+px-','/960px-',src)
        open('www/img/%d.jpg'%(i+1),'wb').write(get(src))
        print('ok',t,src)
    except Exception as e:
        print('fail',t,e)
