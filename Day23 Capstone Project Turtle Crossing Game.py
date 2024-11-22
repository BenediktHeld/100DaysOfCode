import turtle
import random

# Erstelle die Screen-Instanz und setze die Fenstergröße
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Setze die Fenstergröße auf 800x600 Pixel
screen.title("Bewegende Rechtecke mit zufälligen Farben")

# Begrenzung des Spielfelds
def draw_border():
    border_turtle = turtle.Turtle()
    border_turtle.penup()
    border_turtle.goto(-310, 310)  # Obere linke Ecke
    border_turtle.pendown()
    border_turtle.pensize(3)
    border_turtle.color("black")
    for _ in range(4):
        if _ % 2 == 0:
            border_turtle.forward(620)
        else:
            border_turtle.right(90)
            border_turtle.forward(620)
            border_turtle.right(90)
    border_turtle.hideturtle()

# Zeichne das Spielfeld
draw_border()

# Funktion, um eine zufällige Farbe zu generieren
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Erstelle eine Funktion, die eine Turtle in Rechteckform am rechten Rand des Bildschirms spawnen und nach links bewegen lässt
def spawn_rectangle_turtle():
    t = turtle.Turtle()
    t.penup()
    t.shape('square')
    t.shapesize(stretch_wid=0.5, stretch_len=1)  # Breite 0.5 und Höhe 1
    t.color(random_color())
    t.goto(400, random.randint(-250, 250))  # Spawne am rechten Rand mit zufälliger y-Position
    t.setheading(180)  # Bewege nach links
    return t

# Liste, um alle Rechtecke zu verwalten
rectangle_turtles = []

# Erstelle eine Hauptturtle
player_turtle = turtle.Turtle()
player_turtle.shape('turtle')
player_turtle.penup()
player_turtle.goto(0, -300)
player_turtle.left(90)

# Funktion zur Steuerung der Player-Turtle
def init_key_bindings():
    screen.listen()
    screen.onkey(lambda: player_turtle.forward(20), "w")
    screen.onkey(lambda: player_turtle.backward(20), "s")
    screen.onkey(lambda: player_turtle.left(45), "a")
    screen.onkey(lambda: player_turtle.right(45), "d")

# Initialisiere die Tastenbindungen
init_key_bindings()

# Funktion zur Kollisionsüberprüfung
def check_collision(t1, t2):
    return t1.distance(t2) < 20  # Einfache Distanzbasierte Kollisionsabfrage

# Hauptschleife zum Erzeugen und Bewegen der Rechtecke
def main_loop():
    while True:
        if random.randint(0, 20) == 0:  # Mit gewisser Wahrscheinlichkeit ein neues Rechteck erzeugen
            rectangle_turtles.append(spawn_rectangle_turtle())

        # Bewege alle Rechtecke nach links
        for t in rectangle_turtles:
            t.forward(5)

            # Entferne Rechtecke, die aus dem Bildschirm heraus sind
            if t.xcor() < -400:
                t.hideturtle()
                rectangle_turtles.remove(t)

            # Überprüfe auf Kollision mit der Player-Turtle
            if check_collision(player_turtle, t):
                turtle_game_over()
                return

        screen.update()
        turtle.time.sleep(0.02)  # Kurze Pause für flüssige Animation

# Funktion zum Anzeigen der Game Over Nachricht
def turtle_game_over():
    game_over_turtle = turtle.Turtle()
    game_over_turtle.hideturtle()
    game_over_turtle.penup()
    game_over_turtle.goto(0, 0)
    game_over_turtle.color("red")
    game_over_turtle.write("GAME OVER", align="center", font=("Arial", 36, "bold"))

# Initialisiere den Bildschirm-Update-Modus
screen.tracer(0)

# Starte den Hauptloop
main_loop()

# Halte das Fenster offen
screen.mainloop()