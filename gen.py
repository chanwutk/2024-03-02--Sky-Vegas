import os


def page(repo: str, number: int, fr: int, to: int):
    _number = number - fr + 1
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Thai Grad 2024: Graduation Photos</title>
<style>
  body {'{'}
    display: flex;
    flex-direction: column;
    align-items: center;
  {'}'}
  .navigation-container {'{'}
    display: flex;
    justify-content: center;
    margin-top: 20px;
  {'}'}
  .p-btn, .n-btn {'{'}
    padding: 10px 20px;
    margin: 0 10px;
    font-size: 16px;
    cursor: pointer;
  {'}'}
  .a-img {'{'}
    width: 30%;
    height: auto;
    margin: 10px;
  {'}'}
</style>
</head>
<body>
  <div class="navigation-container">
    {f'<a href="http://chanwutk.github.io/{repo}/{(_number-1):02d}" class="p-btn">prev</a>' if number > fr else ''}
    <a href="http://chanwutk.github.io/{repo}/{(_number+1):02d}" class="n-btn">next</a>
  </div>
  <div style="display: flex; flex-direction: row; flex-wrap: wrap;">
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}0.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}0.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}1.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}1.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}2.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}2.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}3.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}3.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}4.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}4.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}5.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}5.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}6.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}6.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}7.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}7.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}8.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}8.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/FILM - {'' if number == 0 else number}9.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-FILM - {'' if number == 0 else number}9.JPG?raw=true" width=100% height=auto alt=""></a>
  </div>
  <div class="navigation-container">
    <a href="http://chanwutk.github.io/{repo}/{(_number-1):02d}" class="p-btn">prev</a>
    {f'<a href="http://chanwutk.github.io/{repo}/{(_number+1):02d}" class="p-btn">next</a>' if number < to else ''}
  </div>
  <div>
    Page {number - fr + 1} of {to - fr + 1}.
  </div>
</body>
</html>
"""

def generate(fr: int, to: int):
    os.makedirs("./docs", exist_ok=True)

    with open(f"./docs/index.html", "w") as f:
        f.write('<!DOCTYPE html>\n<html><head><meta http-equiv="refresh" content="0;url=01.html" /></head></html>')

    for i in range(fr, to + 1):
        with open(f"./docs/{(i - fr + 1):02d}.html", "w") as f:
            f.write(page('2024-03-02--Sky-Vegas', i, fr, to))

# TODO: Currently assume image number not overflowing 9999
images = [f for f in os.listdir(".") if f.startswith("FILM - ") and f.endswith(".jpeg")]
image_numbers = [int('0' + f[len('FILM - '):-len('X.jpeg')]) for f in images]

fr = min(image_numbers)
to = max(image_numbers)

generate(fr, to)