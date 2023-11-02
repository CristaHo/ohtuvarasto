import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_liian_paljon_ottaminen(self):
        self.varasto.lisaa_varastoon(2)
        
        self.assertAlmostEqual(self.varasto.ota_varastosta(3), 2)
        
    def test_lisaysmaara_miinusmerkkinen(self):
      
        self.assertAlmostEqual(self.varasto.lisaa_varastoon(-2), None)
    
    def test_tilavuus_miinusmerkkinen(self):
        self.varasto1 = Varasto(-2)
        self.assertAlmostEqual(self.varasto1.saldo, -2)
    
    def test_saldo_miinusmerkkinen(self):
        self.varasto2 = Varasto(10, -2)
        self.assertAlmostEqual(self.varasto2.saldo, 0)
    
    def test_lisaa_varastoon_liikaa(self):
        self.assertAlmostEqual(self.varasto.lisaa_varastoon(12), None)
    
    def test_ota_varastosta_miinusmerkkisesti(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-2), miljoona)
    
    def test_str_lause_ok(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
    
