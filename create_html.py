import pdfkit
from json import loads
from random import choice, shuffle

html = """
<!DOCTYPE html>
<html>
<meta charset="utf-8">

<body>
  <table border="1">
{}

{}
  </table>
</body>

</html>"""

options = {
    'page-size': 'A4',
    'margin-top': '0.1in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'encoding': "UTF-8",
    'no-outline': None,
    'disable-smart-shrinking': '',
}

with open(r'./test.json', encoding='utf-8') as fh:
    json_txt = fh.read()
    json_txt = str(json_txt).replace('True', 'true').replace('False', 'false')
    test_data = loads(json_txt)

question_list = list(test_data.items())

text = ""
all_answer = []
for i in range(15):
    answer_list = []
    answer = choice(question_list)

    all_answer.append(answer[0])
    answer_list.append(answer[0])

    for _ in range(3):
        answer_list.append(choice(question_list)[0])

    shuffle(answer_list)
    text += f"      <tr>\n       　<th  colspan='4' style='text-align: left;'>{i+1}問: {answer[1][1]}</th>\n      </tr>\n"
    for num, ans in enumerate(answer_list):
        text += f"      <th style='text-align: left;'>{num+1}: {ans}</th>\n"
    text += "\n"
text = text[:-1]

text2 = f"      <tr>\n       　<th  colspan='4' style='text-align: left;'>答え：</th>\n      </tr>\n"

for num, ans in enumerate(all_answer):
    num += 1
    text2 += f"      <th style='text-align: left;'>{num}: {ans}</th>\n"
    if num % 4 == 0:
        text2 += f"      <tr></tr>\n"

text2 = text2[:-1]

last_html = html.format(text, text2)
with open(r'./index1.html', mode='w', encoding='utf-8') as f:
    f.write(last_html)

config = pdfkit.configuration(wkhtmltopdf=r'https://github.com/Anijaaaaaaaaaaa/html.github.io/releases/download/2020-08-16/wkhtmltopdf.exe')
pdfkit.from_string(last_html, '四字熟語.pdf', options=options, configuration=config)

