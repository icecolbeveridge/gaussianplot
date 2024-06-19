from PIL import Image

S = 1000
img = Image.new("RGB", (2*S,2*S), "white")
pixels = img.load()
down = 30
for a in range(100):
    for p in range(-100,100):
        for q in range(-100, 100):
            s = p**2 + q**2
            if s == 0:
                continue
            x= S*a*(p-q)/s
            y= S*a*(p+q)/s
            if -S <x<S and -S<y<S:
                xi, yi = int(x+S), int(y+S)
                r,g,b = pixels[xi, yi]
                if r > 0:
                    try:
                        pixels[xi,yi] = r-down, g-down, b-down
                        pixels[2*S-xi,yi] = r-down, g-down, b-down
                        pixels[xi,2*S-yi] = r-down, g-down, b-down
                        pixels[2*S-xi,2*S-yi] = r-down, g-down, b-down
                    except: # if xi or yi is 0, this fails and I can't be bothered fixing it
                        pass
img.show()
