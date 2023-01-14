# import modules
import os
import qrcode
from PIL import Image

# taking image which user wants
# in the QR code center
Logo_link = 'conta.jpg'



vcard = """
BEGIN:VCARD
VERSION:3.0
FN;CHARSET=UTF-8:Mara Travers
N;CHARSET=UTF-8:Intermpump Antriebstechnik Gmbh;Mara Traverso;;
URL:https://panni.com
URL:https://contarini.net
EMAIL:traversom@panni.com
EMAIL:mtraverso@contarini.net
TEL;TYPE=mobile:+49 175 3032097

ADR;TYPE=intl,work,postal,parcel:;;Diesel 6;Fellbach;;70736;Germany
END:VCARD
"""

vcard_old2 = '''BEGIN:VCARD

VERSION:3.0

N:Fabio;Spadavecchia

FN:Fabio Spadavecchia

ORG:Contarini Leopoldo Srl

URL:contarini.net

EMAIL:fspadavecchia@contarini.net

TEL;TYPE=voice,work,pref:+39 0545 281137

TEL;TYPE=mobile:+39 3421246431

ADR;TYPE=intl,work,postal,parcel:;;Via Fiumazzo 46;Lugo(RA);;48022;Lugo

END:VCARD'''

vcard_old3 = '''BEGIN:VCARD

VERSION:3.0

N:Fabio;Cimatti
FN:Fabio Cimatti

ORG:Contarini Leopoldo Srl

URL:contarini.net

EMAIL:fcimatti@contarini.net


TEL;TYPE=mobile:+39 3351568614

ADR;TYPE=intl,work,postal,parcel:;;Via Fiumazzo 75;Lugo(RA);;48022;Lugo

END:VCARD'''

vcard_old4 = '''BEGIN:VCARD

VERSION:3.0

N:Cesare;Pretolani

FN:Cesare Pretolani

ORG:Contarini Leopoldo Srl

URL:contarini.net

EMAIL:cpretonali@contarini.net

TEL;TYPE=mobile:+39 3405861028

ADR;TYPE=intl,work,postal,parcel:;;Via Fiumazzo 46;Lugo(RA);;48022;Lugo

END:VCARD'''

vcard_old5 = '''BEGIN:VCARD

VERSION:3.0

N:Claudio;Versari

FN:Claudio Versari

N:Contarini Leopoldo Srl

URL:contarini.net

EMAIL:cversari@contarini.net

TEL;TYPE=mobile:+39 3488229385

ADR;TYPE=intl,work,postal,parcel:;;Via Fiumazzo 46;Lugo(RA);;48022;Lugo

END:VCARD'''
logo = Image.open(Logo_link)

# taking base width
basewidth = 50

# adjust image size
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)
QRcode = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# taking url or text
# url = 'https://www.contarini.net/'

# adding URL or text to QRcode
QRcode.add_data(vcard)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'Black'

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')


# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)

#QRimg.paste(logo,pos)

# save the QR code generated
QRimg.save('mtraverso_QR.png')

print('QR code generated!')