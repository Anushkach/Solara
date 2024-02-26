import solara
@solara.component
def Page():
    solara.ProgressLinear(value=True) # indeterminate
    solara.ProgressLinear(value=30,color="purple") # precentage progress
    solara.ProgressLinear(value=False) # Hidden, but space remian in layout

    solara.ProgressLinear(value=70,
                          color='green',
                          style={"width":"600px",
                                 "height":"20px",
                                 "background-color":"orange",
                                 "border-radius":"5px"},
                          classes=["class1","class2","class3"])
    
    solara.ProgressLinear(value=True,
                          color='green',
                          style={"width":"2000px",
                                "height":"20px",
                                "background-color":"black",
                                "border-radius":"10px"})