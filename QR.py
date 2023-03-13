import qrcode as QR
img = QR.make("https://github.com/swatidaware?tab=repositories")
img.save("SWATI Github.png")