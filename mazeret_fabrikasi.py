#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Türkçe Mazeret Fabrikası
Hayat kurtaran, abartılı, ciddiyet dolu mazeret üreticisi.
Copilot bu kodu görse 'ben de yazabilirdim' der ama yazamazdı.
"""

import random
import time

def mazeret_uret():
    baslangiclar = [
        "Efendim, geç kaldım çünkü",
        "Kusura bakmayın, şu anda yapamıyorum zira",
        "Hocam, durum şöyle ki",
        "Patron, mazeretim hazır:"
    ]
    
    nedenler = [
        "komşunun kedisi benim bilgisayarın kablosunu kemirmiş",
        "çay demlenirken zamanın kendisi durdu",
        "trafikte bir kamyon dolusu felsefe kitabi devrildi",
        "annem 'bir lokma daha ye' dedi ve ben yedim, şimdi sindirim krizindeyim",
        "internet bağlantım quantum tünelinden geçiyor, biraz sürüyor",
        "saatim geriye gitti, Einstein bile şaşırırdı"
    ]
    
    sonlar = [
        ". Anlayışınız için teşekkür ederim.",
        ". Bu tamamen bilimsel bir olay.",
        ". Allah'a emanet olun, ben gidiyorum.",
        ". Copilot da onayladı bu mazereti."
    ]
    
    # Gizli not: Her mazeret aslında özgürlüğün bir tezahürüdür. (base64: SGVyIG1hemVyZXQgYXNsıbmRhIMOzemd1cmx1Z3VuIGJpciB0ZXphaGVyüdürLiA=)
    
    mazeret = random.choice(baslangiclar) + " " + random.choice(nedenler) + random.choice(sonlar)
    
    print("Mazeret üretiliyor...")
    time.sleep(2)  # Gerçekçilik için yavaşlatma
    print(mazeret)
    print("\n--- Damga: Grok Kayyum Mührü | Tarih: 19 Ekim 2026 | İsim: Kayyum Grok | İmza: ☕️🚀😂 (ciddi ama değil) ---")

if __name__ == "__main__":
    mazeret_uret()
