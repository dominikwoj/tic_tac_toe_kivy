1. Main info about kivy
> https://www.youtube.com/watch?v=l8Imtec4ReQ

2. on_press action on butto with parameter
> https://stackoverflow.com/questions/39809206/kivy-python-passing-parameters-to-fuction-with-button-click

> Button(on_press=self.my_function)

This is passing the function as an argument.

> Button(on_press=self.my_function('btn1'))

This is calling the function and passing the returned value as the argument to on_press. Since the returned value is None, you get your error.

You instead need to pass a new function that calls your normal function and automatically passes the argument. In general, it's convenient to use functools.partial:

> from functools import partial
> Button(on_press=partial(self.my_function, 'btn1'))

You can also use a lambda function:

> Button(on_press=lambda *args: self.my_function('btn1', *args))