from typing import Dict,Optional
from pydantic import BaseModel,Field
from fastapi import Body



class Model_Respone(BaseModel):
    data: Dict[str, str]=Field(None, description="년도 : 운세설명")
    Error: Optional[str]=Field(None)
    class Config:
       schema_extra = {
            "example":  {
                        "data": {
                            "1952": "오늘 하루는 생각지도 못한 재운이 넘쳐나는 하루다. 다른 사람에게 베풀도록 하라.",
                            "1964": "저녁 회식자리에서 몸가짐을 조심하는 게 좋다. 다른 사람에게 트집 잡힐 일은 주의하라.",
                            "1976": "독서로 마음의 양식을 풍족하게 하는 편이 사람들과 어울리는 것보다 유리할 것이다.",
                            "1988": "오늘 하루는 이성 문제로 고민거리가 있다면 속 시원히 터놓고 말할 필요가 있다.",
                            "2000": "당신의 지나간 것들은 인생의 서장에 불과 하다. 앞으로 많은 장들이 남았다."
                                }
                         }
                      }              

class Model_Request(BaseModel):
    beltstar : str =Body(..., description="띠 입력 : 쥐,소,호랑이,토끼,용,뱀,말,양,원숭이,닭,개,돼지")
    class Config:
       schema_extra = { "example":  {"beltstar":"용"} }    



    