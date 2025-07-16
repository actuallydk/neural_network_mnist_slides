from manim import * 
from manim_slides import Slide
import random
import math

class MyScene(Slide):
    def construct(self):
        # First slide: Neural Network text
        title = Text("Neural Network", font_size=72)
        self.play(Write(title))
        self.next_slide()
        self.clear()

        svg3_1 = SVGMobject("src/1-3.svg").scale(2).set_color(WHITE)
        svg3_2 = SVGMobject("src/2-3.svg").scale(2).set_color(WHITE)
        svg3_3 = SVGMobject("src/3-3.svg").scale(2).set_color(WHITE)
        svg3_4 = SVGMobject("src/3-4.svg").scale(2).set_color(WHITE)
        group = VGroup(svg3_1, svg3_2, svg3_3, svg3_4).arrange(RIGHT, buff=1)
        self.play(Write(group))
        self.next_slide()

        ul = (-4.0, 2.0, 0.0)  # upper left
        ur = (4.0, 2.0, 0.0)   # upper right
        bl = (-4.0, -2.0, 0.0) # bottom left
        br = (4.0, -2.0, 0.0)  # bottom right
        self.play(
            svg3_1.animate.scale(0.7).move_to(ul),
            svg3_2.animate.scale(0.7).move_to(ur),
            svg3_3.animate.scale(0.7).move_to(bl),
            svg3_4.animate.scale(0.7).move_to(br),
            run_time=0.75
        )
        # Brain in center
        brain_svg = SVGMobject("src/brain.svg").scale(1.5).move_to((0.0, 0.0, 0.0))
        self.play(Write(brain_svg))
        self.next_slide()
        self.clear()
        
        # 70,000 Images
        title = Text("70,000 Images", font_size=72)
        self.play(Write(title))
        self.next_slide()
        self.clear()

        # What is a Neural Network?
        title = Text("What is a Neural Network?", font_size=72)
        self.play(Write(title))
        self.next_slide()
        self.clear()

        # x^2 graph
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 25, 5],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": False},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        graph = axes.plot(lambda x: x**2, color=RED)
        graph_label = axes.get_graph_label(graph, label="x^2")
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), Write(graph_label))
        self.next_slide()
        self.clear()

        # x^3 graph
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-130, 130, 20],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": False},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        graph = axes.plot(lambda x: x**3, color=YELLOW)
        graph_label = axes.get_graph_label(graph, label="x^3")
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), Write(graph_label))
        self.next_slide()
        self.clear()

    # Trigonometric functions on same graph
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-3, 3, 1],
            x_length=12,
            y_length=6,
            axis_config={"include_numbers": False},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Create the two trig functions
        sin_graph = axes.plot(lambda x: np.sin(x), color=RED, x_range=[-2*PI, 2*PI])
        cos_graph = axes.plot(lambda x: np.cos(x), color=BLUE, x_range=[-2*PI, 2*PI])
        
        # Create labels
        sin_label = MathTex("\\sin x", color=RED).to_edge(UR).shift(LEFT*2)
        cos_label = MathTex("\\cos x", color=BLUE).next_to(sin_label, DOWN)
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(sin_graph), Write(sin_label))
        self.play(Create(cos_graph), Write(cos_label))
        self.next_slide()
        self.clear()

        # Function: sin(2x) + cos(3x) + sin(random(1, π))
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-4, 4, 1],
            x_length=12,
            y_length=6,
            axis_config={"include_numbers": False},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Generate random constant for sin(random(1, π))
        random_val = random.uniform(1, math.pi)
        sin_random = math.sin(random_val)
        
        # Function definition
        def complex_function(x):
            return math.sin(2*x) + math.cos(3*x) + sin_random
        
        # Create points instead of continuous line
        points = VGroup()
        
        # Generate 200 points from -2π to 2π
        for i in range(200):
            x = -2*PI + i * (4*PI / 199)  # Spread points evenly
            y = complex_function(x)
            point = Dot(axes.c2p(x, y), radius=0.02, color=YELLOW)
            points.add(point)
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(points), run_time=3)
        self.next_slide()
        self.clear()
