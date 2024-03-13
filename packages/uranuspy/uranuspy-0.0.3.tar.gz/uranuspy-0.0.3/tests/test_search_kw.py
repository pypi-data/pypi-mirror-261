import re


def extract_search_intent(input_string):
    # Search for the keyword after "搜索"
    # match = re.search(
    #     r"[搜索|查|搜]\s*一下\s*([\w一-龥]+?)(?=并|$)|搜索\s*([\w一-龥]+)", input_string
    # )
    match = re.search(
        r"(?:搜|搜索|查)\s*一下\s*([\w一-龥]+?)(?=并|$)|(?:搜|搜索|查)\s*([\w一-龥]+)", input_string
    )
    if match:
        # Return the first group captured by the regex, which is the search intent
        a = match.group(1) if match.group(1) else match.group(2)
        return a.replace("一下", "")
    else:
        return None


a = [
    "搜索一下王哥的故事并汇总一个报告",
    "搜索正义填报",
    "搜索谢霆锋",
    "查一下三大队",
    "搜一下郭敬明的升高",
    "搜一下特朗普大选最新情况，汇总一个报告",
    '帮我搜一下雅加达的首都在哪里',
    '你好吗',
    '郭敬明身高'
]
for aa in a:
    b = extract_search_intent(aa)
    print(b)  # Should print: 王哥的故事, 正义填报, 谢霆锋
