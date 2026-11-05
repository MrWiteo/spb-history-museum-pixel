import json,urllib.request,urllib.parse,os,re
C=[
[("ru","Музей_Старого_Петербурга"),("ru","Государственный_музей_истории_Санкт-Петербурга"),("en","Saint_Petersburg")],
[("ru","Дом_Сюзора"),("ru","Кадетская_линия"),("en","Vasilyevsky_Island")],
[("ru","Садовая_улица_(Санкт-Петербург)"),("ru","Сенная_площадь"),("en","Saint_Petersburg")],
[("ru","Луначарский,_Анатолий_Васильевич"),("en","Anatoly_Lunacharsky")],
[("ru","Ильин,_Лев_Александрович"),("ru","Музей_города_(Санкт-Петербург)"),("ru","Аничков_дворец")],
[("ru","Аничков_дворец"),("en","Anichkov_Palace")],
[("ru","Особняк_Румянцева"),("ru","Румянцевский_особняк"),("ru","Петропавловская_крепость")],
[("ru","Санкт-Петербург"),("en","Saint_Petersburg")],
[("ru","Петропавловская_крепость"),("en","Peter_and_Paul_Fortress")],
[("ru","Комендантский_дом_(Санкт-Петербург)"),("ru","Комендантский_дом"),("ru","Петропавловская_крепость")],
[("ru","Блокада_Ленинграда"),("ru","Особняк_Румянцева")],
[("ru","Петропавловский_собор"),("en","Peter_and_Paul_Cathedral")],
[("ru","Орешек_(крепость)"),("ru","Шлиссельбургская_крепость"),("en","Oreshek_Fortress")],
[("ru","Санкт-Петербург"),("en","Saint_Petersburg")]]
os.makedirs('www/img',exist_ok=True)
H={'User-Agent':'museum-app/1.0 (https://github.com/MrWiteo/spb-history-museum-pixel)'}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40).read()
for i,cands in enumerate(C):
    for lang,t in cands:
        try:
            d=json.loads(get('https://%s.wikipedia.org/api/rest_v1/page/summary/%s'%(lang,urllib.parse.quote(t))))
            src=(d.get('thumbnail') or {}).get('source')
            if not src: raise Exception('no thumb')
            src=re.sub(r'/\d+px-','/960px-',src)
            open('www/img/%d.jpg'%(i+1),'wb').write(get(src))
            print('ok',i+1,lang,t);break
        except Exception as e:
            print('miss',i+1,lang,t,e)
