import qrcode

texto = input("Ingrese el texto para generar el código QR: ").strip()
archivo = input("Ingrese el nombre del archivo para guardar el código QR (con extensión .png): ").strip()

qr=qrcode.QRCode(box_size=10, border=5)
qr.add_data(texto)  

qr.make(fit=True)

imagen = qr.make_image(fill_color="black", back_color="white")
imagen.save(archivo)    

print(f"Código QR generado y guardado en {archivo}")