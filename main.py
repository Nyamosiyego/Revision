import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


ctx.rectangle(150, 100, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

ctx.rectangle(300, 100, 100, 240)
ctx.set_source_rgb(0, 0, 1)
ctx.fill()

ctx.rectangle(450, 100, 200, 200)
ctx.set_source_rgb(1, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(5)
ctx.stroke()




surface.write_to_png("rectangle.jpg")