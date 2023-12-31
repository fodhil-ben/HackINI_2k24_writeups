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

"""
the flag : shellmates{JustASimpleAnalysis}
"""