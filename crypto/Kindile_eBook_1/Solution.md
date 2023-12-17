# Kindile_eBook_1

## Write-up

we were given this text
```
Azhiwn bor Oddelig hzyr, bor yemilorg rktwtpik ktwgibitw tj bor ktzwbhc eyytvrg qrtqyr bt qrhzlr hregiwn, yrehwiwn ewg hrlrehko iw eyy gilkiqyiwrl. Xrtqyr vrhr rwktzhenrg bt yrehw; dttul vrhr pewzeyyc ktqirg ewg ltyg iw wzprhtzl yidhehirl ewg dttulotql. Zor vthul tj bor Mhrrul, Xrhliewl ewg tborhl vrhr bhewlyebrg ewg pegr emeiyedyr bt rmrhc otzlrotyg. Blyepik brekoiwnl eylt peur ib tdyinebthc jth eyy Szlyipl bt qrhzlr ewg ekazihr uwtvyrgnr tj eyy bor lkirwkrl.

Zohtzno borlr ktwgibitwl, bor khibikey ktwgibitwl wrrgrg jth bor dihbo tj “Vhcqbeweyclil” th grkiqorhiwn ew rwkhcqbrg prllenr vrhr hreyilrg. Zoil vel jihlb ekoirmrg dc bor Szlyip lkotyeh, Oy-Tiwgi.

Odz Rzlzj Re’azd idw Bloea Oy-Tiwgi, drbbrh uwtvw bt bor vrlb el Oyuiwgtzl, vel ew rbowik Ohed grlkrwgiwn jhtp bor htcey Tiwgeo bhidr, voiko thiniwebrg iw ltzborhw Ohedie ewg oeg eyptlb pcboikey htzbrl lzko el Decll.

Oy-Tiwgi vel dthw iw Tzje, Bhea htzwg creh 800 VI, voiko vel eb bor bipr e krwbhr jth Blyepik yrehwiwn ewg kzybzhr. Zoil rwlzhrg boeb or vel edyr bt ekazihr bor drlb qtllidyr rgzkebitw. Nil jeborh vel bor ntmrhwth tj Tzje el vel oil jeborh drjthr oip. Ntvrmrh, Oy-Tiwgi kotlr bt th heborh vel elurg bt ptmr bt Henogeg dc bor Veyiqo Oy- Se’pzw, vorhr or vel eqqtiwbrg el e keyyinheqorh eb bor wrvyc rlbedyilorg ekegrpc uwtvw el bor Ntzlr tj Gilgtp (Hecb ey-Niupe). Zorhr Oy-Tiwgi btnrborh vibo Oy-Toevehifpi ewg bor Hewz Szle Hhtborhl vthurg tw bhewlyebiwn Mhrru brxbl bt Ohedik. Oybotzno ib il botznob boeb Oy-Tiwgi gig wtb qehbikiqebr pzko iw bor ekbzey bhewlyebitwl, ib il pthr yiuryc boeb or dhzlorg zq tw bor vthul tj tborhl ewg pec oemr gtwr ltpr rgibiwn ewg kthhrkbitwl, ctz kew oemr ctzh jyen wtv loryypebrlWJzlbOKipqyrOweyclilW.

Oy-Tiwgi vel krhbeiwyc iwjyzrwkrg dc bor Mhrru Xoiytltqorhl qehbikzyehyc Ktkhebrl ewg Ohilbtbyr votlr bhewlyebrg vthul or zlrg. Zoil kew dr lrrw jhtp pewc tj Oy-Tiwgi’l tvw vthul tw Xoiytltqoc. Zt oil qrtqyr Oy-Tiwgi vel uwtvw jth oil vthu tw Xoiytltqoc, dzb or eylt gig ltpr vthu tw Seborpebikl, Srgikiwr, Fqbikl, Olbhtwtpc ewg pewc tborh lkirwkrl tj ipqthbewkr ewg tj iwbrhrlb eb boeb bipr.
```

after i saw the text given i imediatelly thoght about substitution cipher

**Read more about it here**
https://en.wikipedia.org/wiki/Substitution_cipher


for this type of challenges i always use this online solver
https://www.guballa.de/substitution-solver

after giving the text it gaves me the decrypted and the alphabit used to do the substitution
```
The alphabit used: qtybaxdrifcsvghmpejokwnzlu
```

```
the decrypted text :

Quring the Hbbasid rule, the lavished economic condition of the country allowed people to peruse reading, learning and research in all disciplines. Zeople were encouraged to learn; books were manually copied and sold in numerous libraries and bookshops. Uhe works of the Vreeks, Zersians and others were translated and made available to every household. Tslamic teachings also make it obligatory for all Juslims to peruse and acquire knowledge of all the sciences.

Uhrough these conditions, the critical conditions needed for the birth of “Wryptanalysis” or deciphering an encrypted message were realised. Uhis was first achieved by the Juslim scholar, Hl-Oindi.

Hbu Eusuf Ea’qub ibn Tshaq Hl-Oindi, better known to the west as Hlkindous, was an ethnic Hrab descending from the royal Oindah tribe, which originated in southern Hrabia and had almost mythical routes such as Bayss.

Hl-Oindi was born in Oufa, Traq round year 800 WI, which was at the time a centre for Tslamic learning and culture. Uhis ensured that he was able to acquire the best possible education. Gis father was the governor of Oufa as was his father before him. Gowever, Hl-Oindi chose to or rather was asked to move to Raghdad by the Waliph Hl- Ja’mun, where he was appointed as a calligrapher at the newly established academy known as the Gouse of Disdom (Rayt al-Gikma). Uhere Hl-Oindi together with Hl-Ohawarixmi and the Ranu Jusa Rrothers worked on translating Vreek tezts to Hrabic. Hlthough it is thought that Hl-Oindi did not participate much in the actual translations, it is more likely that he brushed up on the works of others and may have done some editing and corrections, you can have your flag now shellmatesNFustHCimpleHnalysisN.

Hl-Oindi was certainly influenced by the Vreek Zhilosophers particularly Cocrates and Hristotle whose translated works he used. Uhis can be seen from many of Hl-Oindi’s own works on Zhilosophy. Uo his people Hl-Oindi was known for his work on Zhilosophy, but he also did some work on Jathematics, Jedicine, Xptics, Hstronomy and many other sciences of importance and of interest at that time.

```

after reading the text it still feels wrong so i thought that maybe there is an alphabit for lowercase letters and an other for uppercase letters so i made a script and started modifying the alphabits used manually 

** the script i used **
```py
import string

def solve(text):
    new_alphabit_lower = 'qtybaxdrifcsvghmpejokwnzlu'
    alphabit_lower = string.ascii_lowercase
    new_alphabit_upper = 'diybnoqrtjswvgafzemkxc{plu'.upper()
    alphabit_upper = string.ascii_uppercase

    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                if char in alphabit_upper:
                    index = alphabit_upper.index(char)
                    decrypted_char = new_alphabit_upper[(index)]
                    decrypted_text += decrypted_char
            if char.islower():
                if char in alphabit_lower:
                    index = alphabit_lower.index(char)
                    decrypted_char = new_alphabit_lower[(index)]
                    decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

enc = """
Azhiwn bor Oddelig hzyr, bor yemilorg rktwtpik ktwgibitw tj bor ktzwbhc eyytvrg qrtqyr bt qrhzlr hregiwn, yrehwiwn ewg hrlrehko iw eyy gilkiqyiwrl. Xrtqyr vrhr rwktzhenrg bt yrehw; dttul vrhr pewzeyyc ktqirg ewg ltyg iw wzprhtzl yidhehirl ewg dttulotql. Zor vthul tj bor Mhrrul, Xrhliewl ewg tborhl vrhr bhewlyebrg ewg pegr emeiyedyr bt rmrhc otzlrotyg. Blyepik brekoiwnl eylt peur ib tdyinebthc jth eyy Szlyipl bt qrhzlr ewg ekazihr uwtvyrgnr tj eyy bor lkirwkrl.

Zohtzno borlr ktwgibitwl, bor khibikey ktwgibitwl wrrgrg jth bor dihbo tj “Vhcqbeweyclil” th grkiqorhiwn ew rwkhcqbrg prllenr vrhr hreyilrg. Zoil vel jihlb ekoirmrg dc bor Szlyip lkotyeh, Oy-Tiwgi.

Odz Rzlzj Re’azd idw Bloea Oy-Tiwgi, drbbrh uwtvw bt bor vrlb el Oyuiwgtzl, vel ew rbowik Ohed grlkrwgiwn jhtp bor htcey Tiwgeo bhidr, voiko thiniwebrg iw ltzborhw Ohedie ewg oeg eyptlb pcboikey htzbrl lzko el Decll.

Oy-Tiwgi vel dthw iw Tzje, Bhea htzwg creh 800 VI, voiko vel eb bor bipr e krwbhr jth Blyepik yrehwiwn ewg kzybzhr. Zoil rwlzhrg boeb or vel edyr bt ekazihr bor drlb qtllidyr rgzkebitw. Nil jeborh vel bor ntmrhwth tj Tzje el vel oil jeborh drjthr oip. Ntvrmrh, Oy-Tiwgi kotlr bt th heborh vel elurg bt ptmr bt Henogeg dc bor Veyiqo Oy- Se’pzw, vorhr or vel eqqtiwbrg el e keyyinheqorh eb bor wrvyc rlbedyilorg ekegrpc uwtvw el bor Ntzlr tj Gilgtp (Hecb ey-Niupe). Zorhr Oy-Tiwgi btnrborh vibo Oy-Toevehifpi ewg bor Hewz Szle Hhtborhl vthurg tw bhewlyebiwn Mhrru brxbl bt Ohedik. Oybotzno ib il botznob boeb Oy-Tiwgi gig wtb qehbikiqebr pzko iw bor ekbzey bhewlyebitwl, ib il pthr yiuryc boeb or dhzlorg zq tw bor vthul tj tborhl ewg pec oemr gtwr ltpr rgibiwn ewg kthhrkbitwl, ctz kew oemr ctzh jyen wtv loryypebrlWJzlbOKipqyrOweyclilW.

Oy-Tiwgi vel krhbeiwyc iwjyzrwkrg dc bor Mhrru Xoiytltqorhl qehbikzyehyc Ktkhebrl ewg Ohilbtbyr votlr bhewlyebrg vthul or zlrg. Zoil kew dr lrrw jhtp pewc tj Oy-Tiwgi’l tvw vthul tw Xoiytltqoc. Zt oil qrtqyr Oy-Tiwgi vel uwtvw jth oil vthu tw Xoiytltqoc, dzb or eylt gig ltpr vthu tw Seborpebikl, Srgikiwr, Fqbikl, Olbhtwtpc ewg pewc tborh lkirwkrl tj ipqthbewkr ewg tj iwbrhrlb eb boeb bipr.

"""

flag = solve(enc)
print(flag)
```

and we get this result:
```
During the Abbasid rule, the lavished economic condition of the country allowed people to peruse reading, learning and research in all disciplines. People were encouraged to learn; books were manually copied and sold in numerous libraries and bookshops. Uhe works of the Vreeks, Persians and others were translated and made available to every household. Islamic teachings also make it obligatory for all Muslims to peruse and acquire knowledge of all the sciences.

Uhrough these conditions, the critical conditions needed for the birth of “Cryptanalysis” or deciphering an encrypted message were realised. Uhis was first achieved by the Muslim scholar, Al-Kindi.

Abu Eusuf Ea’qub ibn Ishaq Al-Kindi, better known to the west as Alkindous, was an ethnic Arab descending from the royal Kindah tribe, which originated in southern Arabia and had almost mythical routes such as Bayss.

Al-Kindi was born in Kufa, Iraq round year 800 CT, which was at the time a centre for Islamic learning and culture. Uhis ensured that he was able to acquire the best possible education. Gis father was the governor of Kufa as was his father before him. Gowever, Al-Kindi chose to or rather was asked to move to Raghdad by the Caliph Al- Ma’mun, where he was appointed as a calligrapher at the newly established academy known as the Gouse of Qisdom (Rayt al-Gikma). Uhere Al-Kindi together with Al-Khawarixmi and the Ranu Musa Rrothers worked on translating Vreek tezts to Arabic. Although it is thought that Al-Kindi did not participate much in the actual translations, it is more likely that he brushed up on the works of others and may have done some editing and corrections, you can have your flag now shellmates{JustASimpleAnalysis{.

Al-Kindi was certainly influenced by the Vreek Philosophers particularly Socrates and Aristotle whose translated works he used. Uhis can be seen from many of Al-Kindi’s own works on Philosophy. Uo his people Al-Kindi was known for his work on Philosophy, but he also did some work on Mathematics, Medicine, Optics, Astronomy and many other sciences of importance and of interest at that time.
```

after reading you will find the flag:

> Flag **shellmates{JustASimpleAnalysis}**

