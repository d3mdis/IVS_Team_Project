import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    colors,
)

import math_lib
import math_interface
from evaluate_rec import Evaluate

HEIGHT = 500
WIDTH = 360
BG_GRADIENT = ft.LinearGradient(
    begin=ft.alignment.top_center,
    end=ft.alignment.bottom_center,
    stops=[0.0, 0.58, 1.0],
    colors=["#51108c", "#1c144f", "#100149"]
)
DISPLAY_GRADIENT = ft.LinearGradient(
    begin=ft.alignment.bottom_left,
    end=ft.alignment.top_right,
    colors=["#51108c", "#0c0038"]
)


class CalculatorApp(UserControl):
    def __init__(self, library: math_interface.MathInterface):
        super().__init__()
        self.m = library
        self.result = None
        self.expression = None
        self.hint_states = ["Zero Division", "Syntax error", " 0"]

    def build(self):
        self.result = Text(value=" 0", width=300, text_align=ft.TextAlign.END, no_wrap=True, color=colors.WHITE, size=40)
        self.expression = Text(value="0", width=260, text_align=ft.TextAlign.END, no_wrap=True, color=colors.WHITE, size=20)

        result_field = Container(
            width=330,
            height=100,
            expand=1,
            opacity=0.8,
            padding=5,
            border_radius=10,
            gradient=DISPLAY_GRADIENT,
            content=Row(
                expand=1,
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    Column(
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        controls=[
                            self.expression,
                            self.result,
                        ]
                    )
                ]
            )

        )

        numpad_parentheses = Row(
            controls=[
                        ElevatedButton(
                            text="(",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="(",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text=")",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data=")",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                    ]
        )
        numpad_1 = Row(
            controls=[
                        ElevatedButton(
                            text="AC",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="AC",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="1/x",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="1/x",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="x!",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="!",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            content=ft.Icon(name=ft.icons.BACKSPACE, color=colors.WHITE),
                            bgcolor="#e28600",
                            data="BACKSPACE",
                            on_click=self.button_clicked,
                            expand=2,
                        ),
                    ]
        )
        numpad_2 = Row(
            controls=[
                        ElevatedButton(
                            text="7",
                            bgcolor="#0c0038",
                            elevation=5,
                            color=colors.WHITE,
                            data="7",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="8",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="8",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="9",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="9",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="+",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="+",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="-",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="-",
                            on_click=self.button_clicked,
                            expand=1,
                        ),

                    ]
        )
        numpad_3 = Row(
            controls=[
                        ElevatedButton(
                            text="4",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="4",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="5",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="5",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="6",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="6",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="*",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="*",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="/",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="/",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                    ]
        )
        numpad_4 = Row(
            controls=[
                        ElevatedButton(
                            text="1",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="1",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="2",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="2",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="3",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="3",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="xⁿ",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="^",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="√",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="√",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                    ]
        )
        numpad_5 = Row(
            controls=[
                        ElevatedButton(
                            text="0",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="0",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text=".",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data=".",
                            on_click=self.button_clicked,
                            expand=2,
                        ),
                        ElevatedButton(
                            text="=",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="=",
                            on_click=self.button_clicked,
                            expand=2,
                        )
                    ]
        )

        numpad = Container(
            width=WIDTH,
            expand=2,
            content=Column(
                controls=[
                    numpad_parentheses,
                    numpad_1,
                    numpad_2,
                    numpad_3,
                    numpad_4,
                    numpad_5,
                ]
            )
        )

        calculator = Container(
            width=WIDTH,
            height=HEIGHT,
            gradient=BG_GRADIENT,
            padding=10,
            border_radius=ft.border_radius.all(10),
            content=Column(
                controls=[result_field,
                          numpad]
            )
        )

        # application's root control (i.e. "view") containing all other controls
        return calculator

    def check_expression(self, expression: str) -> bool:
        for char in expression:
            if char not in "0123456789.+-*/^√()!":
                return True
        lpar = expression.count("(")
        rpar = expression.count(")")
        if lpar != rpar:
            return True
        return False

    def parse_expression(self, expression):
        try:
            evaluated_expression = Evaluate(expression, self.m).evaluate()
        except ZeroDivisionError:
            return "Zero Division"
        except ValueError:
            return "Syntax error"

        result = str(evaluated_expression)
        if result == "None":
            result = "0"
        elif len(result) > 13:
            return '{:.2e}'.format(float(result))
        if result[-2:] == ".0":
            return result[:-2]
        else:
            return result

    def calculate_result(self):
        self.result.value = self.result.value.strip()
        if self.check_expression(self.result.value):
            self.result.value = "Syntax error"
        else:
            self.expression.value = self.result.value
            self.result.value = self.parse_expression(self.result.value)
            self.expression.value += "="

    def button_clicked(self, e):
        #delete all
        if e.control.data == "AC":
            self.result.value = " 0"

        #backspace
        elif e.control.data == "BACKSPACE":
            self.result.value = self.result.value[:-1]

        #evaluate expression
        elif e.control.data == "=":
            self.calculate_result()
        #inverse
        elif e.control.data == "1/x":
            if len(self.result.value) == 1:
                self.result.value = f"1/{self.result.value}"
            else:
                self.result.value = f"1/({self.result.value})"

        #base hint
        else:
            if self.result.value in self.hint_states:
                self.result.value = ""
            self.result.value += e.control.data
        self.update()


def set_page_params(page: Page):
    page.window_width = WIDTH
    page.window_height = HEIGHT + 60
    page.window_maximizable = False
    page.bgcolor = "#0c0038"

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_opacity = 0.9
#   page.window_title_bar_hidden = True
    page.window_left = 400
    page.window_top = 200


def main(page: Page):
    mathlib = math_lib.MathLib()
    # create application instance
    calc = CalculatorApp(mathlib)

    key_map = {
        "0": ")",
        "1": "!",
        "6": "^",
        "8": "*",
        "9": "(",
    }

    def key_pressed(e):
        if e.key == "Escape":
            e.page.window_close()
        elif e.key == "Delete":
            calc.result.value = " 0"
        elif e.key == "Backspace":
            calc.result.value = calc.result.value[:-1]
        elif e.key == "Enter":
            calc.calculate_result()
        elif e.key in "0123456789-+^*()/!.":
            if calc.result.value == " 0":
                calc.result.value = ""
            if e.key in key_map.keys() and e.shift:
                calc.result.value += key_map[e.key]
            else:
                calc.result.value += e.key
        calc.update()

    # set page parameters
    set_page_params(page)
    page.title = "Calc App"
    page.on_keyboard_event = key_pressed

    # add application's root control to the page
    page.add(Container(
        width=360,
        height=100,
        expand=1,
        opacity=0.8,
        padding=5,
        border_radius=10,
        bgcolor="#51108c",
        content=ft.WindowDragArea(
            Row(
                expand=1,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=255,
                controls=[
                    ft.IconButton(ft.icons.MENU_BOOK_ROUNDED,
                                  tooltip="Dokumentacia pouzivania bla bla bla\n"
                                          "pre hybanie oknom dragujte tento riadok"
                                          "esc zavrie appku,del funguje ako AC, backspace je backspace lol. cisla a operacie funguju tak ako vam hovori intuicia.\n"
                                          "odmocnina pouzitie cislo√cislo\n"
                                          "neskor tu bude nieco rozumne, napr tuknutie na otvorenie dokumentacie\n"
                                          "co by ste povedali, keby este rychlo implementujeme nejake mikrotranzakcie? Mozno light theme..\n"
                                          "podla mna je cela kalkulacka prilis fialova, ale posudok necham na vas majstri",

                                  icon_color=colors.WHITE,
                                  ),
                    ft.IconButton(ft.icons.CLOSE, icon_color=colors.WHITE, on_click=lambda _: page.window_close()),
                ]
            )
        )
    ))
    page.add(calc)


ft.app(target=main)
