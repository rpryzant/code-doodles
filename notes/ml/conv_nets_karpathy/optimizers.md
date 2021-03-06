https://www.youtube.com/watch?v=hd_KFJ5ktUc

* **parameter updates**
  * sgd is `-lerning_rate * gradient`
  * its not very good in practice, there's way better ones. why?
    * e.g. think of a loss function that's steep vertically but shallow vertically (big horizontal oval)
    * sgd will oscilate horizontally and move too slowly in x direction
  * step 1: **momentum**
    * ball rolling around. velocity gets multiplied by accelleration
    * slowly build up velocity vector `v = mu * v - lr * grad`, then apply that `v`  (mu is a hyperparam)
    * generally improves convergence 
  * next: **nesterov momentum**
    * make momentum/gradient steps seperate (there's really two parts to teh above step), take momentum step first
    * has nicer theoretical properties and generally works a little better because of one-step lookahead-like behavior given by breaking it into two steps
  * **adagrad**
    * `cache += grad**2`
    * `x += - lr * grad / (sqrt(cache) + 1e-7) `
    * cache builds up *second moements* of gradients
    * every dimension of parameter space has its *own learning rate*
    * so steep/shallow disparities are accounted for!
    * problem: over time, cache keep=s growing, so denominator keeps growing, so you eventually decay to basically no movement
  * **rmsprop**
    * fixes adagrad problem by making cache leaky
    * fun fact: it wasn't released in a paper, but in a slide form a slideshow
    * `cache = decay * cache + (1 - decay) * grad ** 2`
    * then same weight update as adagrad
  * **adam**: rmsprop + momentum
    * kind of like rmsprop + momentum
    * current best bet! (but not always the case)

* second-order approximations
  * use slope + HESSIAN (2nd derivative)
  * can then use newton methods (use hessian + grad to jump directly to soln)
  * nice because fast convergence, 
  * bad because hessian is HUGE (size of num params * size of num params) and needs to be inverted


* **model ensembles**
  * train multiple models, average predictions at test time, always get a little big of performance bost (~2%)
  * can also get slight boost from averaging multiple checkpoints of single model


* **dropout**
  * regularization scheme
  * in forward pass, randomly zero out some units, don't let them fire
  * think of it like training a large ensemble of models (powerset of units)
  *  scale each training activation by p because expected value of each neuron activation is (p)*(what it was without dropout). without this treatment neurons would break during test because they haven't seen activations so strong before
  * at test time, don't drop units



