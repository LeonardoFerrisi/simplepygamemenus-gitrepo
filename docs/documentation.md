# NAME
    menu.py - SIMPLE PYGAME MENU - Leonardo Ferrisi 23'

# DESCRIPTION
    contact: ferrisil@union.edu

    A python package for simplifying the process of importing your pygame menus

    Some Rules:

        - Make the main menu first!
        - If you want to be able to switch back to the previous menu, set the main parameter in Menu() to the previous menu

# CLASSES
    builtins.object
        Button
        Menu

## Button

    class Button(builtins.object)
     |  Button(image: pygame.Surface, pos: tuple, text_input: str, font: pygame.font.Font, base_color: tuple, hovering_color: tuple)
     |
     |  A button you can click on and execute functions with
     |
     |  Methods defined here:
     |
     |  __init__(self, image: pygame.Surface, pos: tuple, text_input: str, font: pygame.font.Font, base_color: tuple, hovering_color: tuple)
     |      Create a Button object
     |
     |          Parameters:
     |              `image`      (pygame.Surface): An image to overlay the text on. Example: a rectangle
     |              `pos`                 (tuple): A tuple containing the x, y position of the button center
     |              `text_input`            (str): The text that goes on the button
     |              `font`     (pygame.font.Font): The font of the text. Use `get_font` for best functionality
     |              `base_color`            (str): The base color of button when not being interacted with
     |              `hovering_color`        (str): The hovering color of button when being interacted with
     |
     |  changeColor(self, position: tuple) -> None
     |      Given an (x,y) position, typically provided by `pygame.mouse.get_pos()`
     |      tell us if the mouse is above the button and change color accordingly
     |
     |          Parameters:
     |              `position` (tuple): The x, y position provided by `pygame.mouse.get_pos()`
     |
     |  checkForInput(self, position: tuple) -> bool
     |      Given an (x,y) position, typically provided by `pygame.mouse.get_pos()`
     |      tell us if the mouse is interacting with button
     |
     |          Parameters:
     |              `position` (tuple): The x, y position provided by `pygame.mouse.get_pos()`
     |
     |  update(self, screen: pygame.Surface) -> None
     |      Updated the Button state
     |
     |          Paramters:
     |              `screen` (pygame.Surface): The pygame surface object that we are composing the button onto
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

## Menu

    class Menu(builtins.object)
     |  Menu(caption='A Simple Pygame Menu', title='MENU', x=500, y=500, world=None, background=None, displaytitle=True, main=None, useDisplayScreen=True, showESCKEYhint=True)
     |
     |  A constructor for menus
     |
     |  Methods defined here:
     |
     |  __init__(self, caption='A Simple Pygame Menu', title='MENU', x=500, y=500, world=None, background=None, displaytitle=True, main=None, useDisplayScreen=True  
                 showESCKEYhint=True)
     |      Creates a Menu object
     |
     |      Parameters:
     |          `caption`            (str): The window caption of your menu
     |          `title`              (str): The title of your menu, is by default shown at the top of your menu, can be hidden by setting 'displayTitle' to False
     |          `x`                  (int): The width of your menu, leave blank if using a pygame.Surface object or using another menu as main
     |          `y`                  (int): The width of your menu, leave blank if using a pygame.Surface object or using another menu as main
     |          `world`   (pygame.Surface): A pygame surface object you can use as the base python screen. An alternative to using x, y for dimensions.
     |                                      Useful for having all menus use the same display
     |          `background`         (str): The local path to a background file
     |                                      If you have an image you want to use as a background, provide the **FULL** filepath to the image here.
     |          `displaytitle`      (bool): A boolean to hide or show the title on your menu
     |          `main`              (Menu): Add a main menu to return to with ESC. Pass in another menu object to be able to return to it by clicking ESC
     |          `useDisplaySceen`   (bool): In the event you do not want to use the display screen passed in by `world` or `main`, set this to False. Default is True
     |          `showESCKEYhint`    (bool): True if you wish to show a hint at the top of all menus that have a `main` parameter that is not None. Else set to False.
     |
     |  add_button(self, label: str = 'button', function: <built-in function callable> = None, x: int = 0, y: int = 0, font: str = None, fontsize: int = 30, 
                   basecolor: tuple = (0, 0, 255), hovercolor: tuple = (255, 255, 0)) -> None
     |      Add a button object to internal button storage.
     |      When Menu is run using `<menu name>.run_menu()`, all buttons added with this method are rendered.
     |
     |
     |          Parameters:
     |              `label`          (str): Text to display on the button
     |              `function`  (callable): A callable function for the button to execute
     |
     |                  NOTE : functions passed in must not be called when being passed. Do not use `()` when passing function in.
     |
     |                      Proper Usage Example:
     |
     |                          `def callable_method():`
     |                              `do something`
     |
     |                          `menu.add_button(... , ... , function = callable_method , ... )`
     |
     |              `x`              (int): The x coordinate of the button center
     |              `y`              (int): The y coordinate of the button center
     |              `font`           (str): The filepath to a font ttf file if applicable. Leave as None to use default font
     |              `fontsize`       (int): The size of the label font
     |              `basecolor`    (tuple): RGB tuple representing the button color when mouse IS NOT hovering over it
     |              `hovercolor`   (tuple): RGB tuple representing the button color when mouse IS hovering over it
     |
     |  add_text(self, text: str = 'default', x: int = 0, y: int = 0, size: int = 45, color: str = '#b68f40') -> None
     |      Add text to render for the menu
     |
     |          Parameters:
     |              `text`   (str): The text to add
     |              `x`      (int): The x coordinates for text center
     |              `y`      (int): The y coordinates for text center
     |              `size`   (int): The size of the text
     |              `color`  (str): A string representing color values in hexadecimal
     |
     |  default_func(self) -> None
     |      Useless placeholder to demonstrate a thing a button can do.
     |
     |  display_text(self, text='', size=45, color='#b68f40', pos=(0, 0), custom_font=None, line_spacing=10)
     |              Displays the text on the Menu
     |
     |                  Parameters:
     |
     |                      `text`             (str): The text to display
     |                      `size`             (int): The size of the text. Default is 45
     |                      `color`            (str): Color of the text as a hexadecimal code.
     |                      `pos`  (tuple[int, int]): The position of the text in x,y format
     |                      `custom_font`      (str): Custom font (.ttf) filepath. Default is None
     |                      `line_spaceing`    (int): The spacing for text that uses `
     |      ` characters
     |
     |  gen_text(self, text: str = '', size: str = 45, color: str = '#b68f40', pos: tuple = (0, 0), custom_font: str = None) -> None
     |      Generates text to display
     |
     |          Parameters:
     |
     |              `text`             (str): The text to display
     |              `size`             (int): The size of the text. Default is 45
     |              `color`            (str): Color of the text as a hexadecimal code.
     |              `pos`  (tuple[int, int]): The position of the text in x,y format
     |              `custom_font`      (str): Custom font (.ttf) filepath. Default is None
     |
     |  load_background_coords(self, use_center=True) -> None
     |      Loads the background coordinates
     |
     |          Parameters:
     |              `use_center` (bool): Default is True. Declares whether to center background or not
     |
     |  load_win_dimensions(self, x: int, y: int) -> None
     |      Given an x, y input - load them as the instance variables for window height and width
     |
     |          Parameters:
     |              `x` (int): The width of Menu window
     |              `y` (int): The height of Menu window
     |
     |  prepSCREEN(self, screen: pygame.Surface = None, background_filepath: str = None) -> None
     |      Initializes pygame and sets the screen and background where applicable
     |
     |          Parameters:
     |              `screen` (pygame.Surface)  : Default is None. Pass in pygame.Surface object instead to use that
     |              `background_filepath` (str): Default is None. The filepath of an image file to use as a background.
     |
     |  render_background(self, color: str = 'black') -> None
     |      Renders the background. If self.background is not None, uses that as the background
     |      otherwise uses a solid color
     |
     |          Parameters:
     |              `color` (str): Default is 'black'. A string representing the color.
     |
     |                  Example:
     |                      color = "black"
     |
     |  render_buttons(self, MOUSEPOS: tuple = None) -> None
     |      Renders all added Buttons onto the menu
     |
     |          Parameter:
     |              `MOUSEPOS` (tuple[int, int]): An x, y pos extracted from pygame.mouse.get_pos
     |
     |  render_display_texts(self) -> None
     |      Renders all added Text onto the menu
     |
     |  run_menu(self) -> None
     |      Runs the menu as a loop
     |
     |  set_background_color(self, color: str = None) -> None
     |      Change the background color.
     |
     |          Parameters:
     |              `color` (str): A string representing the color.
     |
     |                  Example:
     |                      color = "white"
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

# FUNCTIONS
    get_font(size: int = None, font_path: str = None) -> pygame.font.Font
        Gets a font from a provided .ttf file indicated by `font_path`

            Parameters:
                `size`      (int): The size of the font
                `font_path` (str): Default is None. The path to a font file if applicable.
