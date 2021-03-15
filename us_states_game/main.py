import turtle
import pandas
from on_screen_text import OnScreenText
IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)
states = pandas.read_csv("50_states.csv")
on_screen_text = OnScreenText()

game_is_on = True
guessed = 0
guessed_states = []
while game_is_on:
    screen.update()
    answer_state = screen.textinput(title=f"Guess the state name {guessed}/50", prompt="What's another state name?")
    answer_state = answer_state.title()
    if states[states.state == answer_state].empty or answer_state in guessed_states:
        continue
    guessed_states.append(answer_state)
    guessed += 1
    x_cor = states[states.state == answer_state].x
    y_cor = states[states.state == answer_state].y
    on_screen_text.write_on_screen(int(x_cor), int(y_cor), answer_state)
    if guessed == 50:
        game_is_on = False



screen.exitonclick()




