# ASCII Art

ASCII Art is when you use ASCII characters as a font like this:

```
   _ \          |    |                   
  |   |  |   |  __|  __ \    _ \   __ \  
  ___/   |   |  |    | | |  (   |  |   |
 _|     \__, | \__| _| |_| \___/  _|  _|
        ____/   


                  ##   ###                   
                 ##    ##                    
######  ##  ## ######  #####   #### ## ###   
 ##  ## ##  ##   ##    #   ## ##  ## ##  ##  
 ##  ## ##  ##   ##    ##  ## ##  ## ##  ##  
 #####   #####   ##    ##  ## ##  ## ##  ##  
 ##         ##    ### #### ### #### #### ###
####    #####                                                                            
```

We're not going to build a game exactly, it is more like an ASCII art generator. Here are the **User Stories** of this little program:

1. User can put in any text and output ASCII.
1. User can pick the ASCII font we want.
1. User can list out the ASCII fonts to pick the one we want.

In this tutorial you will learn how to:

1. Make an API request using python3
1. Split text into an array using `.split()`
1. Use control flow to use boolean logic to control the outcome of programs
1. Refactor code into functions

# Getting Started

We are going to take a few steps to make a few features:

1. Send a request to the [ASCII API](http://artii.herokuapp.com)
1. Get text input from the user
1. Get font choice from user
1. See all possible font choices

But to get started we have to first just make our program's root file `asciiart.py`

```bash
$ cd cli-games
$ touch asciiart.py
```

And now open in Atom. (Hint: look back at other chapters if you can't remember how.)

# Sending a GET HTTP Request

We're not going to get too deep into web standards, for this tutorial you are just going to make **GET requests** to an API, which means you are going to read data from a web endpoint in the internet. You won't create, update, or delete any data.

To make a request to a url using python we can use an extremely popular module called `requests`.

Let's import this and make a request in our program:

```py
# cli-games/asciiart.py
import requests

r = requests.get('http://artii.herokuapp.com/make?text=Awesomesauce')
print(r.text)
```

When you run this what do you get? (Hint: `$ python3 asciiart.py`)

At first you probably get an error that warns you that the module `requests` is not actually loaded yet. So let's install this module. In order to install this, we'll need to first install a tool for installing python3 modules called **pip3**.

You can get pip3 very easily by running:

```
$ python3 get-pip.py
```

Now that you have pip3 installed, let's use it to install `requests`

```
$ pip3 install requests
```

Ok now you have the request module so you can run your program again. Good use of interpreting errors!

You should see our ASCII output of the text "Awesomesauce" we are passing in as the `text` parameter to our url.

# Getting Input from the User

Let's use our `input` built-in function to get an input from the user at the command line. Then we'll use the **f-string** pattern to interpolate the text.

Update `asciiart.py` to the following:

```py
import requests

text = input('ASCII Art Text > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
print(r.text)
```

Ok now run that. It ought to work! Great.

In the interest of exploring errors more. Try removing something from the above text, like a `}` or a `)` and see what happens. Read the error you get carefully, and imagine how you would react when you encounter an error like this in the wild. Many errors are just caused by misspelling variables and forgetting commas and other syntax!

# Adding a Font

If you visit [http://artii.herokuapp.com](http://artii.herokuapp.com) you can see that we can also add a `font` url parameter.

Let's add that! Update `asciiart.py` to the following:

```py
import requests

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
print(r.text)
```

Some fonts to test with include "peaks", "shadow", and "thick".

# Display Three Random Fonts

To get all the fonts, you can navigate to [http://artii.herokuapp.com/fonts_list](http://artii.herokuapp.com/fonts_list). This list of fonts is so long that it would be hard to list it all out for people to see in our command lines. Instead we could make it easy for our users and just grab three random fonts and output all three results.

First we can get all the fonts:

```py
data = requests.get('http://artii.herokuapp.com/fonts_list')
print(data)
```

Next we can turn this list of fonts into an array data structure using the `.split()` and split them up by `\n` the invisible new line character.

Use split to break up the array:

```py
fontsArray = data.text.split('\n')
```

Then we can get a random font with the `random.choice()` function.

Update `asciiart.py` to the following:

```py
# cli-games/asciiart.py
import requests
import random

data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')
font = random.choice(fontsArray)
print(font)

text = input('ASCII Art Text > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
print(r.text)
```

Now we should be able to see our text displayed in a random font!

Now we can make 3 requests using a for loop. Here's how we would do that:

```py
...

data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')

for i in range(3):
  font = random.choice(fontsArray)
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
  print("Font:", font)
  print(r.text)
```

# Making Options

It's always harder to make software have a lot of options and configurability, so we're going to give ourselves the challenge of making things a little more complex.

Let's let people have three options with font:

1. Get the default font
1. Set a single font
1. Get 3 random fonts

First if there is no font specified we make the request with no font. Update your code to the following:

```py
# cli-games/asciiart.py
import requests
import random

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

if font == "":
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
  print("Font: default")
  print(r.text)
```

Otherwise if the font is defined at all use the font:

```py
if font:
  font = font
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
  print("Font:", font)
  print(r.text)
```

Finally we need to add our random 3 fonts:

```py
if font == "random":
  data = requests.get('http://artii.herokuapp.com/fonts_list')
  fontsArray = data.text.split('\n')

  for i in range(3):
      font = random.choice(fontsArray)
      r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
      print("Font:", font)
      print(r.text)
```

Consider your Boolean Logic carefully here. What order do these need to come in?

If we do it in the wrong order, we'll get the wrong logic and we might see errors.

Using the code snippets above, arrange them in the proper control flow order.

Once you've tried, check against the solution below:

<details>
<summary>Solution</summary>
<br>
1. `if` Check if font == "random"
2. `elif` Check if font is anything (besides "random")
3. `elif` Check if font is blank
</details>

# Refactoring Code Using Functions

One of the most important principles in **Code Craftsmanship** or **Code Quality** is called **DRY** code. DRY stands for **DO NOT REPEAT YOURSELF**. Code that repeats means if you want to make changes you have to change multiple spots in the code.

Our code currently repeats itself in one place in particular: calling the API. So let's pull that out into a function. Changing your code to be more DRY is called **refactoring**. So let's refactor our project a little bit by defining a function called `getAsciiArt`.

We'll use the `def` keyword to define a function. We'll want to define this function above anywhere where it is called.

Place this near the top of `asciiart.py`:

```py
def getAsciiArt(text, font):
    r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    print("Font:", font)
    print(r.text)
```

Now with this we can use this function to replace each time we called those same lines in our program like this:

```py
  for i in range(3):
      font = random.choice(fontsArray)
      getAsciiArt(text, font)
```

Try to replace the code with the function in all other places. Now your code is DRY!

# In Review: You Can ...

So in review here's what you did and what you can do now:

1. You can make an API request using python3
1. You can split text into an array using `.split()`
1. You can use control flow to use boolean logic to control the outcome of programs
1. You can refactor code into functions

**Congrats on finishing the CLI Games Tutorial!** 
