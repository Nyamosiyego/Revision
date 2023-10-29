import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw the first triangle with only an outline
ctx.move_to(50, 60)
ctx.line_to(50, 300)
ctx.line_to(400, 308)
ctx.close_path()
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Draw the second triangle
ctx.move_to(430, 300)
ctx.line_to(420, 50)
ctx.line_to(70, 50)
ctx.close_path()

# Set the source color for filling the second triangle
ctx.set_source_rgb(1, 0, 0)

# Fill the second triangle
ctx.fill_preserve()

# Draw the outlines of both triangles
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png("polygons.jpg")
