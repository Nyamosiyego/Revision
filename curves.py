import math

import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.arc(300, 200, 150, 0, math.pi * 2)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.fill()

ctx.move_to(300, 50)
ctx.line_to(300, 350)
ctx.set_source_rgb(0, 1, 0)
ctx.set_line_width(10)
ctx.stroke()

ctx.move_to(150, 200)
ctx.line_to(450, 200)
ctx.set_source_rgb(0, 1, 0)
ctx.set_line_width(10)
ctx.stroke()


ctx.arc(300, 200, 150, 0, math.pi/2)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()



surface.write_to_png("curves.jpg")
