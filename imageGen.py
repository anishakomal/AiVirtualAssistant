import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"Bearer sk-enter api key",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "indian girl wearing ethnic dress",
        "output_format": "png",
    },
)

if response.status_code == 200:
    with open("./girl.png", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))


