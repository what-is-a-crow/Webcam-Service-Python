import pygame
from pygame import camera
from pygame import image
from pygame import font
import time
import datetime
from threading import Thread

# todo: get the (real) system timer to work!
class FakeTimer(Thread):
	def __init__(self, action):
		self.action = action
	def start(self):
		while True:
			self.action()
			time.sleep(20)

def capture():
	print 'Capturing current image...'
	surface = cam.get_image()
	if surface is None:
		print 'Could not obtain image from webcam.'
		return
	print 'Saving current image...'
	renderText(surface)
	image.save(surface, '/var/www/webcam.jpg')

def renderText(image):
	dateFont = font.SysFont('arial', 20, bold=True, italic=False)
	addressFont = font.SysFont('arial', 14, bold=False, italic=True)

	date = datetime.datetime.now().strftime('%b %d, %Y %I:%M %p')
	srfDate = dateFont.render(date, True, (255,255,255))
	srfDateShadow = dateFont.render(date, True, (0,0,0))

	address = 'Boulevard East, Weehawken, NJ'
	srfAddress = addressFont.render(address, True, (255,255,255))
	srfAddressShadow = addressFont.render(address, True, (0,0,0))

	image.blit(srfDateShadow, (11, 11))
	image.blit(srfDate, (10,10))
	image.blit(srfAddressShadow, (11, 36))
	image.blit(srfAddress, (10, 35))

print 'Starting WebCam service.'
pygame.init()
camera.init()
cameraNames = camera.list_cameras()
print 'Camera list: {}'.format(cameraNames)

cam = camera.Camera(cameraNames[1]) # todo: make index configurable / pass in name
cam.start()

timer = FakeTimer(capture)
timer.start()