# Mixed Effects Regression


### Linear models, fixed effects

Linear models express a linear relationship between some features `X_1, ..., X_n` and outcome `Y`:

```
Y ~ X_1 + X_2 + ... + X_n  + error
```

This model divides the world into two parts. 

1) There's the stuff we understand in a systematic way. This is the `X_i's`, aka the features/covariates. Our data consists of this information.
2) There's the stuff we don't understand. For the linear model above, we lump all of this into the random `error` term. 

Before we leave linear models we observe that the covariates have a "fixed" effect on `Y`, that is, regaurdless of the example we pick, `X_1` will act on `Y` the same way. It's effect on the explanitory variable is **fixed**.

### Mixed models, random effects

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


### Mixed models in R



### Mixed models in Python



### More reading

* http://www.bodowinter.com/tutorial/bw_LME_tutorial2.pdf
* http://ase.tufts.edu/gsc/gradresources/guidetomixedmodelsinr/mixed%20model%20guide.html

