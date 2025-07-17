from manim import * 
from manim_slides import Slide
import random
import math
from manim import Dot, VMobject

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
        self.play(Create(points), run_time=1.5)
        self.next_slide()
        # Select 10 random points and change them into circles
        random_indices = random.sample(range(200), 10)
        circles = VGroup()
        transforms = []
        for idx in random_indices:
            dot = points[idx]
            # Increased radius for better visibility
            circle = Circle(radius=0.12, color=BLUE).move_to(dot.get_center())
            circles.add(circle)
            transforms.append(Transform(dot, circle))
        # Animate all transformations together
        self.play(*transforms)
        # Remove everything except the circles
        self.remove(axes, axes_labels, points)
        # Arrange circles vertically and move to the left, but animate each from its original position
        n_circles = len(circles)
        # Calculate target positions for vertical arrangement
        vertical_positions = []
        spacing = 0.5  # Increased spacing
        start_y = (n_circles - 1) / 2 * spacing
        for i in range(n_circles):
            pos = LEFT * 4 + UP * (start_y - i * spacing)  # Move further left
            vertical_positions.append(pos)
        # Animate each circle to its new position
        self.play(*[circle.animate.move_to(target) for circle, target in zip(circles, vertical_positions)], run_time=1.2)
        # --- END OF POINTS-TO-CIRCLES SECTION ---

        # --- NEURAL NETWORK VISUALIZATION (step-by-step build) ---
        input_x = LEFT * 3
        hidden_xs = [LEFT, ORIGIN, RIGHT]
        output_x = RIGHT * 3
        n_input = len(circles)
        n_hidden = 18
        n_output = 10
        spacing_input = 0.5
        spacing_hidden = 0.4
        spacing_output = 0.5
        # Move existing input nodes (circles) to input positions
        input_positions = [input_x + UP * ((n_input - 1) / 2 * spacing_input - i * spacing_input) for i in range(n_input)]
        self.play(*[circle.animate.move_to(pos) for circle, pos in zip(circles, input_positions)], run_time=1.2)
        self.next_slide()
        # Output nodes
        output_circles = VGroup()
        output_positions = [output_x + UP * ((n_output - 1) / 2 * spacing_output - i * spacing_output) for i in range(n_output)]
        for pos in output_positions:
            out_circle = Circle(radius=0.15, color=YELLOW).move_to(pos)
            output_circles.add(out_circle)
        self.play(Write(output_circles))
        self.next_slide()
        # Hidden layers, all at once
        hidden_layers = []
        all_hidden_layers = VGroup()
        for x in hidden_xs:
            layer = VGroup()
            layer_positions = [x + UP * ((n_hidden - 1) / 2 * spacing_hidden - i * spacing_hidden) for i in range(n_hidden)]
            for pos in layer_positions:
                node = Circle(radius=0.13, color=WHITE).move_to(pos)
                layer.add(node)
            hidden_layers.append(layer)
            all_hidden_layers.add(layer)
        self.play(Write(all_hidden_layers))
        self.next_slide()
        # Animate connections layer by layer
        all_layers = [circles] + hidden_layers + [output_circles]
        for l1, l2 in zip(all_layers[:-1], all_layers[1:]):
            lines = VGroup()
            for node1 in l1:
                for node2 in l2:
                    line = Line(node1.get_center(), node2.get_center(), stroke_width=1.5, color=GREY_C, stroke_opacity=0.4)
                    lines.add(line)
            self.add(lines)
            try:
                lines.z_index = 0
                l1.z_index = 1
                l2.z_index = 1
            except Exception:
                pass
            self.play(Create(lines), run_time=0.7)
        # Instantly add input arrow/label on the left
        input_arrow = Arrow(start=input_x + LEFT * 1.2, end=input_x, color=WHITE, buff=0.1, stroke_width=4)
        input_label = Text("Input", font_size=36).next_to(input_arrow, LEFT)
        self.add(input_arrow, input_label)
        # Instantly add output label
        output_arrow = Arrow(start=output_x + RIGHT * 1.2, end=output_x, color=YELLOW, buff=0.1, stroke_width=4)
        output_label = Text("Output", font_size=36, color=YELLOW).next_to(output_arrow, RIGHT)
        self.add(output_arrow, output_label)
        self.next_slide()

        # --- CLEAR AND NEW SLIDE: SMALL NETWORK WITH WEIGHTS, BIASES, AND CALCULATION ---
        self.clear()
        self.next_slide()
        # Small network: 2 input, 3 hidden, 1 output (with increased spacing and size)
        small_input_x = LEFT * 5
        small_hidden_x = ORIGIN
        small_output_x = RIGHT * 5
        small_input_nodes = VGroup()
        small_hidden_nodes = VGroup()
        small_output_node = Circle(radius=0.25, color=YELLOW).move_to(small_output_x)
        # Input nodes (larger spacing)
        for i in range(2):
            pos = small_input_x + UP * (0.8 - i * 1.6)
            node = Circle(radius=0.25, color=BLUE).move_to(pos)
            small_input_nodes.add(node)
        # Hidden nodes (larger spacing)
        for i in range(3):
            pos = small_hidden_x + UP * (1.6 - i * 1.6)
            node = Circle(radius=0.25, color=WHITE).move_to(pos)
            small_hidden_nodes.add(node)
        # Add all nodes
        self.play(Write(small_input_nodes), Write(small_hidden_nodes), Write(small_output_node))
        # Draw and label weights (input→hidden, hidden→output) with larger font
        weight_labels = VGroup()
        small_lines = VGroup()
        for i, inp in enumerate(small_input_nodes):
            for j, hid in enumerate(small_hidden_nodes):
                line = Line(inp.get_center(), hid.get_center(), stroke_width=3, color=GREY_C, stroke_opacity=0.7)
                label = MathTex(f"w_{{{j+1}{i+1}}}", color=YELLOW).scale(1.0)
                label.move_to(inp.get_center() + 0.6*(hid.get_center()-inp.get_center()) + UP*0.25)
                self.add(line, label)
                small_lines.add(line)
                weight_labels.add(label)
        for j, hid in enumerate(small_hidden_nodes):
            line = Line(hid.get_center(), small_output_node.get_center(), stroke_width=3, color=GREY_C, stroke_opacity=0.7)
            label = MathTex(f"w_{{o{j+1}}}", color=YELLOW).scale(1.0)
            label.move_to(hid.get_center() + 0.6*(small_output_node.get_center()-hid.get_center()) + UP*0.25)
            self.add(line, label)
            small_lines.add(line)
            weight_labels.add(label)
        # Label biases for hidden and output nodes (larger font)
        bias_labels = VGroup()
        for j, hid in enumerate(small_hidden_nodes):
            bias = MathTex(f"b_{{{j+1}}}", color=RED).scale(1.2).next_to(hid, LEFT, buff=0.4)
            self.add(bias)
            bias_labels.add(bias)
        bias_out = MathTex("b_o", color=RED).scale(1.2).next_to(small_output_node, LEFT, buff=0.4)
        self.add(bias_out)
        bias_labels.add(bias_out)
        self.next_slide()
        # Move network up to make room for equations
        network_group = VGroup(small_input_nodes, small_hidden_nodes, small_output_node, small_lines, weight_labels, bias_labels)
        self.play(network_group.animate.move_to(UP*2.5))
        # Show the general formula (larger font)
        calc_formula = MathTex(r"y = \sigma(w_{o1}h_1 + w_{o2}h_2 + w_{o3}h_3 + b_o)", font_size=48).move_to(DOWN*0.5)
        self.play(Write(calc_formula))
        self.next_slide()
        # Step-by-step: highlight each multiplication, fade others
        # Step 1: Highlight w_{o1}h_1
        # Fade other lines and formula
        fade_lines = [small_lines[1], small_lines[2]]
        self.play(
            *[l.animate.set_color(GREY_C).set_opacity(0.3) for l in fade_lines],
            small_lines[0].animate.set_color(YELLOW).set_stroke(width=5),
            weight_labels[5].animate.set_color(YELLOW).scale(1.2),
            calc_formula.animate.set_opacity(0.3)
        )
        step1 = MathTex(r"w_{o1} \times h_1 = 0.8 \times 0.5 = 0.4", font_size=44, color=YELLOW).move_to(DOWN*0.5)
        self.play(Write(step1))
        self.next_slide()
        # Step 2: Highlight w_{o2}h_2
        self.play(
            small_lines[0].animate.set_color(GREY_C).set_stroke(width=3).set_opacity(0.3),
            weight_labels[5].animate.set_color(YELLOW).scale(1.0),
            small_lines[1].animate.set_color(YELLOW).set_stroke(width=5).set_opacity(1.0),
            weight_labels[6].animate.set_color(YELLOW).scale(1.2),
            FadeOut(step1, shift=DOWN*0.5)
        )
        step2 = MathTex(r"w_{o2} \times h_2 = 0.2 \times 0.7 = 0.14", font_size=44, color=YELLOW).move_to(DOWN*0.5)
        self.play(Write(step2))
        self.next_slide()
        # Step 3: Highlight w_{o3}h_3
        self.play(
            small_lines[1].animate.set_color(GREY_C).set_stroke(width=3).set_opacity(0.3),
            weight_labels[6].animate.set_color(YELLOW).scale(1.0),
            small_lines[2].animate.set_color(YELLOW).set_stroke(width=5).set_opacity(1.0),
            weight_labels[7].animate.set_color(YELLOW).scale(1.2),
            FadeOut(step2, shift=DOWN*0.5)
        )
        step3 = MathTex(r"w_{o3} \times h_3 = 0.4 \times 0.1 = 0.04", font_size=44, color=YELLOW).move_to(DOWN*0.5)
        self.play(Write(step3))
        self.next_slide()
        # Step 4: Show addition with bias
        self.play(
            small_lines[2].animate.set_color(GREY_C).set_stroke(width=3).set_opacity(0.3),
            weight_labels[7].animate.set_color(YELLOW).scale(1.0),
            bias_out.animate.set_color(WHITE).scale(1.5),
            FadeOut(step3, shift=DOWN*0.5)
        )
        step4 = MathTex(r"0.4 + 0.14 + 0.04 + 0.3 = 0.88", font_size=44, color=BLUE).move_to(DOWN*0.5)
        self.play(Write(step4))
        self.next_slide()
        # Step 5: Show final result with activation function
        self.play(
            bias_out.animate.set_color(RED).scale(1.2),
            small_output_node.animate.set_color(WHITE).scale(1.3),
            FadeOut(step4, shift=DOWN*0.5)
        )
        step5 = MathTex(r"y = \sigma(0.88) \approx 0.82", font_size=48, color=YELLOW).move_to(DOWN*0.5)
        self.play(Write(step5))
        # Final highlight of the output
        self.play(
            small_output_node.animate.set_color(YELLOW).scale(1.0),
            step5.animate.set_color(WHITE)
        )
        self.next_slide()
