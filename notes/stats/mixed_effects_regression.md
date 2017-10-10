# Mixed Effects Regression


### Linear models, fixed effects

Linear models express a linear relationship between some features `X_1, ..., X_n` and outcome `Y`:

```
Y ~ X_1 + X_2 + ... + X_n  + error
```

This model divides the world into two parts. 

1) There's the stuff we understand in a systematic way. This is the `X_i's`, aka the features/covariates. Our data consists of this information.
2) There's the stuff we don't understand. For the linear model above, we lump all of this into the random `error` term. 

Before we leave linear models we observe that the covariates have a "fixed" effect on `Y`, that is, regaurdless of the data point we pick, `X_1` will be affecting `Y` in the same way. It's effect on the outcome variable is **fixed**.

### Mixed models, random effects

#### Random intercepts

The goal of mixed effects regression is to give more structure to the `error` term in a principled way. We do so by adding in one or more categorical "random effect" variables to the model, and assuming a different "baseline" outcome and error term for each level of these variables. In other words, we introduce a bunch of categorical variables, and give each level of these variables its own intercept.


```
Y ~ X_1 + X_2 + ... + X_n + (1 | random_effect_1) + ... + (1 | random_effect_k) + error

(this notation is coming from R)
```


**A random effect is a confound which divides the data into subsets, and in each subset this variable acts on `Y` in a different way**. 

For example, let's say you recorded a bunch of men and women and are attempting to predict politeness from vocal pitch. `pitch` is certainly a fixed effect; variations in pitch are predictive of `politeness` regaurdless of interview subject. But there are also the confounding factors of `gender` and `situation`, which likely affects pitch but isn't really related to politeness (aka it doesn't have a fixed effect on politeness).

```
              |
              |  men
              |
average pitch |
              |        women
              |
               _____________
                  subjects

```

So we introduce `gender` as a random effects, thereby assuming that these groups have different baseline vocal pitches and modeling these groups accordingly. 

```
politeness ~ pitch + (1 | gender) + error
```

#### Random slopes

One advanced note for the 1337 h4Xors out there. 

Let's reconsider our `politeness ~ pitch + (1 | gender)` example. What if men not only have a lower baseline pitch, but also _raise their pitch less_ to indicate politeness? This means that the fixed effect `pitch` acts on the response `politeness` _differently_ under each treatment of the random effect. Seperate male/female intercepts won't cut it this time. We also need seperate slopes. Fortunately, we can do this with the following R-style notation:

```
politeness ~ pitch + (1 + pitch | gender) + error
```

### Mixed models in R

Use package llmer 
* [paper](https://cran.r-project.org/web/packages/lme4/vignettes/lmer.pdf)
* [documentation](https://www.rdocumentation.org/packages/lme4/versions/1.1-13/topics/lmer).

If you have variables `Y`, `X`, and `Confound` (categorical) in your dataframe `mydata`:
```
model = lmer(Y ~ X + (1 | Confound), data=mydata, REML=FALSE)

summary(model)    # model summary
coef(model)       # model coefficients

predict(model, myTestData)    # inference -- TODO FIGURE THIS OUT
```

Note that `REML=False` tells the system to use a maximum likelihood objective when training.

L1 Regularized implementations:
* [[1]](https://cran.r-project.org/web/packages/lmmlasso/lmmlasso.pdf)
* [[2]](https://cran.r-project.org/web/packages/glmmLasso/glmmLasso.pdf)


### Mixed models in Python


```
from rpy2.robjects import r, pandas2ri
import pandas as pd

pandas2ri.activate()

df = {
  'A': [1, 2, 3],
  'B': [4, 5, 6],
  'C':[7,8,9]},
  index=[1, 2, 3])}

r_dataframe = pandas2ri.py2ri(df)
rpy2.robjects.globalenv['dataset'] = r_dataframe

result = rpy2.robjects.r('''
      fit=lmer(A ~ A + B + (1 | C), data=dataset)
''')
rpy2.robjects.globalenv['result'] = result

...
TODO

```


### More reading

* http://www.bodowinter.com/tutorial/bw_LME_tutorial2.pdf
* http://ase.tufts.edu/gsc/gradresources/guidetomixedmodelsinr/mixed%20model%20guide.html

