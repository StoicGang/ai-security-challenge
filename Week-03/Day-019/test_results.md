# Test Results - Day 019: Two-Tool Agent

## Objective

Verify that the agent correctly routes user requests to the appropriate tool based on the user's intent.

---

## Test 1 - Calculator Tool Routing

### User Input
>Ask a question: What is ((75+25)×(18−6))/11?

arguments={'expression': '((75+25)*(18-6))/11'} id='9i8ztpvh' name='calculator' type='function_call' signature='EsoCCscCARFNMg8L66
The value of the expression **((75+25)×(18−6))/11** is:

1. First, solve the expressions inside the parentheses:
   * $75 + 25 = 100$
   * $18 - 6 = 12$

2. Next, multiply the results:
   * $100 \times 12 = 1200$

3. Finally, divide by 11:
   * $1200 / 11 = 109 \frac{1}{11} \approx 109.09$ (repeating)


## Test 2 - Scoped File Reader Routing
### User Input
>Ask a question: Extract the key points from the training manual and use real life analogy to explain the key concept

Based on the training manual, here is an extraction of the key points regarding the **Fast Gradient Sign Method (FGSM)**, followed by an intuitive, real-life analogy to explain how it works.

---

### **Key Points from the Training Manual**

#### **1. What is FGSM?**
FGSM (Fast Gradient Sign Method) is a simple, highly efficient "one-step" adversarial attack designed to trick Machine Learning models. By adding a tiny, mathematically calculated, and human-imperceptible amount of noise (perturbation) to a clean input, it forces the model to make a wildly incorrect prediction.

#### **2. The Formula & Its 4 Moving Parts**
The attack is calculated using a single equation:
$$\mathbf{x_{adv} = x + \epsilon \cdot \text{sign}(\nabla_x J(\theta, x, y))}$$

*   **Part 1: $x$ (The Clean Input):** This is the original, untouched data point (like a clean image of a panda) before any tampering occurs.
*   **Part 2: $\nabla_x J(\theta, x, y)$ (The Gradient / The Compass):** In normal training, the model uses gradients to adjust its *internal weights* to get smarter. FGSM flips this: it calculates the gradient with respect to the *input pixels* ($x$) to ask: *"Which direction should I shift each pixel to make the model's loss (error rate) as high as possible?"*
*   **Part 3: $\text{sign}()$ (The Equalizer):** If you only changed the pixels that matter the most, the changes would cluster in one spot and be highly visible to humans. The $\text{sign}()$ function strips away the *magnitude* of the changes and keeps only the *direction* ($+1$ or $-1$). This spreads the changes uniformly across every single pixel, making the edit completely "flat" and invisible to the human eye.
*   **Part 4: $\epsilon$ (Epsilon / The Budget):** A tiny decimal multiplier (typically between $0.01$ and $0.3$) that acts as the attacker's "stealth dial." 
    *   *High $\epsilon$:* Highly successful attack, but the image looks blurry/grainy to humans.
    *   *Low $\epsilon$:* Imperceptible to humans, but might fail to fool the AI.

#### **3. Why is it "Fast"?**
FGSM is incredibly fast because it takes exactly **one step**. It performs one forward pass to get the predictions, one backward pass to calculate the gradient direction, multiplies it by the budget ($\epsilon$), and adds it to the original. 

#### **4. The Limitation**
Because it only takes one step, it is a "shortcut." It looks at a complex, curving mathematical landscape and assumes a straight line. If the model has adversarial defenses, this single-step assumption might miss the mark. (Advanced attacks like BIM or PGD fix this by taking multiple smaller steps).

---

### **The Real-Life Analogy: The "Stealth Makeup" Airport Escape**

Imagine you are trying to sneak past a **smart facial recognition gate** at an airport. 

The security camera is an AI model trained to identify your face as **"User: John."** Your goal is to get the gate to misidentify you as **"User: Unknown"** (causing a system error) so you can slip through. However, there are human security guards standing right next to the camera. If you wear a heavy Halloween mask or a fake beard, the human guards will immediately notice and arrest you. 

Here is how you apply the **FGSM technique** to pull off this escape:

#### **1. The Clean Input ($x$)**
*   **In the formula:** Your original, clean image.
*   **In real life:** Your bare, natural face.

#### **2. The Gradient ($\nabla_x J$) — "The Weakness Blueprint"**
*   **In the formula:** Calculating which pixel direction maximizes loss.
*   **In real life:** You sneak a look at the AI camera's software blueprint. It tells you exactly how the AI measures faces. You ask: *"If I could change every millimeter of my skin, which direction (slightly lighter or slightly darker) would confuse the AI's math the most?"* The blueprint gives you a map showing exactly which direction to change each patch of skin.

#### **3. The Equalizer ($\text{sign}()$) — "The Airbrushing Rule"**
*   **In the formula:** Turning all gradient values into a uniform $+1$ or $-1$.
*   **In real life:** If you only put heavy black makeup on your nose and forehead (the highest gradient areas), you'll look ridiculous, and the human guards will stop you. To stay stealthy, you decide to ignore *how much* you need to change any one spot. Instead, you apply a completely flat, microscopic layer of skin-tone powder to **every single millimeter** of your face. Every spot is adjusted by the exact same tiny amount—either a fraction of a shade lighter or a fraction of a shade darker. Because the change is spread perfectly evenly across your entire face, there are no weird patches. To a human guard, you still look exactly like "John."

#### **4. The Budget ($\epsilon$) — "The Makeup Thickness"**
*   **In the formula:** The scale factor of the noise.
*   **In real life:** This is how thick you apply the makeup powder. If you use too much ($\epsilon = 0.3$), you will look cakey and dusty, drawing the human guards' attention. If you use too little ($\epsilon = 0.01$), the security camera will still recognize you as "John." You dial it to the perfect sweet spot—just enough to throw off the camera's math, but light enough to look like normal skin.

#### **5. One-Step Execution**
*   **In the formula:** A single calculation and addition.
*   **In real life:** You apply this makeup once in the bathroom, walk confidently up to the gate, and pass through. You don't stand in front of the camera adjusting your makeup back and forth (which would be a multi-step attack like PGD)—you calculate it once, apply it once, and it either works or it doesn't.