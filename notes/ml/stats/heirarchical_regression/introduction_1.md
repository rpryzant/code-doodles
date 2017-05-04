https://www.youtube.com/watch?v=2w7Q4Wjn1uM

* should be used when data are "clustered", i.e., workers are nested into firms, which themselves are nested into regions
* error assumptions are violated
  * obs are no longer indep, and are correlated within clusters
  * each cluster has different sample sizes (and thus varience)
  * effect of predictors might be different on each cluster (different slopes might be appropriate)
* nieve solutions
  * aggregate everything (dumb for obvious reaons)
    * ex: fit to cluster means
    * ex: fitting line through nothing
  * make cluster feature, and include that in the regression model (assums there's more data than there is, violates indep assump)
  * run model seperatly for each group (now have small samples, tests are underpowered)
* visualized: two seperate line
* derivation
  * start with Y_ij = alpha_0j + B_1j X + eij
    * we can now have a sperate alpha/B for each group
    * make each param (alpha / beta) a linear function itself
    * but now error terms aren't indep
      * error terms commmon to all members of same cluster
      * size of these terms depends on X (b/c cluster)
   * mini regressions to estimate slopes/intercepts
* naming
  * called 3 things: multilevel mode, mixed effects model, random effects model = ALL THE SAME THING
  
* *random effects*
  * parts of the model aren't estimated directly, but described by their variences/covariences
  * best when multiple observations are nested in a single person

* more lectures!!