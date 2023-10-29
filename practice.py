import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1200, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


ctx.move_to(50, 350)
ctx.line_to(250, 650)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(8)
ctx.stroke()

ctx.move_to(400, 50)
ctx.line_to(600, 350)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(8)
ctx.stroke()

ctx.move_to(50, 350)
ctx.curve_to(150, 580, 450, 50, 600, 350)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()


surface.write_to_png("practice.jpg")