import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa=Kassapaate()

    def test_luotu_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_kateisnosto_riittaa(self):
        assert self.kassa.syo_edullisesti_kateisella(240)==0
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullinen_kateisnosto_ei_riita(self):
        assert self.kassa.syo_edullisesti_kateisella(200)==200
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_maukas_kateisnosto_riittaa(self):
        assert self.kassa.syo_maukkaasti_kateisella(400)==0
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukas_kateisnosto_ei_riita(self):
        assert self.kassa.syo_maukkaasti_kateisella(200)==200
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_edullinen_korttiosto_riittaa(self):
        kortti=Maksukortti(240)
        assert self.kassa.syo_edullisesti_kortilla(kortti)==True
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullinen_korttiosto_ei_riita(self):
        kortti=Maksukortti(200)
        assert self.kassa.syo_edullisesti_kortilla(kortti)==False
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_maukas_korttiosto_riittaa(self):
        kortti=Maksukortti(400)
        assert self.kassa.syo_maukkaasti_kortilla(kortti)==True
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukas_korttiosto_ei_riita(self):
        kortti=Maksukortti(200)
        assert self.kassa.syo_maukkaasti_kortilla(kortti)==False
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_rahan_lataus_toimii(self):
        kortti=Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)