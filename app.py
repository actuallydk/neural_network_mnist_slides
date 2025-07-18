from manim import *
from manim_slides import Slide
import random
import math
from manim import Dot, VMobject
import os

class MyScene(Slide):
    def construct(self):
        # First slide: Neural Network text
        title = Text("Neural Network", font_size=72)
        self.play(Write(title))
        self.next_slide()
        self.clear()

        # First slide: Neural Network text
        title = Text("Neural Network", font_size=72)
        self.play(Write(title))
        self.next_slide()
        self.clear()

        # Load PNG images
        img3_1 = ImageMobject("src/1-3.png").scale(2)
        img3_2 = ImageMobject("src/2-3.png").scale(2)
        img3_3 = ImageMobject("src/3-3.png").scale(2)
        img3_4 = ImageMobject("src/3-4.png").scale(2)
        group = VGroup(img3_1, img3_2, img3_3, img3_4).arrange(RIGHT, buff=1)
        self.play(FadeIn(group))
        self.next_slide()

        ul = (-4.0, 2.0, 0.0)  # upper left
        ur = (4.0, 2.0, 0.0)   # upper right
        bl = (-4.0, -2.0, 0.0) # bottom left
        br = (4.0, -2.0, 0.0)  # bottom right
        self.play(
        img3_1.animate.scale(0.7).move_to(ul),
        img3_2.animate.scale(0.7).move_to(ur),
        img3_3.animate.scale(0.7).move_to(bl),
        img3_4.animate.scale(0.7).move_to(br),
        run_time=0.75
        )

        # Brain in center (PNG version)
        brain_img = ImageMobject("src/brain.png").scale(1.5).move_to((0.0, 0.0, 0.0))
        self.play(FadeIn(brain_img))
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

        # --- NEW SLIDE: 2-3-2 NEURAL NETWORK ---
        self.clear()
        self.next_slide()
        
        # Network configuration: 2 inputs, 3 hidden, 2 outputs
        input_x = LEFT * 4
        hidden_x = ORIGIN
        output_x = RIGHT * 4
        # Create input nodes
        input_nodes = VGroup()
        for i in range(2):
            pos = input_x + UP * (0.8 - i * 1.6)
            node = Circle(radius=0.25, color=BLUE).move_to(pos)
            input_nodes.add(node)
        # Create hidden layer nodes
        hidden_nodes = VGroup()
        for i in range(3):
            pos = hidden_x + UP * (1.6 - i * 1.6)
            node = Circle(radius=0.25, color=WHITE).move_to(pos)
            hidden_nodes.add(node)
        # Create output nodes
        output_nodes = VGroup()
        for i in range(2):
            pos = output_x + UP * (0.8 - i * 1.6)
            node = Circle(radius=0.25, color=YELLOW).move_to(pos)
            output_nodes.add(node)
        # Add all nodes
        self.play(Write(input_nodes), Write(hidden_nodes), Write(output_nodes))
        self.next_slide()
        
        # Draw connections and weights step by step
        weight_labels = VGroup()
        connection_lines = VGroup()
        
        # First draw all lines
        all_lines = []
        for i, inp in enumerate(input_nodes):
            for j, hid in enumerate(hidden_nodes):
                line = Line(inp.get_center(), hid.get_center(), stroke_width=3, color=GREY_C, stroke_opacity=0.7)
                all_lines.append(line)
                connection_lines.add(line)
        # Hidden to output connections
        for j, hid in enumerate(hidden_nodes):
            for k, out in enumerate(output_nodes):
                line = Line(hid.get_center(), out.get_center(), stroke_width=3, color=GREY_C, stroke_opacity=0.7)
                all_lines.append(line)
                connection_lines.add(line)
        
        # Animate lines appearing
        self.play(Create(connection_lines), run_time=1.5)
        self.next_slide()
        
        # Add weight labels with animation
        weight_labels_list = []
        for i, inp in enumerate(input_nodes):
            for j, hid in enumerate(hidden_nodes):
                start = inp.get_center()
                end = hid.get_center()
                # Place at 40% along the line
                pos = start + 0.4 * (end - start)
                direction = end - start
                perp = np.array([-direction[1], direction[0], 0])
                perp = perp / np.linalg.norm(perp) if np.linalg.norm(perp) > 0 else perp
                offset = 0.25 * perp
                angle = np.arctan2(direction[1], direction[0])
                outward = LEFT * 0.15 if pos[0] < 0 else RIGHT * 0.15
                label = MathTex(f"w_{{{j+1}{i+1}}}", color=WHITE).scale(0.5)
                label.move_to(pos + offset + outward)
                label.rotate(angle)
                weight_labels_list.append(label)
                weight_labels.add(label)
        # Hidden to output weights (use v for right side, 60% along the line)
        for j, hid in enumerate(hidden_nodes):
            for k, out in enumerate(output_nodes):
                start = hid.get_center()
                end = out.get_center()
                # Place at 60% along the line
                pos = start + 0.6 * (end - start)
                direction = end - start
                perp = np.array([-direction[1], direction[0], 0])
                perp = perp / np.linalg.norm(perp) if np.linalg.norm(perp) > 0 else perp
                offset = 0.25 * perp
                angle = np.arctan2(direction[1], direction[0])
                outward = LEFT * 0.15 if pos[0] < 0 else RIGHT * 0.15
                label = MathTex(f"v_{{{k+1}{j+1}}}", color=WHITE).scale(0.5)
                label.move_to(pos + offset + outward)
                label.rotate(angle)
                weight_labels_list.append(label)
                weight_labels.add(label)
        
        # Animate weight labels appearing one by one
        for label in weight_labels_list:
            self.play(Write(label), run_time=0.2)
        self.next_slide()
        
        # Add bias labels with animation
        bias_labels = VGroup()
        bias_labels_list = []
        for j, hid in enumerate(hidden_nodes):
            bias = MathTex(f"b_{{{j+1}}}", color=RED).scale(0.6).next_to(hid, LEFT, buff=0.6)
            bias_labels_list.append(bias)
            bias_labels.add(bias)
        for k, out in enumerate(output_nodes):
            bias = MathTex(f"b_{{{k+1}}}", color=RED).scale(0.6).next_to(out, LEFT, buff=0.6)
            bias_labels_list.append(bias)
            bias_labels.add(bias)
        
        # Animate bias labels appearing one by one
        for bias in bias_labels_list:
            self.play(Write(bias), run_time=0.2)
        self.next_slide()
        
        # Shrink the entire network
        network_group = VGroup(input_nodes, hidden_nodes, output_nodes, connection_lines, weight_labels, bias_labels)
        self.play(network_group.animate.scale(0.7).move_to(UP * 1.5))
        self.next_slide()
        
        # Add equation at the bottom
        equation = MathTex(r"y_1 = \sigma(w_{11}h_1 + w_{12}h_2 + w_{13}h_3 + b_1)", font_size=36, color=WHITE).move_to(DOWN * 1.5)
        equation2 = MathTex(r"y_2 = \sigma(w_{21}h_1 + w_{22}h_2 + w_{23}h_3 + b_2)", font_size=36, color=WHITE).move_to(DOWN * 2.2)
        self.play(Write(equation))
        self.next_slide()
        self.play(Write(equation2))
        self.next_slide()
        
        # Show network architecture
        arch_text = Text("2-3-2 Neural Network", font_size=24, color=WHITE).move_to(DOWN * 3.0)
        self.play(Write(arch_text))
        self.next_slide()

        # --- NEW SLIDE: RELU AND SIGMOID SIDE BY SIDE ---
        self.clear()
        self.next_slide()
        
        # Axes for ReLU
        relu_axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 4, 1],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": False},
        ).to_edge(LEFT, buff=1.5)
        relu_graph = relu_axes.plot(lambda x: max(0, x), color=YELLOW)
        relu_label = MathTex(r"\text{ReLU}(x)", font_size=32, color=YELLOW).next_to(relu_axes, UP)
        
        # Axes for Sigmoid
        sigmoid_axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1, 0.2],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": False},
        ).to_edge(RIGHT, buff=1.5)
        sigmoid_graph = sigmoid_axes.plot(lambda x: 1/(1+np.exp(-x)), color=BLUE)
        sigmoid_label = MathTex(r"\sigma(x)", font_size=32, color=BLUE).next_to(sigmoid_axes, UP)
        
        # Show both plots and labels
        self.play(Create(relu_axes), Create(sigmoid_axes))
        self.play(Create(relu_graph), Create(sigmoid_graph))
        self.play(Write(relu_label), Write(sigmoid_label))
        self.next_slide()
        
        # Write 'Activation Functions' below
        act_text = Text("Activation Functions", font_size=36, color=WHITE).move_to(DOWN * 2.5)
        self.play(Write(act_text))
        self.next_slide()

        # --- ANIMATED NEURAL NETWORK FORWARD AND BACKWARD PASS ---
        self.clear()
        self.next_slide()

        # Network structure: 3 input, 4 hidden, 2 output
        input_x = LEFT * 4
        hidden_x = ORIGIN
        output_x = RIGHT * 4
        input_nodes = VGroup()
        for i in range(3):
            pos = input_x + UP * (1 - i * 1.0)
            node = Circle(radius=0.25, color=BLUE).move_to(pos)
            input_nodes.add(node)
        hidden_nodes = VGroup()
        for i in range(4):
            pos = hidden_x + UP * (1.5 - i * 1.0)
            node = Circle(radius=0.25, color=WHITE).move_to(pos)
            hidden_nodes.add(node)
        output_nodes = VGroup()
        for i in range(2):
            pos = output_x + UP * (0.5 - i * 1.0)
            node = Circle(radius=0.25, color=YELLOW).move_to(pos)
            output_nodes.add(node)

        # Draw all nodes and lines with dim colors
        input_hidden_lines = VGroup()
        for i_node in input_nodes:
            for h_node in hidden_nodes:
                line = Line(i_node.get_center(), h_node.get_center(), color=GREY)
                line.set_opacity(0.5)
                input_hidden_lines.add(line)
        hidden_output_lines = VGroup()
        for h_node in hidden_nodes:
            for o_node in output_nodes:
                line = Line(h_node.get_center(), o_node.get_center(), color=GREY)
                line.set_opacity(0.5)
                hidden_output_lines.add(line)

        self.play(
            *[FadeIn(mob) for mob in input_nodes],
            *[FadeIn(mob) for mob in hidden_nodes],
            *[FadeIn(mob) for mob in output_nodes],
            *[FadeIn(line) for line in input_hidden_lines],
            *[FadeIn(line) for line in hidden_output_lines],
        )

        # Forward Pass text (center top)
        forward_text = Text("Forward Pass", font_size=36, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(forward_text))

        # Highlight forward pass: input->hidden (BLUE_B), hidden->output (GREEN_B)
        for line in input_hidden_lines:
            self.play(line.animate.set_color(BLUE_B).set_opacity(1.0), run_time=0.08)
        for line in hidden_output_lines:
            self.play(line.animate.set_color(GREEN_B).set_opacity(1.0), run_time=0.08)
        self.next_slide()
        self.clear()

        # Cross Categorical Entropy Loss (center top)
        loss_text = Text("Cross Categorical Entropy Loss", font_size=36, color=YELLOW).to_edge(UP)
        loss_formula = MathTex(r"L(z, y) = -\frac{1}{N} \sum_{n=1}^{N} \sum_{c=1}^{C} y_{n,c} \cdot \log\left( \frac{e^{z_{n,c}}}{\sum_{j=1}^{C} e^{z_{n,j}} + \varepsilon} \right)", font_size=36, color=WHITE).next_to(loss_text, DOWN, buff=0.5)
        self.play(FadeIn(loss_text), Write(loss_formula))
        self.next_slide()
        self.clear()

        # Redraw network for backward pass
        self.play(
            *[FadeIn(mob) for mob in input_nodes],
            *[FadeIn(mob) for mob in hidden_nodes],
            *[FadeIn(mob) for mob in output_nodes],
            *[FadeIn(line) for line in input_hidden_lines],
            *[FadeIn(line) for line in hidden_output_lines],
        )

        # Backward Pass text (center top)
        backward_text = Text("Backward Pass", font_size=36, color=RED).to_edge(UP)
        self.play(FadeIn(backward_text))

        # Highlight backward pass: hidden->output (RED), input->hidden (ORANGE)
        for line in reversed(hidden_output_lines):
            self.play(line.animate.set_color(RED).set_opacity(1.0), run_time=0.08)
        for line in reversed(input_hidden_lines):
            self.play(line.animate.set_color(ORANGE).set_opacity(1.0), run_time=0.08)
        self.next_slide()
        self.clear()

        # --- APPLICATIONS OF NEURAL NETWORKS SLIDES (IMPROVED) ---
        # Slide: Applications of Neural Networks (title)
        app_title = MarkupText('Applications of <span fgcolor="{}">neural networks</span>'.format(YELLOW), font_size=60).move_to(ORIGIN)
        self.play(Write(app_title))
        self.next_slide()
        self.clear()

        # Slide: Image recognition
        img_head = MarkupText('<span fgcolor="{}">Image recognition</span>'.format(BLUE_B), font_size=54).to_edge(UP)
        img_points = [
            "Image Recognition (in Google Photos, Apple Photos, etc)",
            "Face ID and security systems",
            "Object detection in CCTV footage",
        ]
        bullets = VGroup(*[
            MarkupText(f"• {pt}", font_size=40) for pt in img_points
        ])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(img_head, DOWN, buff=1.2)
        self.play(Write(img_head), FadeIn(bullets))
        self.next_slide()
        self.clear()

        # Slide: Speech recognition
        speech_head = MarkupText('<span fgcolor="{}">Speech recognition</span>'.format(GREEN_B), font_size=54).to_edge(UP)
        speech_points = ["Virtual assistants", "Siri", "Alexa", "Google Assistant"]
        bullets = VGroup(*[
            MarkupText(f"• {pt}", font_size=40) for pt in speech_points
        ])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(speech_head, DOWN, buff=1.2)
        self.play(Write(speech_head), FadeIn(bullets))
        self.next_slide()
        self.clear()

        # Slide: Medical diagnosis
        med_head = MarkupText('<span fgcolor="{}">Medical diagnosis</span>'.format(RED), font_size=54).to_edge(UP)
        med_points = ["AI-assisted disease detection from patient data", "Can make breakthrough in Tumor Diagnosis in 5 years"]
        bullets = VGroup(*[
            MarkupText(f"• {pt}", font_size=40) for pt in med_points
        ])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(med_head, DOWN, buff=1.2)
        self.play(Write(med_head), FadeIn(bullets))
        self.next_slide()
        self.clear()

        # Slide: Drug Discovery
        drug_head = MarkupText('<span fgcolor="{}">Drug Discovery</span>'.format(PURPLE_B), font_size=54).to_edge(UP)
        drug_points = ["Accelerating new medicine development"]
        bullets = VGroup(*[
            MarkupText(f"• {pt}", font_size=40) for pt in drug_points
        ])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(drug_head, DOWN, buff=1.2)
        self.play(Write(drug_head), FadeIn(bullets))
        self.next_slide()
        self.clear()

        # Slide: Protein Structure Discovery
        prot_head = MarkupText('<span fgcolor="{}">Protein Structure Discovery</span>'.format(ORANGE), font_size=54).to_edge(UP)
        prot_points = ["AlphaFold: Nobel-level protein folding predictions", "Job which would take 50 YEARS"]
        bullets = VGroup(*[
            MarkupText(f"• {pt}", font_size=40) for pt in prot_points
        ])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(prot_head, DOWN, buff=1.2)
        self.play(Write(prot_head), FadeIn(bullets))
        self.next_slide()
        self.clear()

        # Slide: ChatGPT and LLMs
        chat_head = MarkupText('<span fgcolor="{}">ChatGPT &amp; LLMs</span>'.format(YELLOW), font_size=54).to_edge(UP)
        chat_points = [
            "Neural networks as the core of language models",
            "Text generation, Q&amp;A, and more"
        ]
        bullets = VGroup(*[
            MarkupText(f"• {pt}", font_size=40) for pt in chat_points
        ])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(chat_head, DOWN, buff=1.2)
        self.play(Write(chat_head), FadeIn(bullets))
        self.next_slide()
        self.clear()

        # Slide: Miscellaneous
        misc_head = MarkupText('<span fgcolor="{}">Other</span>'.format(GREY_B), font_size=54).to_edge(UP)
        misc_points = [
            "Weather forecasting",
            "Brain-computer interfaces",
            "Recommender systems",
            "Stock market prediction"
        ]
        bullets = VGroup(*[
            MarkupText(f"• {pt}", font_size=40) for pt in misc_points
        ])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(misc_head, DOWN, buff=1.2)
        self.play(Write(misc_head), FadeIn(bullets))
        self.next_slide()
        self.clear()
