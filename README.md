<h1>[PORTFOLIO] 네이버 운세 API Server </h1>
    - 네이버 띠운세 페이지 웹크롤링 하여 API Backend 형태로 처리한다
     <p><p>
     <img src=https://github.com/ChaShane/FortuneAPI/assets/96649804/7e6eba32-61d8-4c1d-a1f6-199c2deb4d83></img>
     <p>
     <b>* 요청 - POST</b>
     <br>
     <b>&nbsp;&nbsp;1.&nbsp;헤더</b>
     <p>
      <table style="border-collapse: collapse; border="1">
      <tbody>
         <tr> 
           <th>키</th>
           <th>값</th>
           <th>설명</th>
           <th>필수</th>
         </tr>
        <tr> 
           <td>dte</td>
           <td>Number</td>
           <td>오늘일자(yyyyMMdd)</td>
           <td>O</td>
         </tr>
        <tr> 
           <td>Content-Type</td>
           <td>application/json</td>
           <td>Json 형태로 요청 </td>
           <td>X</td>
         </tr>
      </tbody>
      </table>
      <p>
       <b>&nbsp;&nbsp;2.&nbsp;Body</b>
     <p>
      <table style="border-collapse: collapse; border="1">
      <tbody>
         <tr> 
           <th>이름</th>
           <th>타입</th>
           <th>설명</th>
           <th>필수</th>
         </tr>
        <tr> 
           <td>beltstar</td>
           <td>String</td>
           <td>*&nbsp;띠 입력<br>쥐,소,호랑이,토끼,용,뱀,말,양,원숭이,닭,개,돼지</td>
           <td>O</td>
         </tr>
      </tbody>
      </table>
      <p>
     <b>* 응답</b>
     <table>
       <tbody>
         <tr>
           <td>
             {
             <br>&nbsp;&nbsp;"data": {
             <br>&nbsp;&nbsp;&nbsp;&nbsp;년도: 운세설명,
             <br>&nbsp;&nbsp;&nbsp;}
            <br>}
           </td>
         </tr>
       </tbody>
     </table>
     <p>
      <b>* 예제</b>
     <table>
       <tbody>
         <tr>
           <td>
           curl -d "{\"beltstar\": \"용\"}" -H "Content-Type: application/json" -H "dte: 20230901" <br>-X POST https://port-0-fortuneapi-6w1j2alm041d5v.sel5.cloudtype.app/todayfortune
           </td>
         </tr>
       </tbody>
     </table>   
     <p>
     - API 가이드 
      <br>&nbsp;&nbsp;&nbsp;https://port-0-fortuneapi-6w1j2alm041d5v.sel5.cloudtype.app/redoc
     
     
