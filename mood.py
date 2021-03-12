import svg
import random

print(dir(svg))
def my_art():


    draw_all_shapes()
def draw_all_shapes():
 
   s = svg.SVG()

   s.create(670,430)

   s.fill("#00022e")

   for star in range(0, 800):
        x = random.randrange(0, 800)
        y = random.randrange(0, 600)
    	
        s.rectangle(1,1,x,y,"silver","silver",1,1,1) 

   s.text(80, 178, "script", 50,"#FFFF00", "#000000", "weet")
   s.text(50, 240, "script", 160,"#DC143C", "#000000", "Sensation...")

   
   s.finalize()


   try:
        s.save("assessment.svg")
   except IOError as ioe:
        print(ioe)

   print(s)


my_art()