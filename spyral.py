import turtle as tu
foo = tu.Turtle()
foo.left(0)
foo.speed(1000)
foo.color("red")
foo.fillcolor("violet")
foo.shape("circle")
foo.shapesize(0.1, 0.1, 0.1)
#recursion
def draw(l):
    if(l<0.001):
        return
    else:
        foo.forward(l)
        foo.left(62)
        draw(l/0.99)
        foo.right(70)
        draw(l/0.99)
        foo.left(62)
        foo.backward(l)


draw(100)
foo.home()
