import requests
import json
import streamlit as st

st.title("demo app")
st.write("soru sor")

input=st.text_input("buraya soru sor")
if input is not None:
    btn=st.button("submit")
    if btn:

      url = "https://api.openai.com/v1/chat/completions"
      
      payload = json.dumps({
        "model": "gpt-3.5-turbo-0125",
        "messages": [
          {
            "role": "system",
            "content": "sen yardımsever bir cahtbot asistansın"
          },
          {
            "role": "user",
            "content": input
          }
        ]
      })
      headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer OPENAI_API_KEY_BURAYA_YAZILMALI',
        'Cookie': '__cf_bm=tplJk6QQNE76bI1x5UuzQ1Guf0_h.PDN3pHCUBh8i3Q-1720419060-1.0.1.1-D0XP8Mmih9_K8HbhtMTYc1RhtfBXiyJ.xI5p30MTUIHO0YJXjVhz3iC_kYEZmaxBihuRkVQnFLgkENxwZI0bvg; _cfuvid=drGaERzeppvUCxrCUYzn5RH8Rc2ZohX7bEYJnkP8AuI-1720419060763-0.0.1.1-604800000'
      }
      
      response = requests.request("POST", url, headers=headers, data=payload)
      data=response.json()
      st.write(data["choices"][0]["message"]["content"])
