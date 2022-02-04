import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

game_over = False

while not game_over and len(guessed_states) < len(all_states):

    title = str(f"{len(guessed_states)}/{len(all_states)} States Correct")
    answer_state = screen.textinput(title=title, prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #t.write(state_data.state.item())
        t.write(answer_state)
        guessed_states.append(answer_state)

    if answer_state == "Quit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_over = True

#screen.exitonclick()

