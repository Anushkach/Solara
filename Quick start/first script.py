import solara
# Declare Reactive variables at the top level. Components use these variables
# Will be reexecuted when their values change
sentence=solara.reactive("Solara meke our team more productive")
word_limit=solara.reactive(10)

@solara.component
def Page():
    # calculate word_count within component to ensure re-execution if the reactive variable changes.
    word_count=len(sentence.value.split())

    solara.SliderInt("word Limit",value=word_limit,min=2,max=20,step=1)
    solara.InputText(label="Your sentence", value=sentence,continuous_update=True)

    # display message based on the current word count and the word limit
    if word_count>=int(word_limit.value):
        solara.Error(f"With {word_count} words, you have exceed the word limit of {word_limit.value}.",icon=True)
    elif word_count>=int(0.8*int(word_limit.value)):
        solara.Warning(f"with {word_count} words, you are close to the word limit of {word_limit.value}.",icon=True)
    else:
        solara.Success(f"Great short story with {word_count} words!",icon=True)



