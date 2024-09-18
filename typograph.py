import re
from bs4 import BeautifulSoup

text_for_typo = (
    "<h1>”Стоимость такого решения на 30-40% дешевле покупки в рознице”, - сказал Шестаков."
    "</h1><p class=”kek” style=”color: red”>”Если возникнет повод для ее повторного переноса, "
    "Брозовский окажется в списке депутатов от ”Единой России”, которым перед выборами 2026 года "
    "будут искать замену. УГМК как раз давно присматривается к этому округу”, - намекает собеседник."
    "Такой же подход власть готова применить к Горевому. "
    "Его семье приписывают контроль над ”Хлебозаводом №7”, "
    "одним из похоронных активов и загородным клубом ”Лесная поляна”. "
    "От комментариев по этому поводу он так же воздержался. "
    "Евгений Писцов, отвечая на вопрос корреспондента о своем участии в выборах,"
    " заявил: ”Не могу комментировать информацию до ее официального оглашения”.</p>"
)


def typo(text):
    soup = BeautifulSoup(text, "html.parser")
    strings = []
    string = soup.find("h1").text
    strings.append(string)
    string2 = soup.find("p", class_="”kek”").text
    strings.append(string2)
    new_text = text
    for s in strings:
        st = s.replace(" - ", " — ")
        if st.count("”") < 2:
            result = st
        elif st.count("”") == 2:
            result = st.replace("”", "«", 1).replace("”", "»")
        elif st.count("”") > 2:
            closed = re.findall(r"\w”", st)
            for cl in closed:
                st = st.replace(cl, f"{cl[:-1]}»")
            opened = re.findall(r"”\w", st)
            for op in opened:
                st = st.replace(op, f"«{op[1:]}")
            quotes = ""
            res = []
            for sym in st:
                if sym == "«":
                    if sym == quotes:
                        sym = "„"
                        quotes = "„"
                    else:
                        quotes = "«"
                elif sym == "»":
                    if quotes == "„":
                        sym = "“"
                        quotes = "“"
                    else:
                        quotes = "»"
                res.append(sym)
            result = "".join(res)
        new_text = new_text.replace(s, result)
    return new_text


editor_text = typo(text_for_typo)
print(editor_text)
