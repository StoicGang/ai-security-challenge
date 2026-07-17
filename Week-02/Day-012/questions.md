### RAG Q&A Demonstration

**Question**

> What is the formula for the FGSM? What does each field represent?

**Retrieved Chunk**

> FGSM (Fast Gradient Sign Method) generates adversarial examples by adding a small perturbation to the input in the direction of the gradient of the loss with respect to the input.
>
> Formula:
> \[
> x_{adv} = x + \epsilon \cdot \text{sign}(\nabla_x J(\theta, x, y))
> \]
>
> Where:
> - \(x\): Original input image
> - \(\epsilon\): Perturbation magnitude
> - \(\nabla_x J(\theta, x, y)\): Gradient of the loss with respect to the input
> - \(\text{sign}(\cdot)\): Sign of the gradient
> - \(x_{adv}\): Adversarial example

**Grounded Answer**

> The FGSM formula is:
>
> \[
> x_{adv} = x + \epsilon \cdot \text{sign}(\nabla_x J(\theta, x, y))
> \]
>
> The original image \(x\) is modified by adding a small perturbation. The perturbation is controlled by \(\epsilon\), while the sign of the input gradient determines the direction that maximally increases the model's loss. The resulting image \(x_{adv}\) appears visually similar to the original but is more likely to fool the model. This explanation is based solely on the retrieved context.