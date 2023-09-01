from model import Model_Request,Model_Respone #데이터 형식 모델 정의
from bs4 import BeautifulSoup as bs #웹크로링 라이브러리
from fastapi import FastAPI,Request,Header #FAST API 라이브러리 
from fastapi.responses import JSONResponse
from datetime import datetime #현재시간 가져오기
import uvicorn # ASGI(Asynchronous Server Gateway Interface) 비동기 처리 라이브러리
import urllib 
from urllib.request import Request as r, urlopen

#FastAPI 선언
app = FastAPI(docs_url=None,redoc_documentation_url=None,title="네이버 띠운세 API")

@app.post("/todayfortune",response_model=Model_Respone,response_model_exclude_none=True)
async def TodayFortune(unsae:Model_Request,req:Request,dte:str=Header(..., description="오늘일자(yyyyMMdd)")):

    current_datetime = datetime.now()
    dt = current_datetime.strftime('%Y%m%d')
    #Header에 오늘일자(yyyyMMdd) 판단
    if dt!=dte : 
        return JSONResponse(content={"Error":"잘못된 Header 값입니다."}, status_code=401)
    else:
        try:
            #Body 띠(beltstar)의 값을 가져온다
            body = await req.json()
            beltstar = body['beltstar']
            ddi="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="+urllib.parse.quote(beltstar + "띠+운세", encoding='utf-8')

            req = r(
                url=ddi, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            html = urlopen(req).read()
            print(html)
            soup = bs(html, 'html.parser')
            data1 = soup.select('div.api_cs_wrap > div#yearFortune > div.infors > dl')

            #해당 데이터 체크
            if len(data1) ==0:
                return JSONResponse(content={"Error":"잘못된 Body 값 입니다."}, status_code=412) 
            
            #운세 데이터가 있으면 dict(JSON) 형태로 보낸다
            json={}
            unsae ={}
            for item in data1:
                style_attr = item.get('style')
                #웹크롤링 후 data1 값은 내일, 이주 운세 데이터도 나오지만 오늘운세만 출력하기위해 제외!
                if style_attr is None or 'display:none' not in style_attr:
                    dt_elements = item.select('dt')
                    dd_elements = item.select('dd')
                    
                    for dt, dd in zip(dt_elements, dd_elements):
                        dt_text = dt.getText()
                        dd_text = dd.getText()
                        unsae[dt_text[:4]]=dd_text

            json["data"]=unsae                        
            return json                        
        except Exception as e:         
            return JSONResponse(content={"Error": str(e)}, status_code=500)
                 

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7891)













