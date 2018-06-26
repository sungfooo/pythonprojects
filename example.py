from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baseball-reference.com/leagues/MLB/2013-finalyear.shtml")
from bs4 import BeautifulSoup
doc = BeautifulSoup(driver.page_source, "html.parser")

careers = []
for i in doc.find_all("table")[9:10]:
    dictionary = {}
    player = i.find_all(attrs = {"data-stat": "player"})
    if player:
        for n in player[1:]:
            dictionary["Names"] = n.text.strip()
            print(n.text.strip())
    experience = i.find_all(attrs = {"data-stat": "experience"})
    if experience:
        for r in experience[1:]:
            dictionary["Years"] = r.text.strip()
    year_min = i.find_all(attrs = {"data-stat": "year_min"})
    if year_min:
        for From in year_min[1:]:
            dictionary["From"] = From.text.strip()
    year_max = i.find_all(attrs = {"data-stat": "year_max"})
    if year_max:
        for To in year_max[1:]:
            dictionary["To"] = To.text.strip()
    WAR = i.find_all(attrs = {"data-stat": "WAR_bat"})
    if WAR:
        for bat in WAR[1:]:
            dictionary["WAR"] = bat.text.strip()
    G = i.find_all(attrs = {"data-stat": "G"})
    if G:
        for g in G[1:]:
            dictionary["Games"] = g.text.strip()
    PA = i.find_all(attrs = {"data-stat": "PA"})
    if PA:
        for p in PA[1:]:
            dictionary["PA"] = p.text.strip()
    AB = i.find_all(attrs = {"data-stat": "AB"})
    if AB:
        for ab in AB[1:]:
            dictionary["AB"] = ab.text.strip()
    R = i.find_all(attrs = {"data-stat": "R"})
    if R:
        for r in R[1:]:
            dictionary["R"] = r.text.strip()
    age = i.find_all(attrs = {"data-stat": "age"})
    if age:
        for age_1 in age[1:]:
            dictionary["age"] = age_1.text.strip()
    HR = i.find_all(attrs = {"data-stat": "HR"})
    if HR:
        for hr in HR[1:]:
            dictionary["HR"] = hr.text.strip()
    H = i.find_all(attrs = {"data-stat": "H"})
    if H:
        for h in H[1:]:
            dictionary["H"] = h.text.strip()
    SB = i.find_all(attrs = {"data-stat": "SB"})
    if SB:
        for sb in SB[1:]:
            dictionary["SB"] = sb.text.strip()
    BB = i.find_all(attrs = {"data-stat": "BB"})
    if BB:
        for bb in BB[1:]:
            dictionary["BB"] = bb.text.strip()
    SO = i.find_all(attrs = {"data-stat": "SO"})
    if SO:
        for so in SO[1:]:
            dictionary["SO"] = so.text.strip()
    OPS = i.find_all(attrs = {"data-stat": "onbase_plus_slugging"})
    if OPS:
        for ops in OPS[1:]:
            dictionary["OPS"] = ops.text.strip()
    careers.append(dictionary)

print careers
