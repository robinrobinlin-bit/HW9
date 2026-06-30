### # 🌐 Live Demo

👉 [Open Live Demo](https://hw-9-gilt.vercel.app/)
Scrape Center - Movie Crawler Project (ssr2)

This repository contains a concurrent Python crawler that scrapes movie details from https://ssr2.scrape.center and downloads movie cover images locally.

## Project Structure
- [crawler.py](file:///c:/Users/admin/Desktop/HW9/crawler.py): The main scraping CLI script.
- [movies.json](file:///c:/Users/admin/Desktop/HW9/movies.json): Raw movie data output.
- [covers/](file:///c:/Users/admin/Desktop/HW9/covers/): Folder containing local downloaded JPG movie covers.

## Scraped Movie Catalog

Below is a formatted list of all 100 movies. The preview column uses relative links to the locally downloaded covers in the `covers/` folder.

| Cover | Title | Categories | Regions | Duration | Release Date | Score | Detail Link |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| <img src="covers/霸王别姬 - Farewell My Concubine.jpg" width="60" alt="霸王别姬 - Farewell My Concubine"> | **霸王别姬 - Farewell My Concubine** | 剧情, 爱情 | 中国内地, 中国香港 | 171 分钟 | 1993-07-26 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/1) |
| <img src="covers/这个杀手不太冷 - Léon.jpg" width="60" alt="这个杀手不太冷 - Léon"> | **这个杀手不太冷 - Léon** | 剧情, 动作, 犯罪 | 法国 | 110 分钟 | 1994-09-14 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/2) |
| <img src="covers/肖申克的救赎 - The Shawshank Redemption.jpg" width="60" alt="肖申克的救赎 - The Shawshank Redemption"> | **肖申克的救赎 - The Shawshank Redemption** | 剧情, 犯罪 | 美国 | 142 分钟 | 1994-09-10 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/3) |
| <img src="covers/泰坦尼克号 - Titanic.jpg" width="60" alt="泰坦尼克号 - Titanic"> | **泰坦尼克号 - Titanic** | 剧情, 爱情, 灾难 | 美国 | 194 分钟 | 1998-04-03 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/4) |
| <img src="covers/罗马假日 - Roman Holiday.jpg" width="60" alt="罗马假日 - Roman Holiday"> | **罗马假日 - Roman Holiday** | 剧情, 喜剧, 爱情 | 美国 | 118 分钟 | 1953-08-20 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/5) |
| <img src="covers/唐伯虎点秋香 - Flirting Scholar.jpg" width="60" alt="唐伯虎点秋香 - Flirting Scholar"> | **唐伯虎点秋香 - Flirting Scholar** | 喜剧, 爱情, 古装 | 中国香港 | 102 分钟 | 1993-07-01 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/6) |
| <img src="covers/乱世佳人 - Gone with the Wind.jpg" width="60" alt="乱世佳人 - Gone with the Wind"> | **乱世佳人 - Gone with the Wind** | 剧情, 爱情, 历史, 战争 | 美国 | 238 分钟 | 1939-12-15 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/7) |
| <img src="covers/喜剧之王 - The King of Comedy.jpg" width="60" alt="喜剧之王 - The King of Comedy"> | **喜剧之王 - The King of Comedy** | 剧情, 喜剧, 爱情 | 中国香港 | 85 分钟 | 1999-02-13 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/8) |
| <img src="covers/楚门的世界 - The Truman Show.jpg" width="60" alt="楚门的世界 - The Truman Show"> | **楚门的世界 - The Truman Show** | 剧情, 科幻 | 美国 | 103 分钟 | N/A | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/9) |
| <img src="covers/狮子王 - The Lion King.jpg" width="60" alt="狮子王 - The Lion King"> | **狮子王 - The Lion King** | 动画, 歌舞, 冒险 | 美国 | 89 分钟 | 1995-07-15 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/10) |
| <img src="covers/V字仇杀队 - V for Vendetta.jpg" width="60" alt="V字仇杀队 - V for Vendetta"> | **V字仇杀队 - V for Vendetta** | 剧情, 动作, 科幻, 惊悚 | 美国, 英国, 德国 | 132 分钟 | 2005-12-11 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/11) |
| <img src="covers/少年派的奇幻漂流 - Life of Pi.jpg" width="60" alt="少年派的奇幻漂流 - Life of Pi"> | **少年派的奇幻漂流 - Life of Pi** | 剧情, 奇幻, 冒险 | 美国, 中国台湾, 英国, 加拿大 | 127 分钟 | 2012-11-22 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/12) |
| <img src="covers/美丽心灵 - A Beautiful Mind.jpg" width="60" alt="美丽心灵 - A Beautiful Mind"> | **美丽心灵 - A Beautiful Mind** | 剧情, 传记 | 美国 | 135 分钟 | 2001-12-13 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/13) |
| <img src="covers/初恋这件小事 - สิ่งเล็กเล็กที่เรียกว่า...รัก.jpg" width="60" alt="初恋这件小事 - สิ่งเล็กเล็กที่เรียกว่า...รัก"> | **初恋这件小事 - สิ่งเล็กเล็กที่เรียกว่า...รัก** | 喜剧, 爱情 | 泰国 | 118 分钟 | 2012-06-05 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/14) |
| <img src="covers/借东西的小人阿莉埃蒂 - 借りぐらしのアリエッティ.jpg" width="60" alt="借东西的小人阿莉埃蒂 - 借りぐらしのアリエッティ"> | **借东西的小人阿莉埃蒂 - 借りぐらしのアリエッティ** | 动画, 奇幻, 冒险 | 日本 | 94 分钟 | 2010-07-17 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/15) |
| <img src="covers/一一 - Yi yi_ A One and a Two.jpg" width="60" alt="一一 - Yi yi: A One and a Two"> | **一一 - Yi yi: A One and a Two** | 剧情, 爱情, 家庭 | 中国台湾, 日本 | 173 分钟 | 2000-05-15 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/16) |
| <img src="covers/美丽人生 - La vita è bella.jpg" width="60" alt="美丽人生 - La vita è bella"> | **美丽人生 - La vita è bella** | 战争, 剧情, 爱情 | 意大利 | 116 分钟 | 2020-01-03 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/17) |
| <img src="covers/海上钢琴师 - La leggenda del pianista sull'oceano.jpg" width="60" alt="海上钢琴师 - La leggenda del pianista sull'oceano"> | **海上钢琴师 - La leggenda del pianista sull'oceano** | 剧情, 爱情, 音乐 | 意大利 | 126 分钟 | 2019-11-15 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/18) |
| <img src="covers/千与千寻 - 千と千尋の神隠し.jpg" width="60" alt="千与千寻 - 千と千尋の神隠し"> | **千与千寻 - 千と千尋の神隠し** | 动画, 冒险, 奇幻, 家庭 | 日本 | 125 分钟 | 2019-06-21 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/19) |
| <img src="covers/迁徙的鸟 - The Travelling Birds.jpg" width="60" alt="迁徙的鸟 - The Travelling Birds"> | **迁徙的鸟 - The Travelling Birds** | 纪录片 | 法国, 德国, 意大利, 西班牙, 瑞士 | 98 分钟 | 2001-12-12 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/20) |
| <img src="covers/黄金三镖客 - Il buono, il brutto, il cattivo..jpg" width="60" alt="黄金三镖客 - Il buono, il brutto, il cattivo."> | **黄金三镖客 - Il buono, il brutto, il cattivo.** | 西部, 冒险 | 意大利, 西班牙, 西德 | 161 分钟 | 1966-12-23 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/21) |
| <img src="covers/海洋 - Océans.jpg" width="60" alt="海洋 - Océans"> | **海洋 - Océans** | 纪录片 | 法国, 瑞士, 西班牙, 美国, 阿联酋 | 104 分钟 | 2011-08-12 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/22) |
| <img src="covers/我爱你 - 그대를 사랑합니다.jpg" width="60" alt="我爱你 - 그대를 사랑합니다"> | **我爱你 - 그대를 사랑합니다** | 剧情, 爱情 | 韩国 | 118 分钟 | 2011-02-17 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/23) |
| <img src="covers/阿飞正传 - Days of Being Wild.jpg" width="60" alt="阿飞正传 - Days of Being Wild"> | **阿飞正传 - Days of Being Wild** | 剧情, 爱情, 犯罪 | 中国香港 | 94 分钟 | 2018-06-25 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/24) |
| <img src="covers/7号房的礼物 - 7번방의 선물.jpg" width="60" alt="7号房的礼物 - 7번방의 선물"> | **7号房的礼物 - 7번방의 선물** | 剧情, 喜剧, 家庭 | 韩国 | 127 分钟 | 2013-01-23 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/36) |
| <img src="covers/爱·回家 - 집으로....jpg" width="60" alt="爱·回家 - 집으로..."> | **爱·回家 - 집으로...** | 剧情, 家庭 | 韩国 | 80 分钟 | 2002-04-05 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/25) |
| <img src="covers/龙猫 - となりのトトロ.jpg" width="60" alt="龙猫 - となりのトトロ"> | **龙猫 - となりのトトロ** | 动画, 冒险, 奇幻, 家庭 | 日本 | 86 分钟 | 2018-12-14 | ⭐ `9.1` | [Detail](https://ssr2.scrape.center/detail/26) |
| <img src="covers/七武士 - 七人の侍.jpg" width="60" alt="七武士 - 七人の侍"> | **七武士 - 七人の侍** | 剧情, 动作, 冒险 | 日本 | 207 分钟 | 1954-04-26 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/27) |
| <img src="covers/美国往事 - Once Upon a Time in America.jpg" width="60" alt="美国往事 - Once Upon a Time in America"> | **美国往事 - Once Upon a Time in America** | 剧情, 犯罪 | 意大利, 美国 | 229 分钟 | 2015-04-23 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/28) |
| <img src="covers/完美的世界 - A Perfect World.jpg" width="60" alt="完美的世界 - A Perfect World"> | **完美的世界 - A Perfect World** | 剧情, 犯罪 | 美国 | 138 分钟 | 1993-11-24 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/29) |
| <img src="covers/上帝之城 - Cidade de Deus.jpg" width="60" alt="上帝之城 - Cidade de Deus"> | **上帝之城 - Cidade de Deus** | 剧情, 犯罪 | 巴西, 法国 | 130 分钟 | N/A | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/30) |
| <img src="covers/辩护人 - 변호인.jpg" width="60" alt="辩护人 - 변호인"> | **辩护人 - 변호인** | 剧情 | 韩国 | 127 分钟 | 2013-12-18 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/31) |
| <img src="covers/忠犬八公物语 - ハチ公物語.jpg" width="60" alt="忠犬八公物语 - ハチ公物語"> | **忠犬八公物语 - ハチ公物語** | 剧情 | 日本 | 107 分钟 | 1987-08-01 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/32) |
| <img src="covers/海豚湾 - The Cove.jpg" width="60" alt="海豚湾 - The Cove"> | **海豚湾 - The Cove** | 纪录片 | 美国 | 92 分钟 | 2009-07-31 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/33) |
| <img src="covers/英雄本色 - A Better Tomorrow.jpg" width="60" alt="英雄本色 - A Better Tomorrow"> | **英雄本色 - A Better Tomorrow** | 剧情, 动作, 犯罪 | 中国香港 | 95 分钟 | 2017-11-17 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/34) |
| <img src="covers/恐怖直播 - 더 테러 라이브.jpg" width="60" alt="恐怖直播 - 더 테러 라이브"> | **恐怖直播 - 더 테러 라이브** | 剧情, 悬疑, 犯罪 | 韩国 | 97 分钟 | 2013-07-31 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/35) |
| <img src="covers/窃听风暴 - Das Leben der Anderen.jpg" width="60" alt="窃听风暴 - Das Leben der Anderen"> | **窃听风暴 - Das Leben der Anderen** | 剧情, 悬疑 | 德国 | 137 分钟 | 2006-03-23 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/37) |
| <img src="covers/时空恋旅人 - About Time.jpg" width="60" alt="时空恋旅人 - About Time"> | **时空恋旅人 - About Time** | 喜剧, 爱情, 奇幻 | 英国 | 123 分钟 | 2013-09-04 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/38) |
| <img src="covers/穿条纹睡衣的男孩 - The Boy in the Striped Pajamas.jpg" width="60" alt="穿条纹睡衣的男孩 - The Boy in the Striped Pajamas"> | **穿条纹睡衣的男孩 - The Boy in the Striped Pajamas** | 剧情, 战争 | 英国, 美国 | 94 分钟 | 2008-08-28 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/39) |
| <img src="covers/教父 - The Godfather.jpg" width="60" alt="教父 - The Godfather"> | **教父 - The Godfather** | 剧情, 犯罪 | 美国 | 175 分钟 | 2015-04-18 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/40) |
| <img src="covers/萤火之森 - 蛍火の杜へ.jpg" width="60" alt="萤火之森 - 蛍火の杜へ"> | **萤火之森 - 蛍火の杜へ** | 剧情, 爱情, 动画, 奇幻 | 日本 | 45 分钟 | 2011-09-17 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/41) |
| <img src="covers/素媛 - 소원.jpg" width="60" alt="素媛 - 소원"> | **素媛 - 소원** | 剧情 | 韩国 | 123 分钟 | 2013-10-02 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/42) |
| <img src="covers/小鞋子 - بچههای آسمان.jpg" width="60" alt="小鞋子 - بچههای آسمان"> | **小鞋子 - بچههای آسمان** | 剧情, 家庭 | 伊朗 | 89 分钟 | N/A | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/43) |
| <img src="covers/熔炉 - 도가니.jpg" width="60" alt="熔炉 - 도가니"> | **熔炉 - 도가니** | 剧情 | 韩国 | 125 分钟 | 2011-09-22 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/44) |
| <img src="covers/大话西游之大圣娶亲 - A Chinese Odyssey Part Two - Cinderella.jpg" width="60" alt="大话西游之大圣娶亲 - A Chinese Odyssey Part Two - Cinderella"> | **大话西游之大圣娶亲 - A Chinese Odyssey Part Two - Cinderella** | 喜剧, 爱情, 奇幻 | 中国香港, 中国大陆 | 110 分钟 | 2014-10-24 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/45) |
| <img src="covers/新龙门客栈 - New Dragon Gate Inn.jpg" width="60" alt="新龙门客栈 - New Dragon Gate Inn"> | **新龙门客栈 - New Dragon Gate Inn** | 动作, 爱情, 武侠, 古装 | 中国香港, 中国大陆 | 88 分钟 | 2012-02-24 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/46) |
| <img src="covers/触不可及 - Intouchables.jpg" width="60" alt="触不可及 - Intouchables"> | **触不可及 - Intouchables** | 剧情, 喜剧 | 法国 | 112 分钟 | 2011-11-02 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/47) |
| <img src="covers/钢琴家 - The Pianist.jpg" width="60" alt="钢琴家 - The Pianist"> | **钢琴家 - The Pianist** | 剧情, 音乐, 传记, 历史, 战争 | 法国, 德国, 英国, 波兰 | 150 分钟 | 2002-05-24 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/48) |
| <img src="covers/本杰明·巴顿奇事 - The Curious Case of Benjamin Button.jpg" width="60" alt="本杰明·巴顿奇事 - The Curious Case of Benjamin Button"> | **本杰明·巴顿奇事 - The Curious Case of Benjamin Button** | 剧情, 爱情, 奇幻 | 美国 | 166 分钟 | 2008-12-25 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/49) |
| <img src="covers/倩女幽魂 - A Chinese Ghost Story.jpg" width="60" alt="倩女幽魂 - A Chinese Ghost Story"> | **倩女幽魂 - A Chinese Ghost Story** | 爱情, 奇幻, 武侠, 古装 | 中国香港 | 98 分钟 | 2011-04-30 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/50) |
| <img src="covers/哈利·波特与死亡圣器（下） - Harry Potter and the Deathly Hallows_ Part 2.jpg" width="60" alt="哈利·波特与死亡圣器（下） - Harry Potter and the Deathly Hallows: Part 2"> | **哈利·波特与死亡圣器（下） - Harry Potter and the Deathly Hallows: Part 2** | 剧情, 悬疑, 奇幻, 冒险 | 英国, 美国 | 130 分钟 | 2011-08-04 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/51) |
| <img src="covers/甜蜜蜜 - Comrades_ Almost a Love Story.jpg" width="60" alt="甜蜜蜜 - Comrades: Almost a Love Story"> | **甜蜜蜜 - Comrades: Almost a Love Story** | 剧情, 爱情 | 中国香港 | 118 分钟 | 2015-02-13 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/52) |
| <img src="covers/蝙蝠侠：黑暗骑士崛起 - The Dark Knight Rises.jpg" width="60" alt="蝙蝠侠：黑暗骑士崛起 - The Dark Knight Rises"> | **蝙蝠侠：黑暗骑士崛起 - The Dark Knight Rises** | 剧情, 动作, 科幻, 惊悚, 犯罪 | 美国, 英国 | 165 分钟 | 2012-08-27 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/53) |
| <img src="covers/鬼子来了 - Devils on the Doorstep.jpg" width="60" alt="鬼子来了 - Devils on the Doorstep"> | **鬼子来了 - Devils on the Doorstep** | 剧情, 战争 | 中国大陆 | 139 分钟 | 2000-05-13 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/54) |
| <img src="covers/无敌破坏王 - Wreck-It Ralph.jpg" width="60" alt="无敌破坏王 - Wreck-It Ralph"> | **无敌破坏王 - Wreck-It Ralph** | 喜剧, 动画, 奇幻, 冒险 | 美国 | 101 分钟 | 2012-11-06 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/55) |
| <img src="covers/致命魔术 - The Prestige.jpg" width="60" alt="致命魔术 - The Prestige"> | **致命魔术 - The Prestige** | 剧情, 悬疑, 惊悚 | 美国, 英国 | 130 分钟 | 2006-10-17 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/56) |
| <img src="covers/神偷奶爸 - Despicable Me.jpg" width="60" alt="神偷奶爸 - Despicable Me"> | **神偷奶爸 - Despicable Me** | 喜剧, 动画, 冒险 | 美国, 法国 | 95 分钟 | 2010-06-20 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/57) |
| <img src="covers/断背山 - Brokeback Mountain.jpg" width="60" alt="断背山 - Brokeback Mountain"> | **断背山 - Brokeback Mountain** | 剧情, 爱情, 家庭 | 美国, 加拿大 | 134 分钟 | 2005-09-02 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/58) |
| <img src="covers/怦然心动 - Flipped.jpg" width="60" alt="怦然心动 - Flipped"> | **怦然心动 - Flipped** | 剧情, 喜剧, 爱情 | 美国 | 90 分钟 | 2010-07-26 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/59) |
| <img src="covers/驯龙高手 - How to Train Your Dragon.jpg" width="60" alt="驯龙高手 - How to Train Your Dragon"> | **驯龙高手 - How to Train Your Dragon** | 喜剧, 动画, 奇幻, 冒险 | 美国 | 98 分钟 | 2010-05-14 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/60) |
| <img src="covers/飞屋环游记 - Up.jpg" width="60" alt="飞屋环游记 - Up"> | **飞屋环游记 - Up** | 剧情, 喜剧, 动画, 冒险 | 美国 | 96 分钟 | 2009-08-04 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/61) |
| <img src="covers/黑客帝国3：矩阵革命 - The Matrix Revolutions.jpg" width="60" alt="黑客帝国3：矩阵革命 - The Matrix Revolutions"> | **黑客帝国3：矩阵革命 - The Matrix Revolutions** | 动作, 科幻 | 美国, 澳大利亚 | 129 分钟 | 2003-11-05 | ⭐ `8.8` | [Detail](https://ssr2.scrape.center/detail/62) |
| <img src="covers/速度与激情5 - Fast Five.jpg" width="60" alt="速度与激情5 - Fast Five"> | **速度与激情5 - Fast Five** | 动作, 犯罪 | 美国 | 130 分钟 | 2011-05-12 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/63) |
| <img src="covers/勇敢的心 - Braveheart.jpg" width="60" alt="勇敢的心 - Braveheart"> | **勇敢的心 - Braveheart** | 剧情, 动作, 传记, 历史, 战争 | 美国 | 177 分钟 | 1995-05-18 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/64) |
| <img src="covers/三傻大闹宝莱坞 - 3 Idiots.jpg" width="60" alt="三傻大闹宝莱坞 - 3 Idiots"> | **三傻大闹宝莱坞 - 3 Idiots** | 剧情, 喜剧, 爱情, 歌舞 | 印度 | 171 分钟 | 2011-12-08 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/65) |
| <img src="covers/闻香识女人 - Scent of a Woman.jpg" width="60" alt="闻香识女人 - Scent of a Woman"> | **闻香识女人 - Scent of a Woman** | 剧情 | 美国 | 157 分钟 | 1992-12-23 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/66) |
| <img src="covers/末代皇帝 - The Last Emperor.jpg" width="60" alt="末代皇帝 - The Last Emperor"> | **末代皇帝 - The Last Emperor** | 剧情, 传记, 历史 | 英国, 意大利, 中国大陆, 法国, 美国 | 163 分钟 | 1987-10-23 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/67) |
| <img src="covers/风之谷 - 風の谷のナウシカ.jpg" width="60" alt="风之谷 - 風の谷のナウシカ"> | **风之谷 - 風の谷のナウシカ** | 动画, 奇幻, 冒险 | 日本 | 117 分钟 | N/A | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/68) |
| <img src="covers/大话西游之月光宝盒 - A Chinese Odyssey.jpg" width="60" alt="大话西游之月光宝盒 - A Chinese Odyssey"> | **大话西游之月光宝盒 - A Chinese Odyssey** | 喜剧, 爱情, 奇幻, 古装 | 中国香港, 中国大陆 | 87 分钟 | 2014-10-24 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/69) |
| <img src="covers/放牛班的春天 - Les choristes.jpg" width="60" alt="放牛班的春天 - Les choristes"> | **放牛班的春天 - Les choristes** | 剧情, 音乐 | 法国, 德国, 瑞士 | 97 分钟 | 2004-10-16 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/70) |
| <img src="covers/当幸福来敲门 - The Pursuit of Happyness.jpg" width="60" alt="当幸福来敲门 - The Pursuit of Happyness"> | **当幸福来敲门 - The Pursuit of Happyness** | 剧情, 家庭, 传记 | 美国 | 117 分钟 | 2008-01-17 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/71) |
| <img src="covers/幽灵公主 - もののけ姫.jpg" width="60" alt="幽灵公主 - もののけ姫"> | **幽灵公主 - もののけ姫** | 动画, 奇幻, 冒险 | 日本 | 134 分钟 | 1998-05-01 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/72) |
| <img src="covers/十二怒汉 - 12 Angry Men.jpg" width="60" alt="十二怒汉 - 12 Angry Men"> | **十二怒汉 - 12 Angry Men** | 剧情 | 美国 | 96 分钟 | 1957-04-13 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/73) |
| <img src="covers/搏击俱乐部 - Fight Club.jpg" width="60" alt="搏击俱乐部 - Fight Club"> | **搏击俱乐部 - Fight Club** | 剧情, 动作, 悬疑, 惊悚 | 美国, 德国 | 139 分钟 | 1999-09-10 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/74) |
| <img src="covers/疯狂原始人 - The Croods.jpg" width="60" alt="疯狂原始人 - The Croods"> | **疯狂原始人 - The Croods** | 喜剧, 动画, 冒险 | 美国 | 98 分钟 | 2013-04-20 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/75) |
| <img src="covers/阿凡达 - Avatar.jpg" width="60" alt="阿凡达 - Avatar"> | **阿凡达 - Avatar** | 动作, 科幻, 冒险 | 美国, 英国 | 162 分钟 | 2010-01-04 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/76) |
| <img src="covers/哈尔的移动城堡 - ハウルの動く城.jpg" width="60" alt="哈尔的移动城堡 - ハウルの動く城"> | **哈尔的移动城堡 - ハウルの動く城** | 动画, 奇幻, 冒险 | 日本 | 119 分钟 | 2004-09-05 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/77) |
| <img src="covers/盗梦空间 - Inception.jpg" width="60" alt="盗梦空间 - Inception"> | **盗梦空间 - Inception** | 剧情, 科幻, 悬疑, 冒险 | 美国, 英国 | 148 分钟 | 2010-09-01 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/78) |
| <img src="covers/忠犬八公的故事 - Hachi_ A Dog's Tale.jpg" width="60" alt="忠犬八公的故事 - Hachi: A Dog's Tale"> | **忠犬八公的故事 - Hachi: A Dog's Tale** | 剧情 | 美国, 英国 | 93 分钟 | 2009-06-13 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/79) |
| <img src="covers/拯救大兵瑞恩 - Saving Private Ryan.jpg" width="60" alt="拯救大兵瑞恩 - Saving Private Ryan"> | **拯救大兵瑞恩 - Saving Private Ryan** | 剧情, 历史, 战争 | 美国 | 169 分钟 | 1998-11-13 | ⭐ `8.9` | [Detail](https://ssr2.scrape.center/detail/80) |
| <img src="covers/活着 - To Live.jpg" width="60" alt="活着 - To Live"> | **活着 - To Live** | 剧情, 家庭, 历史 | 中国大陆, 中国香港 | 132 分钟 | 1994-05-17 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/81) |
| <img src="covers/机器人总动员 - WALL·E.jpg" width="60" alt="机器人总动员 - WALL·E"> | **机器人总动员 - WALL·E** | 喜剧, 科幻, 动画 | 美国 | 98 分钟 | 2008-06-27 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/82) |
| <img src="covers/天堂电影院 - Nuovo Cinema Paradiso.jpg" width="60" alt="天堂电影院 - Nuovo Cinema Paradiso"> | **天堂电影院 - Nuovo Cinema Paradiso** | 剧情, 爱情 | 意大利, 法国 | 155 分钟 | 1988-11-17 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/83) |
| <img src="covers/指环王2：双塔奇兵 - The Lord of the Rings_ The Two Towers.jpg" width="60" alt="指环王2：双塔奇兵 - The Lord of the Rings: The Two Towers"> | **指环王2：双塔奇兵 - The Lord of the Rings: The Two Towers** | 剧情, 动作, 奇幻, 冒险 | 美国, 新西兰 | 179 分钟 | 2003-04-25 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/84) |
| <img src="covers/指环王1：护戒使者 - The Lord of the Rings_ The Fellowship of the Ring.jpg" width="60" alt="指环王1：护戒使者 - The Lord of the Rings: The Fellowship of the Ring"> | **指环王1：护戒使者 - The Lord of the Rings: The Fellowship of the Ring** | 剧情, 动作, 奇幻, 冒险 | 新西兰, 美国 | 178 分钟 | 2002-04-04 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/85) |
| <img src="covers/射雕英雄传之东成西就 - The Eagle Shooting Heroes.jpg" width="60" alt="射雕英雄传之东成西就 - The Eagle Shooting Heroes"> | **射雕英雄传之东成西就 - The Eagle Shooting Heroes** | 喜剧, 奇幻, 武侠, 古装 | 中国香港 | 113 分钟 | 1993-02-05 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/86) |
| <img src="covers/蝙蝠侠：黑暗骑士 - The Dark Knight.jpg" width="60" alt="蝙蝠侠：黑暗骑士 - The Dark Knight"> | **蝙蝠侠：黑暗骑士 - The Dark Knight** | 剧情, 动作, 科幻, 惊悚, 犯罪 | 美国, 英国 | 152 分钟 | 2008-07-14 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/87) |
| <img src="covers/无间道 - Infernal Affairs.jpg" width="60" alt="无间道 - Infernal Affairs"> | **无间道 - Infernal Affairs** | 剧情, 悬疑, 犯罪 | 中国香港 | 101 分钟 | 2003-09-05 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/88) |
| <img src="covers/教父2 - The Godfather_ Part Ⅱ.jpg" width="60" alt="教父2 - The Godfather: Part Ⅱ"> | **教父2 - The Godfather: Part Ⅱ** | 剧情, 犯罪 | 美国 | 202 分钟 | 1974-12-12 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/89) |
| <img src="covers/加勒比海盗 - Pirates of the Caribbean_ The Curse of the Black Pearl.jpg" width="60" alt="加勒比海盗 - Pirates of the Caribbean: The Curse of the Black Pearl"> | **加勒比海盗 - Pirates of the Caribbean: The Curse of the Black Pearl** | 动作, 奇幻, 冒险 | 美国 | 143 分钟 | 2003-11-21 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/90) |
| <img src="covers/哈利·波特与魔法石 - Harry Potter and the Sorcerer's Stone.jpg" width="60" alt="哈利·波特与魔法石 - Harry Potter and the Sorcerer's Stone"> | **哈利·波特与魔法石 - Harry Potter and the Sorcerer's Stone** | 奇幻, 冒险 | 美国, 英国 | 152 分钟 | 2002-01-26 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/91) |
| <img src="covers/指环王3：王者无敌 - The Lord of the Rings_ The Return of the King.jpg" width="60" alt="指环王3：王者无敌 - The Lord of the Rings: The Return of the King"> | **指环王3：王者无敌 - The Lord of the Rings: The Return of the King** | 剧情, 动作, 奇幻, 冒险 | 美国, 新西兰 | 201 分钟 | 2004-03-15 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/92) |
| <img src="covers/黑客帝国 - The Matrix.jpg" width="60" alt="黑客帝国 - The Matrix"> | **黑客帝国 - The Matrix** | 动作, 科幻 | 美国, 澳大利亚 | 136 分钟 | 2000-01-14 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/93) |
| <img src="covers/剪刀手爱德华 - Edward Scissorhands.jpg" width="60" alt="剪刀手爱德华 - Edward Scissorhands"> | **剪刀手爱德华 - Edward Scissorhands** | 剧情, 爱情, 奇幻 | 美国 | 105 分钟 | 1990-12-06 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/94) |
| <img src="covers/春光乍泄 - Happy Together.jpg" width="60" alt="春光乍泄 - Happy Together"> | **春光乍泄 - Happy Together** | 剧情, 爱情 | 中国香港, 日本, 韩国 | 96 分钟 | 1997-05-17 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/95) |
| <img src="covers/大闹天宫 - The Monkey King.jpg" width="60" alt="大闹天宫 - The Monkey King"> | **大闹天宫 - The Monkey King** | 动画, 奇幻 | 中国大陆 | 114 分钟 | 1965-12-31 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/96) |
| <img src="covers/天空之城 - 天空の城ラピュタ.jpg" width="60" alt="天空之城 - 天空の城ラピュタ"> | **天空之城 - 天空の城ラピュタ** | 动画, 奇幻, 冒险 | 日本 | 125 分钟 | 1992-05-01 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/97) |
| <img src="covers/音乐之声 - The Sound of Music.jpg" width="60" alt="音乐之声 - The Sound of Music"> | **音乐之声 - The Sound of Music** | 剧情, 爱情, 歌舞, 传记 | 美国 | 174 分钟 | 1965-03-02 | ⭐ `9.0` | [Detail](https://ssr2.scrape.center/detail/98) |
| <img src="covers/辛德勒的名单 - Schindler's List.jpg" width="60" alt="辛德勒的名单 - Schindler's List"> | **辛德勒的名单 - Schindler's List** | 剧情, 历史, 战争 | 美国 | 195 分钟 | 1993-11-30 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/99) |
| <img src="covers/魂断蓝桥 - Waterloo Bridge.jpg" width="60" alt="魂断蓝桥 - Waterloo Bridge"> | **魂断蓝桥 - Waterloo Bridge** | 剧情, 爱情, 战争 | 美国 | 108 分钟 | 1940-05-17 | ⭐ `9.5` | [Detail](https://ssr2.scrape.center/detail/100) |
