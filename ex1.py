from manim import *
import numpy as np

class test(Scene):
    def construct(self):
        sq = Square(
            side_length=5, stroke_color=RED, fill_color= GREEN, fill_opacity=0.5
        ).to_edge(DR)
        tri = Triangle().to_edge(UL, buff=0.5)
        name = Tex("SIEMANO").shift(LEFT*3)
        self.play(Write(name))
        self.play(Create(tri))
        self.play(DrawBorderThenFill(sq), run_time=10)
        self.wait(5)
        self.play(name.animate.shift(UR), run_time = 1)
        self.play(name.animate.to_edge(DL), run_time = 5)
        self.play(sq.animate.scale(2), run_time = 4)
        self.wait(2)
        self.play(sq.animate.scale(0.1), run_time = 3)
        self.wait()




class wykres(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)
        self.add(plot, labels)


class graph(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-2*np.pi, 2*np.pi, (np.pi)/2],
            y_range = [-1.5, 1.5, 1],
            tips = False,
        )

        linia = axes.plot(lambda x: x, color = WHITE)
        sinus = axes.plot(lambda x: np.sin(x), color = RED)
        cosinus = axes.plot(lambda x: np.cos(x), color = BLUE)
        znak1 = axes.get_T_label(x_val = -2*np.pi, graph=sinus, label=Tex("$-2\pi$"), triangle_size=0).shift([-0.3, 0.1, 0])
        znak2 = axes.get_T_label(x_val=-1*np.pi, graph=sinus, label=Tex("$-\pi$"), triangle_size=0).shift([-0.3, 0.1, 0])
        znak3 = axes.get_T_label(x_val=0, graph=sinus, label=Tex("$0$"), triangle_size=0).shift([-0.3, 0.1, 0])
        znak4 = axes.get_T_label(x_val=np.pi, graph=sinus, label=Tex("$\pi$"), triangle_size=0).shift([-0.3, 0.1, 0])
        znak5 = axes.get_T_label(x_val=2*np.pi, graph=sinus, label=Tex("$2\pi$"), triangle_size=0).shift([-0.3, 0.1, 0])

        znaki = VGroup()
        znaki.add(znak1, znak2, znak3, znak4, znak5)

        self.play(Create(axes), run_time = 5)
        self.play(Create(sinus), run_time = 5)
        self.play(Create(cosinus), run_time = 5)
        self.play(Write(znaki), run_time = 5)
        self.wait()



class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Text("TOP"))
        t0.add_highlighted_cell((2,2), color=GREEN)
        x_vals = np.linspace(-2,2,5)
        y_vals = np.exp(x_vals)
        t1 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True)
        t1.add(t1.get_cell((2,2), color=RED))
        t2 = MathTable(
            [["+", 0, 5, 10],
            [0, 0, 5, 10],
            [2, 2, 7, 12],
            [4, 4, 9, 14]],
            include_outer_lines=True)
        t2.get_horizontal_lines()[:3].set_color(BLUE)
        t2.get_vertical_lines()[:3].set_color(BLUE)
        t2.get_horizontal_lines()[:3].set_z_index(1)
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT))
        a = Circle().set_color(RED).scale(0.5)
        b = cross.set_color(BLUE).scale(0.5)
        t3 = MobjectTable(
            [[a.copy(),b.copy(),a.copy()],
            [b.copy(),a.copy(),a.copy()],
            [a.copy(),b.copy(),b.copy()]])
        t3.add(Line(
            t3.get_corner(DL), t3.get_corner(UR)
        ).set_color(RED))
        vals = np.arange(1,21).reshape(5,4)
        t4 = IntegerTable(
            vals,
            include_outer_lines=True
        )
        g1 = Group(t0, t1).scale(0.5).arrange(buff=1).to_edge(UP, buff=1)
        g2 = Group(t2, t3, t4).scale(0.5).arrange(buff=1).to_edge(DOWN, buff=1)
        self.add(g1, g2)

class poradnikTryg(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2*np.pi, 2*np.pi, np.pi/2],
            y_range=[-1.5, 1.5, 1],
            tips=False,
        )
        axes2 = Axes(
            x_range=[-2*np.pi, 2*np.pi, np.pi/2],
            y_range=[-1.5, 1.5, 1],
            tips=False,
        )
        sin = axes.plot(lambda x: np.sin(x), color=RED)
        cos = axes2.plot(lambda x: np.cos(x), color=BLUE)

        znak11 = axes.get_T_label(x_val=-2*np.pi, graph = sin, label=Tex("$-2\pi$"), triangle_size=0, line_color=None)
        znak12 = axes.get_T_label(x_val=-1*np.pi, graph=sin, label=Tex("$-\pi$"), triangle_size=0, line_color=None)
        znak13 = axes.get_T_label(x_val=np.pi, graph=sin, label=Tex("$\pi$"), triangle_size=0, line_color=None)
        znak14 = axes.get_T_label(x_val=2*np.pi, graph=sin, label=Tex("$2\pi$"), triangle_size=0, line_color=None)
        grupaPi1 = VGroup()
        grupaPi1.add(znak11, znak12, znak13, znak14)

        znak21 = axes2.get_T_label(x_val=-2*np.pi, graph =cos, label=Tex("$-2\pi$"), triangle_size=0, line_color=None)
        znak22 = axes2.get_T_label(x_val=-1*np.pi, graph=cos, label=Tex("$-\pi$"), triangle_size=0, line_color=None)
        znak23 = axes2.get_T_label(x_val=np.pi, graph=cos, label=Tex("$\pi$"), triangle_size=0, line_color=None)
        znak24 = axes2.get_T_label(x_val=2*np.pi, graph=cos, label=Tex("$2\pi$"), triangle_size=0, line_color=None)
        grupaPi2 = VGroup()
        grupaPi2.add(znak21, znak22, znak23, znak24)

        singraf = VGroup()
        singraf.add(axes, sin)
        cosgraf = VGroup()
        cosgraf.add(axes2, cos)

        title = Text("sin(x)")
        title2 = Text("cos(x)")

        self.play(Create(axes), run_time = 3)
        self.play(Create(sin), run_time=3)
        self.play(singraf.animate.scale(0.4), run_time=3)
        self.play(singraf.animate.move_to(2.1*UP+4.2*LEFT), run_time = 3)
        grupaPi1.scale(0.4)
        grupaPi1.move_to(2*UP+4.2*LEFT)
        grupaPi2.scale(0.4)
        grupaPi2.move_to(2.1*DOWN+4.2*LEFT)
        self.play(Write(grupaPi1), run_time = 1)
        self.play(Create(axes2), run_time = 3)
        self.play(Create(cos), run_time = 3)
        self.play(cosgraf.animate.scale(0.4), run_time=3)
        self.play(cosgraf.animate.move_to(2.1*DOWN+4.2*LEFT), run_time = 3)
        self.play(Write(grupaPi2), run_time = 1)
        title.next_to(singraf, UP*0.5).scale(0.5)
        title2.next_to(cosgraf, UP*0.5).scale(0.5)
        self.play(Write(title), run_time=2)
        self.play(Write(title2), run_time=2)
        self.wait()
