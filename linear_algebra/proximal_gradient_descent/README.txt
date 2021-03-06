### What is this this thing?? 
The python file in this project is some rought pseudocode for proximal gradient descent. Below is a quick intuitive explanation of the method.

## Why we need Proximal Gradient Descent

Proximal gradient descent falls into a broader category of methods to fit statistical models to data. This fitting usually requires some sort of optimization. In a perfect world the function we are trying to optimize is convex, differentiable, and unconstrained. This means all we would need to do is basic gradient descent. 

In many real world applications, though, we don't have this luxury. A great example is the class of models with L1 regularization schemes like Lasso regression. This regularization method is an effective promoter of sparsity but it results in a loss function that is *non-differentiable* (aka it has kinks). This introduces a whole bunch of problems. For example, we might not always be able to compute a gradient to descent. Proximal gradient descent is a way of getting around this. 

## Some Definitions

The method makes use of two mathematical tools you may not have heard of already. Lets talk about them.

# Sub-Gradient
* *sub-gradients* are a generalization of the concept of the gradient which can be applied to non-differentiable functions. 
* First, let's visualize what the gradient of a convex, differentiable function looks like. These functions look like the mouth of a smiley face. The gradient of such a function is like a line which touches the curve at only one point. Note that if this is going to be true, the entire rest of the function is held above this line. Ok. That was painless. 
* Let's go on to convex non-differentiable functions. These are like smiley mouths with at least one kink, and they have sub-gradients instead of gradients. Sub-gradients are sets of vectors. Each vector in this set is kind of like a gradient. They touch at only one point and the entire function is held above them. This means that the only element in the sub-gradient IS the gradient at all the smooth, curvey parts of our function. At the kinks, though, the sub-gradient is the set of all lines which are below the function. 

![](http://upload.wikimedia.org/wikipedia/commons/4/4e/Subderivative_illustration.png)
Subgradient at x0 courtesy of Wikipedia. Simple, right?

# Proximal Operators
* The *proximal operator* takes a point in a space (x) and returns another point (x'). It is parameterized by a function (f) and a scalar (g). 
* x' is chosen because it both minimizes f and is close to x (in the L2 sense). The tradeoff between minimizing f and staying close to x is determined by g.

![](http://wikimedia.org/api/rest_v1/media/math/render/svg/857ff1b5b1d8e57a05870b8aee8612309bb5338e)
Formula for proximal operator courtisy of Wikipedia. Yeah yeah the notation is not what I used but I know you love formulas to take it or leave it. 

## Optimality Conditions
* At the minimum of a differentiable function the gradient must be zero. This is because if it wasn't zero, we could just move in the direction of *-gradient(f)*. 
* For non-differentiable convex functions, this optimality contidion isn't helpful because the minimum might be a kink where you can't differentiate. 
* Good thing we have our old friend the sub-gradient! Even if the the minimum point (x*) is a kink, 0 must be in the set of sub gradient's at x*.

## Proximal descent
Basically it works like this: 
1. Break f into two parts: g (the differentiable part) and h (the non-differentiable part).
2. Take a step along the gradient of g to minimize that part of the function
3. Use the proximal operator to take another step that reduces h while staying close to the point selected by (2)
4. Repeat (2) and (3) until the optimality condition is met. 


**TODO** intuitive derivation of optimality condition, proximal descent step

