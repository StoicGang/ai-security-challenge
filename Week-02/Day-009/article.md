One line of math. Four moving parts. A model that breaks in a single step.

In the last article, we established what Fast Gradient Sign Method (FGSM) is and why it exists.

Now we go inside it.

By the end of this article, you should be able to look at the FGSM formula, point at each piece, and explain in plain language what it is doing and why it matters. No ML background required.
The Formula

Here it is. Exactly as Goodfellow wrote it in 2014:

x_adv = x + ε · sign( ∇ₓ J(θ, x, y) )

Press enter or click to view image in full size
FGSM Attack

Four moving parts. Each one deliberate. Let’s go through them left to right.
Part 1: x, The Input

x is the clean input. An image. A file. A data point your model has never seen tampered with.

This is where the attack starts. Everything else in the formula describes what gets added to it.
Part 2:∇ₓ J(θ, x, y), The Gradient

This is the compass.

J(θ, x, y) is the loss function the score that measures how wrong the model's prediction is. During normal training, the model computes this loss and asks: "How should I change my weights to reduce it?"

FGSM asks a different question entirely.

∇ₓ means: compute the gradient not with respect to the weights, but with respect to x: the input pixels. Ask the input: "Which direction should each pixel move to make the loss as large as possible?"

The gradient answers that question. For every single pixel in the image, it returns a direction and a magnitude how much and which way to push it to make the model maximally wrong.
Part 3: sign(), The Equaliser

This is the piece most explanations skip. It’s the most important one.

The raw gradient gives you both a direction and a magnitude for each pixel. Some pixels influence the model’s loss a lot. Others barely matter. If you used the raw gradient directly, the perturbation would concentrate on a small number of pixels pushing those few hard while leaving the rest alone.

That would be detectable. Visible. A cluster of changed pixels stands out.

sign() strips the magnitude out entirely. It keeps only the direction.

Every pixel gets exactly +1 or -1. Push up or push down. Equal weight. No clustering.

The effect: the perturbation is spread uniformly across every pixel in the image. Each individual change is tiny. The total effect on the model’s decision boundary is large.
Write on Medium

This is why adversarial examples look clean to the human eye. The attack is distributed too evenly to see.
Part 4 ε (Epsilon), The Budget

ε is a small number. Typically between 0.01 and 0.3.

It controls how far each pixel is allowed to move. Think of it as the attacker’s budget. Spend more, the attack succeeds more reliably. Spend too much, the perturbation becomes visible to the human eye and the attack becomes detectable.

The attacker’s goal is to find the smallest ε that still breaks the model. That balance point is different for every model, every dataset, and every epsilon value is a tradeoff the attacker consciously makes.

A low epsilon attack (say 0.01) is nearly invisible but may not fully break the model. A high epsilon attack (say 0.3) is reliable but leaves visible grain in the image. In security terms, ε is the attacker’s stealth dial.
Putting It Together:One Step, Done

Put all four parts back together:

x_adv = x + ε · sign( ∇ₓ J(θ, x, y) )

In plain English: take the original input, ask the model which direction every pixel should move to cause maximum loss, keep only the direction (not the magnitude), scale it by epsilon, and add it to the original.

One forward pass to get the predictions. One backward pass to compute the gradient. One multiplication. One addition.

The attack is complete. That is why the word Fast is in the name.
The Code: What This Looks Like in Practice

Here is the FGSM function implemented from scratch using TensorFlow’s GradientTape. No library shortcuts. Every line maps directly to a part of the formula above.
Press enter or click to view image in full size

Read the comments in that cell carefully. Each one points back to a part of the formula. This is the whole attack not abstracted, not wrapped in a library call. The raw mechanics.
What Happens When You Run It

After running the attack at a chosen epsilon, the output from Cell 8 tells the full story:
Press enter or click to view image in full size

That printed gap is not a benchmark from a paper. It came from your model, your training run, your epsilon choice. That is what makes it real.
Why One Step Is Both the Strength and the Ceiling

FGSM is fast because it takes exactly one gradient step. That same property is also why it is not the strongest possible attack.

A single gradient step points in the right direction at one specific point on the loss surface. But the surface is complex. It curves. After the step, the model’s behaviour has shifted and the direction that was optimal at the start may no longer be optimal at the landing point.

This is why FGSM sometimes fails against models with adversarial defences. The one-step shortcut, which makes it fast, also makes it imprecise.

The attacks that came after FGSM BIM and PGD fix this by taking many smaller steps and correcting after each one. But that comes in the next series.

For now: FGSM is the proof of concept. The one punch that showed the attack class was real.

Thanks for sticking with me. If this article helped you see FGSM as more than just a line of math, then it has done its job. In the next part, we’ll take that same intuition and see what happens when one step becomes many.