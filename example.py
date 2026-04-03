import stuge


def setup():
    return 100


def loop(state):
    for k in stuge.keypresses():
        if k == "q":
            stuge.quit()
        if k == "Up":
            state += 10
    stuge.turtle.fd(state)
    return state


stuge.run(setup, loop)
