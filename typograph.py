import re
from bs4 import BeautifulSoup

tags = [
    "span",
    "p",
    "b",
    "a",
    "div",
    "li",
    "h1",
    "h2",
    "h3",
    "button",
    "small",
    "strong",
    "td",
    "img",
    "input",
    "title",
    "meta",
]


def typo(text):
    strings = []
    soup = BeautifulSoup(text, "html.parser")
    for tag in tags:
        try:
            string = soup.find(tag).text
            strings.append(string)
        except AttributeError:
            pass
    new_text = text
    for s in strings:
        st = s.replace(" - ", " — ")
        if st.count("”") < 2:
            result = st
        elif st.count("”") >= 2:
            dub_opened = re.findall(r"(\W””|””\w)", t)
            for op in dub_opened:
                st = st.replace(op, f"{op[-3:-2]}««")
            dub_closed = re.findall(r"(””\W|\w””)", t)
            for cl in dub_closed:
                st = st.replace(cl, f"{cl[-3:-2]}»»")
            opened = re.findall(r"(^”\w|\W”\w)", st)
            for op in opened:
                st = st.replace(op, f"{op[-3:-2]}«{op[-1:]}")
            closed = re.findall(r"(\w”$|\w”\W)", st)
            for cl in closed:
                st = st.replace(cl, f"{cl[0]}»{cl[2:]}")
            quotes = ""
            res = []
            for sym in st:
                if sym == "«":
                    if sym == quotes or quotes == "“":
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


t = '<p>”d” ”d” ”d” ””d” ”d”” ”d” ”d ”d”” ”d”</p>'
res = typo(t)
print(res)
