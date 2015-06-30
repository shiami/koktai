from unittest.case import TestCase


from 臺文格式正規化 import 臺文格式正規化



class 臺文格式正規化試驗(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        self.格式正規化 = 臺文格式正規化()
        self.assertEqual(
            self.格式正規化.正規化(self.原來),
            self.答案,
            self.原來)
    def test_箭頭補一字(self):
        self.原來='是鹽󸝞→󹙧。'
        self.答案='是鹽󸝞→鹽󹙧。'
    def test_箭頭補多一字(self):
        self.原來='橄󹖰欖󹏒(字音)→橄󹖮欖󹏒→橄󹓷欖󹋕(語音)。台灣市面所見多是鹽󸝞→󹙧橄󹖰→󹓷欖󹏒→󹋕，音諧：鹹󹙧矸󹖼仔<k>󸵁</k>/󹋕。'
        self.答案='橄󹖰欖󹏒(字音)→橄󹖮欖󹏒→橄󹓷欖󹋕(語音)。台灣市面所見多是鹽󸝞→鹽󹙧橄󹖰→橄󹓷欖󹏒→欖󹋕，音諧：鹹󹙧矸󹖼仔<k>󸵁</k>/󹋕。'
    def test_箭頭補三字(self):
        self.原來='胳󹕠下󸙖空(/孔)󹦰→󹛚󹳀󹏥。'
        self.答案='胳󹕠下󸙖空(/孔)󹦰→胳󹛚下󹳀空(/孔)󹏥。'
    def test_注音括號提掉(self):
        self.原來='空(/孔)󹦰(/󹦰)(訛變)。'
        self.答案='空(/孔)󹦰/󹦰(訛變)。'
    def test_綜合(self):
        self.原來='胳󹕠下󸙖空(/孔)󹦰→󹛚󹳀󹏥(/󹦰)(訛變)。'
        self.答案='胳󹕠下󸙖空(/孔)󹦰→胳󹛚下󹳀空(/孔)󹏥/󹦰(訛變)。'
    def test_換做注音表的編號(self):
        # ./m3.json:"8652": "ㆤ",
        # ./k.json:"8d44": "ㆤ",
        self.原來='古󹕁早󸅇大󸽜夫󹵴職󹻂以󸛑上󺃳丌<k>󸵄</k>官󹝀(文)/󹛎(語)，所󸒭戴󸽛(文)/󸾼(語)丌<k>󸵄</k>禮󹎽帽󿱶。'
        self.答案='古󹕁早󸅇大󸽜夫󹵴職󹻂以󸛑上󺃳丌<k>󸵄</k>官󹝀(文)/󹛎(語)，所󸒭戴󸽛(文)/󸾼(語)丌󸙒禮󹎽帽󿱶。'
#     def test_無漢字一注音(self):
#         self.原來=''
#         self.答案=''
#     def test_無漢字一注音(self):
#         self.原來=''
#         self.答案=''
