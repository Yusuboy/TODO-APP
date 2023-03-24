import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapääte(unittest.TestCase):
     def test_kassapaate_initialization(self):
        kassapaate = Kassapaate()
        self.assertEqual(kassapaate.kassassa_rahaa, 100000, "rahamäärä oikea ")
        self.assertEqual(kassapaate.edulliset + kassapaate.maukkaat, 0, "myytyjen lounaiden määrä on oikea")

    
     def test_edullisen_lounaan_käteisosto(self):
        kassapaate = Kassapaate()
        maksu = 500
        vaihtoraha = kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(kassapaate.kassassa_rahaa, 100240, "Kassapäätteen rahamäärä oikea")
        self.assertEqual(kassapaate.edulliset, 1, "Edullisten lounaiden määrä oikea")
        self.assertEqual(vaihtoraha, maksu - 240, "Vaihtorahan oikea")



     def test_edullinen_ei_riittava(self):
        kassa = Kassapaate()
        maksu = 100 
        vaihtoraha = kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(vaihtoraha, 100, "Ei riittävästi käteistä")  
        self.assertEqual(kassa.kassassa_rahaa, 100000)  
        self.assertEqual(kassa.edulliset, 0) 

        
     def test_maukkaan_lounaan_käteisosto(self):
        kassapaate = Kassapaate()
        maksu = 600
        vaihtoraha = kassapaate.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(kassapaate.kassassa_rahaa, 100400, "Kassapäätteen rahamäärä väärä")
        self.assertEqual(kassapaate.maukkaat, 1, "Maukkaiden lounaiden määrä oikea")
        self.assertEqual(vaihtoraha, maksu - 400, "Vaihtorahan oikea")    


     def test_maukas_ei_riittava(self):
        kassa = Kassapaate()
        maksu = 100 
        vaihtoraha = kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(vaihtoraha, 100 , "Ei riittävästi käteistä")  
        self.assertEqual(kassa.kassassa_rahaa, 100000)  
        self.assertEqual(kassa.maukkaat, 0) 

     
     def test_syo_edullisesti_kortilla_veloitus_onnistuu(self):
        kortti = Maksukortti(1000)
        kassapaate = Kassapaate()

        asetus = kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(asetus, True, "Kate oli riittävä")
        self.assertEqual(kortti.saldo, 760)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

     def test_syo_edullisesti_kortilla_veloitus_onnistuu_määrä_kasvaa(self):
        kortti = Maksukortti(1000)
        kassapaate = Kassapaate()
        asetus = kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kassapaate.edulliset, 1, "Myytin ateria")
        

     def test_syo_edullisesti_kortilla_veloitus_epäonnistuu(self):
        kortti = Maksukortti(100)
        kassapaate = Kassapaate()

        asetus = kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(asetus, False, "Kate ei ollut riittävä")
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(kassapaate.edulliset, 0)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

     
     def test_syo_maukkaasti_kortilla_veloitus_onnistuu(self):
        kortti = Maksukortti(1000)
        kassapaate = Kassapaate()

        asetus = kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(asetus, True, "Kate oli riittävä")
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

     def test_syo_edullisesti_kortilla_veloitus_onnistuu_määrä_kasvaa(self):
        kortti = Maksukortti(1000)
        kassapaate = Kassapaate()
        asetus = kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kassapaate.edulliset, 1, "Myytiin ateria")
        


     def test_syo_maukkaasti_kortilla_veloitus_epäonnistuu(self):
        kortti = Maksukortti(100)
        kassapaate = Kassapaate()

        asetus = kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(asetus, False, "Kate ei ollut riittävä")
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(kassapaate.maukkaat, 0)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)



     def test_rahaa_ladattaessa_saldo_muuttuu(self):
        kassa = Kassapaate()
        kortti = Maksukortti(0)
        
    
        kassa.lataa_rahaa_kortille(kortti, 500)
        
     
        self.assertEqual(kortti.saldo, 500, "Kortin saldo muuttui")
        self.assertEqual(kassa.kassassa_rahaa, 100500, "Kassan saldo muuttui")
        
        
    

     def test_neg_rahaa_ladattaessa_saldo_muuttuu(self):
        kassa = Kassapaate()
        kortti = Maksukortti(500)

        kassa.lataa_rahaa_kortille(kortti, -100)

      
        self.assertEqual(kortti.saldo, 500 ,"Ei vaikutusta")
        


    


