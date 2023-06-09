import random
menuDict = {'炙烤味噌美乃滋鮭魚': 40,'生鮭魚(一貫)': 40,
            '青森扇貝': 40,'奶油乳酪鮭魚': 40,
            '炙烤照燒鮭魚': 40,'炙烤起司鮭魚': 40,
            '鮭魚肚': 40, '洋蔥鮭魚': 40,
            '蒲燒鮭魚(一貫)': 40, '燒炙鮭魚肚': 40,
            '熟成鮪魚': 40, '炙烤鮪魚中脂(一貫)': 80,
            '熟成鮪魚中脂(一貫)': 80,
            '柚香醃漬鮪魚': 40,
            '炙烤照燒長鰭鮪魚': 40,
            '究極蟹肉棒': 40, '酪梨鮮蝦': 40,
            '炙烤起司鮮蝦': 40, '大生鮮蝦(一貫)': 40,
            '甜蝦': 40, '蝦仁天婦羅握壽司': 40,
            '鮮蝦': 40, '北寄貝': 40,
            '香煎芝麻扇貝': 40, '北海道大帆立貝': 80,
            '稻荷壽司': 40, '星鰻': 40,
            '北海道生章魚': 40, '玉子燒': 40,
            '花枝': 40, '炙烤起司豬五花': 40,
            '炙烤蒲燒鰻魚': 80, '秋刀魚': 40,
            '鰈魚緣側': 40, '香烤鯖魚': 40,
            '鮭魚肚軍艦': 40, '鮭魚卵軍艦': 40,
            '熟成鮪魚脂軍艦': 80, '蔥花鮪魚軍艦': 40,
            '鹽味半熟蛋鮪魚軍艦': 40, '照燒肉丸軍艦': 40,
            '柚香小貝柱軍艦': 40, '飛魚卵軍艦': 40,
            '鮮蝦沙拉軍艦': 40, '海膽軍艦': 40,
            '納豆軍艦': 40, '玉米沙拉軍艦': 40,
            '白身魚天婦羅手卷': 40, '鮮蝦生菜手卷': 40,
            '鮪魚生菜手卷': 40, '炸蝦天婦羅手卷': 40, '鐵火卷': 40,
            '黃瓜卷': 40, '黃金酥脆卷': 80, '酥脆炸蝦卷': 80, '味噌湯': 60,
            '7種魚介濃厚味噌拉麵': 130, '茶碗蒸': 60, '毛豆': 40,
            '青花菜沙拉': 40, '黄金薯條': 60, '和風唐揚雞': 60,
            '香菇天婦羅': 60, '炸蝦天婦羅': 60, '豆皮烏龍麵': 90,
            '7種魚介豚骨醬油拉麵': 130, '醇濃辣味芝麻豬肉烏龍麵': 130,
            '釜玉烏龍麵(溫)': 90, '豆乳甜甜圈': 90, '北海道牛奶布丁塔': 40,
            '北海道千層蛋糕': 80, '北海道牛奶霜淇淋': 40, '抹茶牛奶霜淇淋': 40,
            '靜岡抹茶霜淇淋': 40, '京都風蕨餅': 60, '鯛魚燒霜淇淋': 90,
            '100%純蘋果汁(非濃縮還原)': 60, '100%純柳橙汁(非濃縮還原)': 60,
            '啤酒(瓶)': 90}

set_money = int(input("請輸入最高金額:"))
keyList =[i for i in menuDict.keys()]
resultList = []
total_money = 0
while True:
    chosen = keyList[random.randint(0,len(keyList)-1)]
    resultList.append(chosen)
    total_money += menuDict[chosen]
    if total_money > set_money:
        resultList.remove(chosen)
        total_money -= menuDict[chosen]
        break

print("結果:{}".format(resultList))
print("合計金額:{}元".format(total_money))