f= input("enter the number")
x = input("enter the name")
z = input("enter the email")
data = f"""BEGIN:VCARD
VERSION:3.0
FN:{x}
TEL;TYPE=CELL:{f}
EMAIL:{z}
END:VCARD
"""
r = open("c1.vcf","w")
r.write(data)
r.close()
