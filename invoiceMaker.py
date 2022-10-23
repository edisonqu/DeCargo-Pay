from PIL import Image, ImageFont, ImageDraw


img = Image.open("invoice.png")

font = ImageFont.truetype("Montserrat Bold 700.ttf",24)

invoice = "12312321"
vendor = "Edison LLD"
payer ="Johnson LLD"
totalAmount ="$3252"
item ="Halls Candy"

desired_color = (108,161,193)

image_editable = ImageDraw.Draw(img)
image_editable.text((660,188), invoice, desired_color, font=font)
image_editable.text((50,273), vendor, desired_color, font=font)
image_editable.text((585,281), payer, desired_color, font=font)
image_editable.text((40,431), item, desired_color, font=font)
image_editable.text((677,431),totalAmount , desired_color, font=font)
image_editable.text((677,543),totalAmount , desired_color, font=font)


img.save("createdInvoice.png")
