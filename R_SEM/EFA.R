library(tidyverse)      
library(psych)          # used to undertake the EFA and related analyses 
library(GPArotation)    # called by psych to run certain parts of the EFA 
library(readxl)
library(EFA.dimensions)
library(knitr)

Data1 <- Data[, c(33:39, 41:61, 81:89)]

parallel <-                # store results in 'parallel'
    psych::fa.parallel(      # use fa.parallel function from the psych package
        x = Data1 ,             # ** replace XXXX with the data to read in ! **
        fa = "pc",             # show the eigenvalues for extracted principal components
        quant = .95            # compare them to the 95th quantile of eigenvalues from simulated data
    )


obs_eg <- data.frame(parallel$pc.values)       # get the observed data out of parallel 
colnames(obs_eg) <- c('observed_eigenvalue')   # rename column for easy reading 
percentile_95 <- 
    apply(parallel$values,2,                     # calculate quantiles for simulated 
          function(x) quantile(x, .95))          # eigenvalues (not given 95th by default)
sim_eg <- data.frame(percentile_95)            # create data frame 
parallel_table <- cbind(obs_eg,sim_eg)         # join to two data frames
parallel_table <- 
    parallel_table %>%                           # make it easier to read 
    slice(1:24) %>%                              # drop some rows that aren't useful for this exercise
    mutate(component = c(1:24)) %>% 
    select(c(component, observed_eigenvalue, percentile_95))

kable(parallel_table) 
###############################################################################
two_factor <-
    fa(r = Data1,                     # ** replace XXXX with the data to read in ! **
       nfactors = 2,              # ** replace YYYY with the # of factors you want to extract **
       rotate = "oblimin",
       fm = "ml"                  
    )

loadings <- two_factor$loadings

print(loadings, cut = 0.3)
##############################################################################

three_factor <-
    fa(r = Data1,                     # ** replace XXXX with the data to read in ! **
       nfactors = 3,              # ** replace YYYY with the # of factors you want to extract **
       rotate = "oblimin",
       fm = "ml"                  
    )

loadings1 <- three_factor$loadings

print(loadings1, cut = 0.3)