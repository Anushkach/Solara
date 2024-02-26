import solara
@solara.component
def Page():
    solara.ProgressLinear(value=True)
    solara.ProgressLinear(value=30,color="purple") # precentage progress
    solara.ProgressLinear(value=False) # space remian in layout

    solara.ProgressLinear(value=70,
                          color='green',
                          style={"height":"20px"},
                          classes=["class1","class2","class3"])