from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

ATTRACTIONS = {

    # ===== 東京ディズニーランド ===== #


    "オムニバス": {
        "park": "land",
        "category": "散策",
        "thrill": 1,
        "photo": 3,
        "date": 2,
        "family": 3,
        "popularity": 2
    },

    "ペニーアーケード": {
        "park": "land",
        "category": "散策",
        "thrill": 1,
        "photo": 2,
        "date": 2,
        "family": 3,
        "popularity": 2
    },

    "ウエスタンリバー鉄道": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 3,
        "date": 2,
        "family": 5,
        "popularity": 2
    },

    "カリブの海賊": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 2,
        "photo": 3,
        "date": 3,
        "family": 3,
        "popularity": 5
    },

    "ジャングルクルーズ：ワイルドライフ・エクスペディション": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 3,
        "date": 2,
        "family": 5,
        "popularity": 5
    },

    "スイスファミリー・ツリーハウス": {
        "park": "land",
        "category": "散策",
        "thrill": 1,
        "photo": 3,
        "date": 2,
        "family": 3,
        "popularity": 2
    },

    "魅惑のチキルーム：スティッチ・プレゼンツ“アロハ・エ・コモ・マイ！”": {
        "park": "land",
        "category": "ショー",
        "thrill": 1,
        "photo": 2,
        "date": 2,
        "family": 4,
        "popularity": 2
    },

    "ウエスタンランド・シューティングギャラリー": {
        "park": "land",
        "category": "散策",
        "thrill": 2,
        "photo": 2,
        "date": 2,
        "family": 3,
        "popularity": 2
    },

    "カントリーベア・シアター": {
        "park": "land",
        "category": "ショー",
        "thrill": 1,
        "photo": 2,
        "date": 2,
        "family": 4,
        "popularity": 2
    },

    "蒸気船マークトウェイン号": {
        "park": "land",
        "category": "散策",
        "thrill": 1,
        "photo": 4,
        "date": 4,
        "family": 4,
        "popularity": 2
    },

    "トムソーヤ島いかだ": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 3,
        "date": 2,
        "family": 4,
        "popularity": 2
    },

    "ビッグサンダー・マウンテン": {
        "park": "land",
        "category": "絶叫",
        "thrill": 4,
        "photo": 3,
        "date": 3,
        "family": 2,
        "popularity": 10
    },

    "スプラッシュ・マウンテン": {
        "park": "land",
        "category": "絶叫",
        "thrill": 5,
        "photo": 3,
        "date": 3,
        "family": 2,
        "popularity": 10
    },

    "ビーバーブラザーズのカヌー探険": {
        "park": "land",
        "category": "散策",
        "thrill": 2,
        "photo": 3,
        "date": 2,
        "family": 3,
        "popularity": 2
    },

    "アリスのティーパーティー": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 2,
        "photo": 3,
        "date": 3,
        "family": 4,
        "popularity": 5
    },

    "イッツ・ア・スモールワールド": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 4,
        "date": 3,
        "family": 5,
        "popularity": 8
    },

    "キャッスルカルーセル": {
        "park": "land",
        "category": "映え",
        "thrill": 1,
        "photo": 4,
        "date": 4,
        "family": 4,
        "popularity": 5
    },

    "白雪姫と七人のこびと": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 2,
        "photo": 2,
        "date": 2,
        "family": 3,
        "popularity": 2
    },

    "シンデレラのフェアリーテイル・ホール": {
        "park": "land",
        "category": "映え",
        "thrill": 1,
        "photo": 5,
        "date": 5,
        "family": 4,
        "popularity": 2
    },

    "空飛ぶダンボ": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 4,
        "date": 3,
        "family": 5,
        "popularity": 5
    },

    "美女と野獣“魔法のものがたり”": {
        "park": "land",
        "category": "デート",
        "thrill": 2,
        "photo": 5,
        "date": 5,
        "family": 4,
        "popularity": 10
    },

    "ピーターパン空の旅": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 3,
        "date": 3,
        "family": 4,
        "popularity": 2
    },

    "ピノキオの冒険旅行": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 2,
        "date": 2,
        "family": 3,
        "popularity": 2
    },

    "プーさんのハニーハント": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 4,
        "date": 3,
        "family": 5,
        "popularity": 10
    },

    "ミッキーのフィルハーマジック": {
        "park": "land",
        "category": "ショー",
        "thrill": 1,
        "photo": 2,
        "date": 3,
        "family": 5,
        "popularity": 5
    },

    "ホーンテッドマンション": {
        "park": "land",
        "category": "デート",
        "thrill": 2,
        "photo": 4,
        "date": 4,
        "family": 3,
        "popularity": 8
    },

    "ガジェットのゴーコースター": {
        "park": "land",
        "category": "絶叫",
        "thrill": 3,
        "photo": 2,
        "date": 2,
        "family": 3,
        "popularity": 2
    },

    "グーフィーのペイント＆プレイハウス": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 2,
        "date": 1,
        "family": 4,
        "popularity": 2
    },

    "チップとデールのツリーハウス": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 3,
        "date": 1,
        "family": 4,
        "popularity": 2
    },

    "トゥーンパーク": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 3,
        "date": 1,
        "family": 5,
        "popularity": 2
    },

    "ドナルドのボート": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 3,
        "date": 1,
        "family": 4,
        "popularity": 2
    },

    "ミニーの家": {
        "park": "land",
        "category": "映え",
        "thrill": 1,
        "photo": 5,
        "date": 3,
        "family": 4,
        "popularity": 2
    },

    "ロジャーラビットのカートゥーンスピン": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 2,
        "photo": 3,
        "date": 2,
        "family": 4,
        "popularity": 5
    },

    "スター・ツアーズ：ザ・アドベンチャーズ・コンティニュー": {
        "park": "land",
        "category": "絶叫",
        "thrill": 3,
        "photo": 2,
        "date": 2,
        "family": 3,
        "popularity": 8
    },

    "スティッチ・エンカウンター": {
        "park": "land",
        "category": "ショー",
        "thrill": 1,
        "photo": 2,
        "date": 2,
        "family": 4,
        "popularity": 5
    },

    "ベイマックスのハッピーライド": {
        "park": "land",
        "category": "絶叫",
        "thrill": 2,
        "photo": 4,
        "date": 3,
        "family": 4,
        "popularity": 10
    },

    "モンスターズ・インク“ライド＆ゴーシーク！”": {
        "park": "land",
        "category": "ファミリー",
        "thrill": 1,
        "photo": 3,
        "date": 2,
        "family": 5,
        "popularity": 8
    },


# ===== 東京ディズニーシー =====

"ソアリン：ファンタスティック・フライト": {
    "park": "sea",
    "category": "映え",
    "thrill": 2,
    "photo": 5,
    "date": 5,
    "family": 3,
    "popularity": 8
},

"ヴェネツィアン・ゴンドラ": {
    "park": "sea",
    "category": "デート",
    "thrill": 1,
    "photo": 5,
    "date": 5,
    "family": 3,
    "popularity": 8
},

"フォートレス・エクスプロレーション": {
    "park": "sea",
    "category": "散策",
    "thrill": 1,
    "photo": 4,
    "date": 3,
    "family": 4,
    "popularity": 2
},

"ディズニーシー・トランジットスチーマーライン": {
    "park": "sea",
    "category": "散策",
    "thrill": 1,
    "photo": 4,
    "date": 4,
    "family": 4,
    "popularity": 5
},

"タワー・オブ・テラー": {
    "park": "sea",
    "category": "絶叫",
    "thrill": 5,
    "photo": 3,
    "date": 2,
    "family": 1,
    "popularity": 10
},

"トイ・ストーリー・マニア！": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 4,
    "date": 3,
    "family": 5,
    "popularity": 10
},

"タートル・トーク": {
    "park": "sea",
    "category": "ショー",
    "thrill": 1,
    "photo": 2,
    "date": 2,
    "family": 5,
    "popularity": 8
},

"ニモ＆フレンズ・シーライダー": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 2,
    "photo": 2,
    "date": 2,
    "family": 5,
    "popularity": 8
},

"アクアトピア": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 2,
    "photo": 3,
    "date": 2,
    "family": 4,
    "popularity": 10
},

"インディ・ジョーンズ®・アドベンチャー：クリスタルスカルの魔宮": {
    "park": "sea",
    "category": "絶叫",
    "thrill": 4,
    "photo": 3,
    "date": 2,
    "family": 2,
    "popularity": 8
},

"レイジングスピリッツ": {
    "park": "sea",
    "category": "絶叫",
    "thrill": 5,
    "photo": 2,
    "date": 2,
    "family": 1,
    "popularity": 8
},

"ラプンツェルのランタンフェスティバル": {
    "park": "sea",
    "category": "映え",
    "thrill": 1,
    "photo": 5,
    "date": 5,
    "family": 4,
    "popularity": 10,
},

"アナとエルサのフローズンジャーニー": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 5,
    "date": 4,
    "family": 5,
    "popularity": 10
},

"ピーターパンのネバーランドアドベンチャー": {
    "park": "sea",
    "category": "絶叫",
    "thrill": 3,
    "photo": 4,
    "date": 3,
    "family": 4,
    "popularity": 10
},

"フェアリー・ティンカーベルのビジーバギー": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 4,
    "date": 2,
    "family": 5,
    "popularity": 8
},

"シンドバッド・ストーリーブック・ヴォヤッジ": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 3,
    "date": 2,
    "family": 5,
    "popularity": 5
},

"ジャスミンのフライングカーペット": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 2,
    "photo": 4,
    "date": 3,
    "family": 4,
    "popularity": 8
},

"マジックランプシアター": {
    "park": "sea",
    "category": "ショー",
    "thrill": 1,
    "photo": 3,
    "date": 2,
    "family": 4,
    "popularity": 8
},

"キャラバンカルーセル": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 4,
    "date": 3,
    "family": 5,
    "popularity": 5
},

"フランダーのフライングフィッシュコースター": {
    "park": "sea",
    "category": "絶叫",
    "thrill": 3,
    "photo": 2,
    "date": 2,
    "family": 4,
    "popularity": 5
},

"スカットルのスクーター": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 3,
    "date": 2,
    "family": 4,
    "popularity": 5
},

"ジャンピン・ジェリーフィッシュ": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 3,
    "date": 2,
    "family": 4,
    "popularity": 5
},

"ブローフィッシュ・バルーンレース": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 3,
    "date": 2,
    "family": 4,
    "popularity": 5
},

"ワールプール": {
    "park": "sea",
    "category": "ファミリー",
    "thrill": 1,
    "photo": 2,
    "date": 2,
    "family": 4,
    "popularity": 2
},

"海底2万マイル": {
    "park": "sea",
    "category": "散策",
    "thrill": 2,
    "photo": 3,
    "date": 3,
    "family": 4,
    "popularity": 5
},

"センター・オブ・ジ・アース": {
    "park": "sea",
    "category": "絶叫",
    "thrill": 5,
    "photo": 3,
    "date": 2,
    "family": 1,
    "popularity": 10
}

}

LAND_ATTRACTIONS = {}

SEA_ATTRACTIONS = {}

for name, data in ATTRACTIONS.items():

    if data["park"] == "land":

        LAND_ATTRACTIONS[name] = data

    elif data["park"] == "sea":

        SEA_ATTRACTIONS[name] = data

ATTRACTION_URLS = {

    # =====================
    # 東京ディズニーランド
    # =====================

    "美女と野獣“魔法のものがたり”":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/197/",

    "ベイマックスのハッピーライド":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/196/",

    "プーさんのハニーハント":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/174/",

    "ビッグサンダー・マウンテン":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/160/",

    "スプラッシュ・マウンテン":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/162/",

    "モンスターズ・インク“ライド＆ゴーシーク！”":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/189/",

    "ホーンテッドマンション":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/171/",

    "スター・ツアーズ：ザ・アドベンチャーズ・コンティニュー":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/183/",

    "ジャングルクルーズ：ワイルドライフ・エクスペディション":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/153/",

    "ウエスタンリバー鉄道":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/154/",

    "カリブの海賊":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/152/",

    "イッツ・ア・スモールワールド":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/172/",

    "空飛ぶダンボ":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/169/",

    "ピーターパン空の旅":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/164/",

    "白雪姫と七人のこびと":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/165/",

    "ピノキオの冒険旅行":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/168/",

    "ガジェットのゴーコースター":
    "https://www.tokyodisneyresort.jp/tdl/attraction/detail/179/",

    # =====================
    # 東京ディズニーシー
    # =====================

    "ソアリン：ファンタスティック・フライト":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/219/",

    "タワー・オブ・テラー":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/243/",

    "センター・オブ・ジ・アース":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/223/",

    "レイジングスピリッツ":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/242/",

    "インディ・ジョーンズ®・アドベンチャー：クリスタルスカルの魔宮":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/222/",

    "トイ・ストーリー・マニア！":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/218/",

    "ニモ＆フレンズ・シーライダー":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/247/",

    "タートル・トーク":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/246/",

    "アクアトピア":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/234/",

    "海底2万マイル":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/224/",

    "シンドバッド・ストーリーブック・ヴォヤッジ":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/235/",

    "ジャスミンのフライングカーペット":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/220/",

    "マジックランプシアター":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/226/",

    "ヴェネツィアン・ゴンドラ":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/230/",

    "ディズニーシー・トランジットスチーマーライン":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/227/",

    "アナとエルサのフローズンジャーニー":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/255/",

    "ラプンツェルのランタンフェスティバル":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/256/",

    "ピーターパンのネバーランドアドベンチャー":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/257/",

    "フェアリー・ティンカーベルのビジーバギー":
    "https://www.tokyodisneyresort.jp/tds/attraction/detail/258/"
}

RESTAURANT_URLS = {

    # =====================
    # 東京ディズニーランド
    # =====================

    "ブルーバイユー・レストラン":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/318/",

    "クイーン・オブ・ハートのバンケットホール":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/349/",

    "プラズマ・レイズ・ダイナー":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/352/",

    "グランマ・サラのキッチン":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/344/",

    "ハングリーベア・レストラン":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/338/",

    "センターストリート・コーヒーハウス":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/306/",

    "れすとらん北齋":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/313/",

    "イーストサイド・カフェ":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/300/",

    "クリスタルパレス・レストラン":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/323/",

    "プラザパビリオン・レストラン":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/335/",

    "キャンプ・ウッドチャック・キッチン":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/339/",

    "ポリネシアンテラス・レストラン":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/326/",

    "リフレッシュメントコーナー":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/303/",

    "トゥモローランド・テラス":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/357/",

    "パン・ギャラクティック・ピザ・ポート":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/353/",

    "ヒューイ・デューイ・ルーイのグッドタイム・カフェ":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/362/",

    "スウィートハート・カフェ":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/316/",

    "ソフトランディング":
    "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/354/",


    # =====================
    # 東京ディズニーシー
    # =====================

    "マゼランズ":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/412/",

    "リストランテ・ディ・カナレット":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/408/",

    "S.S.コロンビア・ダイニングルーム":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/425/",

    "テディ・ルーズヴェルト・ラウンジ":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/429/",

    "レストラン櫻":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/421/",

    "ホライズンベイ・レストラン":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/431/",

    "カフェ・ポルトフィーノ":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/400/",

    "ザンビーニ・ブラザーズ・リストランテ":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/409/",

    "ミゲルズ・エルドラド・キャンティーナ":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/456/",

    "ユカタン・ベースキャンプ・グリル":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/459/",

    "ドックサイドダイナー":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/441/",

    "ニューヨーク・デリ":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/416/",

    "ヴォルケイニア・レストラン":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/418/",

    "カスバ・フードコート":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/441/",

    "セバスチャンのカリプソキッチン":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/438/",

    "マンマ・ビスコッティーズ・ベーカリー":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/406/",

    "ケープコッド・クックオフ":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/446/",

    "リバティ・ランディング・ダイナー":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/414/",

    "バーナクル・ビルズ":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/415/",

    "ハドソンリバー・ハーベスト":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/413/",

    # ロストリバーデルタ

    "エクスペディション・イート":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/458/",

    # ミステリアスアイランド

    "ノーチラスギャレー":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/443/",

    "リフレスコス":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/444/",

    # メディテレーニアンハーバー

    "ゴンドリエ・スナック":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/404/",

    # ファンタジースプリングス

    "スナグリーダックリング":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/451/",

    "アレンデール・ロイヤルバンケット":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/452/",

    "ルックアウト・クックアウト":
    "https://www.tokyodisneyresort.jp/tds/restaurant/detail/454/",

    "フードワゴン巡り":
    "https://www.tokyodisneyresort.jp/tds/food/detail/16613058751/"
}
# =====================
# 診断結果データ
# =====================
results = {

    "デート職人": {

        "description":
        "雰囲気と特別感を大切にするタイプ。夜景やロマンチックなスポット選びが得意。",


        "food":
        "季節限定の映えフード、予約を取ってレストラン",

        "strategy":
        "昼はアトラクション、夕方は写真撮影、夜は夜景を楽しもう",

        "morning" :
        "開園直後は人気アトラクションを優先しよう。",

        "afternoon":
        "写真スポット巡りがおすすめ。",

        "night":
        "夜景とロマンチックな雰囲気を楽しむベストタイム！",

    },

    "子連れマスター": {

        "description":
        "休憩場所や移動効率まで考える家族のプロ。",

        "food":
        "ポップコーン、ハンバーガー、ポテト。モバイルオーダーも使いこなせると最高！",

        "strategy":
        "無理に詰め込まず休憩を挟みながら回ろう",

        "morning":
        "朝は元気なうちに人気アトラクションを回ろう。",

        "afternoon":
        "疲れが出やすい時間帯。休憩を挟みながら回ろう。",

        "night":
        "無理せずお土産を見ながらゆったり過ごそう。",


    },

    "DPA課金ガチ勢": {

        "description":
        "待ち時間ゼロを目指す効率厨。DPAもモバイルオーダーも使いこなす。",


        "food":
        "レストラン予約推奨。モバイルオーダーも活用！",

        "strategy":
        "朝一でDPA取得して効率重視",

        "morning":
        "開園後すぐにDPAやプライオリティパスを確保しよう。",

        "afternoon":
        "人気アトラクションを効率良く回る勝負の時間帯。",

        "night":
        "残った人気アトラクションを回収して完全攻略を目指そう。",


    },

    "食べ歩き王": {

        "description":
        "アトラクションよりフード情報をチェックしているタイプ。",


        "food":
        "チュロス、餃子ドッグ、ポップコーン",

        "strategy":
        "フードワゴンを巡ろう",

        "morning":
        "まずは今日食べたいフードをリサーチしよう。",

        "afternoon":
        "食べ歩きゴールデンタイム！気になるフードを制覇しよう。",

        "night":
        "売り切れ前に食べたいフードを確保しよう。",


    },

    "ショーオタク": {

        "description":
        "ショー開始30分前には待機している本気勢。",


        "food":
        "ショー待機中に軽食",

        "strategy":
        "ショースケジュールを中心に動こう",

        "morning":
        "ショースケジュールを確認して一日の計画を立てよう。",

        "afternoon":
        "人気ショーの待機列や観覧場所をチェックしよう。",

        "night":
        "夜のショーやパレードが本番！ベストポジションを確保しよう。",
       

    },

    "絶叫ジャンキー": {

        "description":
        "スリルのためなら長時間待機も惜しまないタイプ。",


        "food":
        "ターキーレッグ。モバイルオーダーで食事時間も短縮！",

        "strategy":
        "人気絶叫アトラクションを優先",

        "morning":
        "待ち時間の短いうちに絶叫アトラクションを攻めよう。",

        "afternoon":
        "混雑時間帯。DPAやプライオリティパスも活用しよう。",

        "night":
        "待ち時間が落ち着くアトラクションを狙おう。パレード後がチャンス！！",

    },

    "映えハンター": {

        "description":
        "写真映えスポットを見つける才能を持つタイプ。",


        "food":
        "リトルグリーンまん、ミッキーワッフル",

        "strategy":
        "明るいうちに人物写真、夕方から夜景タイムで景色を狙おう",

        "morning":
        "明るい時間帯に人物写真をたくさん撮ろう。",

        "afternoon":
        "景色と人物を組み合わせた映え写真が撮りやすい時間帯。",

        "night":
        "ショーや夜景で最高の一枚を狙おう。",

    },

    "パーク散策家": {

        "description":
        "アトラクションだけでなく空気感そのものを楽しむタイプ。",


        "food":
        "レストランでゆっくり",

        "strategy":
        "景色を楽しみながらのんびり散策",

        "morning":
        "人が少ないうちにパークの雰囲気を楽しもう。",

        "afternoon":
        "お気に入りのエリアをゆっくり散策しよう。グリーティングもチャンス！",

        "night":
        "ライトアップされた景色を眺めながら締めくくろう。",


    }

}

TYPE_RECOMMENDATIONS = {

    "デート職人": {
        "land": {
            "attractions": [
                "美女と野獣“魔法のものがたり”",
                "ホーンテッドマンション"
            ],
            "restaurant": {
                "name": "ブルーバイユー・レストラン",
                "mood": "薄暗くロマンチックな雰囲気",
                "menu": "コース料理、肉料理、デザート",
                "recommend": "特別感のあるデートにおすすめ"
            }
        },
        "sea": {
            "attractions": [
                "ソアリン：ファンタスティック・フライト",
                "ラプンツェルのランタンフェスティバル"
            ],
            "restaurant": {
                "name": "マゼランズ",
                "mood": "大人っぽく落ち着いた雰囲気",
                "menu": "コース料理、肉料理、デザート",
                "recommend": "記念日や特別なデートにおすすめ"
            }
        }
    },

    "子連れマスター": {
        "land": {
            "attractions": [
                "イッツ・ア・スモールワールド",
                "プーさんのハニーハント"
            ],
            "restaurant": {
                "name": "クイーン・オブ・ハートのバンケットホール",
                "mood": "アリスの世界観を楽しめる明るい雰囲気",
                "menu": "ハンバーグ、オムライス、デザート",
                "recommend": "子ども連れで楽しく食事したい人におすすめ"
            }
        },
        "sea": {
            "attractions": [
                "トイ・ストーリー・マニア！",
                "アナとエルサのフローズンジャーニー"
            ],
            "restaurant": {
                "name": "ケープコッド・クックオフ",
                "mood": "カジュアルで家族でも入りやすい雰囲気",
                "menu": "バーガー、ポテト、スイーツ",
                "recommend": "子どもと一緒にゆっくり休憩したい人におすすめ"
            }
        }
    },

    "DPA課金ガチ勢": {
        "land": {
            "attractions": [
                "美女と野獣“魔法のものがたり”",
                "ベイマックスのハッピーライド"
            ],
            "restaurant": {
                "name": "プラズマ・レイズ・ダイナー",
                "mood": "回転率が高く効率重視で使いやすい雰囲気",
                "menu": "ライスボウル、チキン、デザート",
                "recommend": "モバイルオーダーを使って待ち時間を減らしたい人におすすめ"
            }
        },
        "sea": {
            "attractions": [
                "ソアリン：ファンタスティック・フライト",
                "アナとエルサのフローズンジャーニー"
            ],
            "restaurant": {
                "name": "ドックサイドダイナー",
                "mood": "気軽に利用できるカジュアルレストラン",
                "menu": "サンドウィッチ、ポテト、ドリンク",
                "recommend": "アトラクション優先で効率よく動きたい人におすすめ"
            }
        }
    },

    "食べ歩き王": {
        "land": {
            "attractions": [
                "カリブの海賊",
                "ウエスタンリバー鉄道"
            ],
            "restaurant": {
                "name": "フードワゴン巡り",
                "mood": "歩きながらいろいろ楽しめる自由なスタイル",
                "menu": "チュロス、ポップコーン、ターキーレッグ",
                "recommend": "少しずついろんな味を楽しみたい人におすすめ"
            }
        },
        "sea": {
            "attractions": [
                "ディズニーシー・トランジットスチーマーライン",
                "シンドバッド・ストーリーブック・ヴォヤッジ"
            ],
            "restaurant": {
                "name": "フードワゴン巡り",
                "mood": "港町を歩きながら食べ歩ける雰囲気",
                "menu": "ギョウザドッグ、うきわまん、チュロス",
                "recommend": "アトラクションよりフードを楽しみたい人におすすめ"
            }
        }
    },

    "ショーオタク": {
        "land": {
            "attractions": [
                "ミッキーのフィルハーマジック",
                "カントリーベア・シアター"
            ],
            "restaurant": {
                "name": "グランマ・サラのキッチン",
                "mood": "落ち着いて休憩しやすい雰囲気",
                "menu": "オムライス、洋食、デザート",
                "recommend": "ショーやパレードの合間にしっかり休みたい人におすすめ"
            }
        },
        "sea": {
            "attractions": [
                "タートル・トーク",
                "マジックランプシアター"
            ],
            "restaurant": {
                "name": "カフェ・ポルトフィーノ",
                "mood": "落ち着いて休憩しやすいレストラン",
                "menu": "パスタ、チキン、デザート",
                "recommend": "ショーの合間にしっかり食事したい人におすすめ"
            }
        }
    },

    "絶叫ジャンキー": {
        "land": {
            "attractions": [
                "ビッグサンダー・マウンテン",
                "スプラッシュ・マウンテン",
                "スター・ツアーズ：ザ・アドベンチャーズ・コンティニュー"
            ],
            "restaurant": {
                "name": "ハングリーベア・レストラン",
                "mood": "カジュアルでしっかり食べられる雰囲気",
                "menu": "カレー、チキン、セットメニュー",
                "recommend": "絶叫アトラクションの合間にがっつり食べたい人におすすめ"
            }
        },
        "sea": {
            "attractions": [
                "タワー・オブ・テラー",
                "センター・オブ・ジ・アース",
                "レイジングスピリッツ"
            ],
            "restaurant": {
                "name": "ユカタン・ベースキャンプ・グリル",
                "mood": "カジュアルでしっかり食べられる雰囲気",
                "menu": "ライスボウル、肉料理、セットメニュー",
                "recommend": "アトラクションの合間にがっつり食べたい人におすすめ"
            }
        }
    },

    "映えハンター": {
        "land": {
            "attractions": [
                "シンデレラのフェアリーテイル・ホール",
                "美女と野獣“魔法のものがたり”"
            ],
            "restaurant": {
                "name": "センターストリート・コーヒーハウス",
                "mood": "レトロで写真に残しやすい雰囲気",
                "menu": "洋食、デザート、ドリンク",
                "recommend": "写真も食事も楽しみたい人におすすめ"
            }
        },
        "sea": {
            "attractions": [
                "ラプンツェルのランタンフェスティバル",
                "ヴェネツィアン・ゴンドラ"
            ],
            "restaurant": {
                "name": "リストランテ・ディ・カナレット",
                "mood": "運河沿いで写真映えするおしゃれな雰囲気",
                "menu": "パスタ、ピザ、デザート",
                "recommend": "写真も食事も楽しみたい人におすすめ"
            }
        }
    },

    "パーク散策家": {
        "land": {
            "attractions": [
                "蒸気船マークトウェイン号",
                "オムニバス"
            ],
            "restaurant": {
                "name": "れすとらん北齋",
                "mood": "落ち着いて休める和食レストラン",
                "menu": "和食、丼、デザート",
                "recommend": "ゆっくり休みながらパークを楽しみたい人におすすめ"
            }
        },
        "sea": {
            "attractions": [
                "ヴェネツィアン・ゴンドラ",
                "ディズニーシー・トランジットスチーマーライン"
            ],
            "restaurant": {
                "name": "テディ・ルーズヴェルト・ラウンジ",
                "mood": "落ち着いた大人っぽいラウンジ",
                "menu": "サンドウィッチ、デザート、ドリンク",
                "recommend": "ゆっくり休みながらパークの雰囲気を楽しみたい人におすすめ"
            }
        }
    }

}

TYPE_PREFERENCE = {

    "デート職人": [
        "映え",
        "デート"
    ],

    "映えハンター": [
        "映え"
    ],

    "絶叫ジャンキー": [
        "絶叫"
    ],

    "食べ歩き王": [
        "フード"
    ],

    "子連れマスター": [
        "ファミリー"
    ],

    "ショーオタク": [
        "ショー"
    ],

    "DPA課金ガチ勢": [
        "絶叫",
        "映え"
    ],

    "パーク散策家": [
        "散策"
    ]

}
TYPE_BONUS = {

    "絶叫ジャンキー": {
        "thrill": 20
    },

    "映えハンター": {
        "映え": 50
    },

    "デート職人": {
        "デート": 50,
        "映え": 30
    },

    "子連れマスター": {
        "ファミリー": 50
    },

    "DPA課金ガチ勢": {
        "thrill": 15
    }

}

TYPE_ICONS = {

    "デート職人": "date.png",
    "子連れマスター": "family.png",
    "DPA課金ガチ勢": "dpa.png",
    "食べ歩き王": "food.png",
    "ショーオタク": "show.png",
    "絶叫ジャンキー": "thrill.png",
    "映えハンター": "photo.png",
    "パーク散策家": "walk.png"

}

TYPE_COLORS = {

    "デート職人": "date",

    "子連れマスター": "family",

    "DPA課金ガチ勢": "dpa",

    "食べ歩き王": "food",

    "ショーオタク": "show",

    "絶叫ジャンキー": "thrill",

    "映えハンター": "photo",

    "パーク散策家": "walk"

}
# =====================
# TOPページ
# =====================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# =====================
# 質問ページ
# =====================

@app.route("/question")
def question():

    return render_template(
        "question.html"
    )

@app.route("/question_detail", methods=["POST"])
def question_detail():

    park = request.form.get("park")

    if park == "land":

        attractions = LAND_ATTRACTIONS

    else:

        attractions = SEA_ATTRACTIONS

    sorted_attractions = sorted(
    attractions.keys()
)

    return render_template(
        "question_detail.html",
        park=park,
        attractions=sorted_attractions
    )


# =====================
# 診断結果
# =====================

@app.route(
    "/result",
    methods=["POST"]
)
def result():

    park = request.form.get(
        "park"
    )

    budget_input = request.form.get(
        "budget"
    )

    who = request.form.get(
        "who"
    )

    priority = request.form.get(
        "priority"
    )

    # ------------------
    # 未入力対策
    # ------------------

    if not all(
        [
            park,
            budget_input,
            who,
            priority
        ]
    ):

        return "未入力があります"


    budget = int(
        budget_input
    )


    # =====================
    # スコア
    # =====================

    scores = {

        "デート職人": 0,

        "子連れマスター": 0,

        "DPA課金ガチ勢": 0,

        "食べ歩き王": 0,

        "ショーオタク": 0,

        "絶叫ジャンキー": 0,

        "映えハンター": 0,

        "パーク散策家": 0

    }


    # =====================
    # 誰と行く？
    # =====================

    if who == "couple":

        scores["デート職人"] += 5
        scores["映えハンター"] += 2

    elif who == "family":

        scores["子連れマスター"] += 5
        scores["ショーオタク"] += 2

    elif who == "friend":

        scores["絶叫ジャンキー"] += 3
        scores["食べ歩き王"] += 2

    elif who == "solo":

        scores["パーク散策家"] += 5


    # =====================
    # 重視すること
    # =====================

    if priority == "thrill":

        scores["絶叫ジャンキー"] += 5
        scores["DPA課金ガチ勢"] += 2

    elif priority == "food":

        scores["食べ歩き王"] += 5

    elif priority == "photo":

        scores["映えハンター"] += 5
        scores["デート職人"] += 2

    elif priority == "show":

        scores["ショーオタク"] += 5

    elif priority == "relax":

        scores["パーク散策家"] += 5


    # =====================
    # 予算
    # =====================

    if budget >= 25000:

        scores["DPA課金ガチ勢"] += 5

    elif budget >= 15000:

        scores["デート職人"] += 1
        scores["食べ歩き王"] += 1

    else:

        scores["パーク散策家"] += 2


    # =====================
    # ランド or シー
    # =====================

    if park == "sea":

        scores["デート職人"] += 1
        scores["映えハンター"] += 1

    elif park == "land":

        scores["子連れマスター"] += 1

 

    # =====================
    # 最終診断
    # =====================

    result_type = max(
        scores,
        key=scores.get
    )

    result_data = results[result_type]
    recommend_data = TYPE_RECOMMENDATIONS[result_type][park]

    # =====================
    # アトラクション取得
    # =====================

    ride1 = request.form.get("ride1")
    ride2 = request.form.get("ride2")
    ride3 = request.form.get("ride3")

    recommended_order = []

    if ride1:

        rides = []

        for ride_name, wait_name in [

            (ride1, "wait1"),
            (ride2, "wait2"),
            (ride3, "wait3")

        ]:

            if ride_name:

                wait = int(
                    request.form.get(
                        wait_name,
                        0
                    )
                )

                attraction_data = ATTRACTIONS[
                    ride_name
                ]

                category = attraction_data[
                    "category"
                ]

                thrill = attraction_data[
                    "thrill"
                ]

            if ride_name:

                wait = int(
                    request.form.get(
                        wait_name,
                        0
                    )
                )

                attraction_data = ATTRACTIONS[
                    ride_name
                ]

                # 基本点：待ち時間が短いほど高い
                score = 200

                score -= wait * 0.5

                score += attraction_data["popularity"] * 10

                # ------------------
                # タイプ別補正
                # ------------------

                if result_type == "デート職人":

                    score += attraction_data["date"] * 20

                elif result_type == "映えハンター":

                    score += attraction_data["photo"] * 20

                elif result_type == "子連れマスター":

                    score += attraction_data["family"] * 20

                elif result_type == "絶叫ジャンキー":

                    score += attraction_data["thrill"] * 20

                elif result_type == "DPA課金ガチ勢":

                    score += attraction_data["thrill"] * 15
                    score += attraction_data["photo"] * 5

                elif result_type == "パーク散策家":

                    score += attraction_data["photo"] * 10
                    score += attraction_data["family"] * 5

                elif result_type == "食べ歩き王":

                    score += 10

                elif result_type == "ショーオタク":

                    score += 10

                rides.append({

                    "name": ride_name,

                    "wait": wait,

                    "score": score,

                })

        recommended_order = sorted(

            rides,

            key=lambda x: x["score"],

            reverse=True

        )

    # =====================
    # 現在時刻取得
    # =====================

    current_hour = datetime.now().hour

    if current_hour < 12:

        time_message = result_data["morning"]

    elif current_hour < 17:

        time_message = result_data["afternoon"]

    elif current_hour < 22:

        time_message = result_data["night"]

    else:

        time_message = (
            "閉園時間です！またのご来園をお待ちしております。"
        )

    # =====================
    # 結果表示
    # =====================

    return render_template(

        "result.html",

        result_type=result_type,

        description=result_data["description"],

        attractions=recommend_data["attractions"],

        food=result_data["food"],

        strategy=result_data["strategy"],

        current_hour=current_hour,

        time_message=time_message,

        recommended_order=recommended_order,

        attraction_urls=ATTRACTION_URLS,
        restaurant=recommend_data["restaurant"],

        restaurant_urls=RESTAURANT_URLS,

        type_icon=TYPE_ICONS[result_type],

        hero_class=TYPE_COLORS[result_type],


    )

# =====================
# 起動
# =====================

if __name__ == "__main__":

    app.run(
        debug=True
    )