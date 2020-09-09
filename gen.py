import qrcode

# Using readlines() 
file1 = open('list.txt', 'r') 
Lines = file1.readlines() 
  


count = 1
# Strips the newline character 
for line in Lines: 
    print("Generateing QR_Code :" +line) 
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
    qr.add_data(line)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    filename = line.strip()+".png"
    img.save("qr_codes/"+filename)
    qr=""
    img=""
