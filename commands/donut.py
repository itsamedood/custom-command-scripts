from math import sin, cos
import os


def donut():
	""" Mmmmm... Donut... """

	donutChars = ".,-~:;=!*#$@"
	a, b, height, width = 0, 0, 24, 80
	clear = "cls"

	if os.name == "posix":
		clear = "clear"

	os.system(clear)

	try:
		while True:
			z: list[float] = [0 for _ in range(4 * height * width)]
			screen = [' ' for _ in range(height * width)]
			j = 0
			while j < 6.28:
				j += 0.07
				i = 0
				while i < 6.28:
					i += 0.02
					sinA = sin(a)
					cosA = cos(a)
					cosB = cos(b)
					sinB = sin(b)
					sini = sin(i)
					cosi = cos(i)
					cosj = cos(j)
					sinj = sin(j)
					cosj2 = cosj + 2
					mess = 1 / (sini * cosj2 * sinA + sinj * cosA + 5)
					t = sini * cosj2 * cosA - sinj * sinA
					x = int(40 + 30 * mess * (cosi * cosj2 * cosB - t * sinB))
					y = int(11 + 15 * mess * (cosi * cosj2 * sinB + t * cosB))
					o = int(x + width * y)
					N = int(8 * ((sinj * sinA - sini * cosj * cosA) * cosB - sini * cosj * sinA - sinj * cosA - cosi  * cosj * sinB))
					if 0 < y < height and 0 < x < width and z[o] < mess:
						z[o] = mess
						screen[o] = donutChars[N if N > 0 else 0]
			os.system(clear)
			for index, char in enumerate(screen):
				if index % width == 0: print()
				else: print(char, end='')
			a += 0.04
			b += 0.02
	except KeyboardInterrupt: print("\n\033[1;31mKeyboard interrupted :(\033[0m")


donut()
