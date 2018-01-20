from flask import Flask, make_response
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

main_title = "ESPN3 / GVSN"

Arial_Black = ImageFont.truetype('fonts/Arial Black.ttf', 90)
Arial_Regular = ImageFont.truetype('fonts/Arial.ttf', 90)

@app.route('/<string:card_title>/<string:runtime>')
def imageing(card_title, runtime):
	card = Image.new('RGB', (1920,1080), color='black')
	d = ImageDraw.Draw(card)
	d.text((400,300), main_title, fill=(255,255,255), font=Arial_Black)
	d.text((400,475), card_title, fill=(255,255,255), font=Arial_Regular)
	d.text((400,575), runtime, fill=(255,255,255), font=Arial_Regular)
	
	fname = card_title.replace(' ', '-').lower()
	
	imagebuffer = BytesIO()
	card.save(imagebuffer, format='PNG')
	response = make_response(imagebuffer.getvalue())
	response.headers['Content-Type'] = 'image/png'
	response.headers['Content-Disposition'] = 'inline; filename="' + fname + '.png"'
	return response