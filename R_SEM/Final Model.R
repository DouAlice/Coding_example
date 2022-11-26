
# Compare fit statistics
compare_fits <- list()

compare_fits$fit_1a <- fit_1a
compare_fits$fit_1b <- fit_1b
compare_fits$fit_1c <- fit_1c
compare_fits$fit_2 <- fit_2
compare_fits$fit_3 <- fit_3
compare_fits$fit_4 <- fit_4
compare_fits$fit_5 <- fit_5
compare_fits$fit_6 <- fit_6
compare_fits$fit_7 <- fit_7
compare_fits$fit_8 <- fit_8
compare_fits$fit_9 <- fit_9
compare_fits$fit_10 <- fit_10

FitT <- round(sapply(compare_fits, fitmeasures, c("df","chisq", "cfi", "srmr", "rmsea")), 3)
write_xlsx(as.data.frame(FitT), "C:\\Users\\hd199\\Documents\\2021S1 Thesis\\Fitall1.xlsx")

#################################################################################

# SUB: 

model_1a <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect

'



# Allowing factors to correlate:
fit_1a <- sem(model = model_1a,             # Add your syntax (saved earlier) here
             data = Data,              # Specify your dataset name here
             estimator = "MLR",
             likelihood = "wishart",
             orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_1a, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_1a))
fitmeasures(fit_1a, c("df", "chisq", "cfi", "srmr", "rmsea"))

pred <- predict(fit_1a)

#################################################################################
#################################################################################

# SUB: 

model_1b <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

 
  # regressions
    
    RNT ~ Depression
    RNT ~ Anxiety
    Anxiety =~ Depression

'



# Allowing factors to correlate:
fit_1b <- sem(model = model_1b,             # Add your syntax (saved earlier) here
              data = Data,              # Specify your dataset name here
              estimator = "MLR",
              likelihood = "wishart",
              orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_1b, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_1b))
fitmeasures(fit_1b, c("chisq", "cfi", "srmr", "rmsea"))


#################################################################################

# SUB: 

model_1c <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Negative_Affect =~ DASS_D + PHQ9_total +  DASS_A + DASS_S + GAD_total

 
  # regressions
    
RNT ~ Negative_Affect

'



# Allowing factors to correlate:
fit_1c <- sem(model = model_1c,             # Add your syntax (saved earlier) here
              data = Data,              # Specify your dataset name here
              estimator = "MLR",
              likelihood = "wishart",
              orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_1c, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_1c))
fitmeasures(fit_1c, c("chisq", "cfi", "srmr", "rmsea"))

#################################################################################

# SUB: 

model_2 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect
    Sum_worry ~ Anxiety
    Sum_brooding ~ Depression

'



# Allowing factors to correlate:
fit_2 <- sem(model = model_2,             # Add your syntax (saved earlier) here
              data = RData,              # Specify your dataset name here
              estimator = "MLR",
              likelihood = "wishart",
              orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_2, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_2))
fitmeasures(fit_2, c("chisq", "cfi", "srmr", "rmsea"))

#################################################################################

# SUB: 

model_3 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect
    Sum_worry ~ Anxiety


'



# Allowing factors to correlate:
fit_3 <- sem(model = model_3,             # Add your syntax (saved earlier) here
              data = Data,              # Specify your dataset name here
              estimator = "MLR",
              likelihood = "wishart",
              orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_3, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_3))

fitmeasures(fit_3)
fitmeasures(fit_3, c("chisq", "cfi", "srmr", "rmsea"))
#################################################################################

# Interference to NA

model_4 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect
    Sum_interference ~ Negative_Affect


'



# Allowing factors to correlate:
fit_4 <- sem(model = model_4,             # Add your syntax (saved earlier) here
              data = Data,              # Specify your dataset name here
              estimator = "MLR",
              likelihood = "wishart",
              orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_4, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_4))
fitmeasures(fit_4, c("chisq", "cfi", "srmr", "rmsea"))

#################################################################################

# inter to dep 

model_5 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect
    Sum_interference ~ Depression

'



# Allowing factors to correlate:
fit_5 <- sem(model = model_5,             # Add your syntax (saved earlier) here
              data = Data,              # Specify your dataset name here
              estimator = "MLR",
              likelihood = "wishart",
              orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_5, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_5))
fitmeasures(fit_5, c("chisq", "cfi", "srmr", "rmsea"))


#################################################################################

# 

model_6 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
RNT ~ Negative_Affect
Sum_worry ~ Negative_Affect

'



# Allowing factors to correlate:
fit_6 <- sem(model = model_6,             # Add your syntax (saved earlier) here
              data = Data,              # Specify your dataset name here
              estimator = "MLR",
              likelihood = "wishart",
              orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_6, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_6))
fitmeasures(fit_6, c("chisq", "cfi", "srmr", "rmsea"))

fitmeasures(fit_6)

#################################################################################

# inter to ,Dep + worry

model_7 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect
    Sum_interference ~ Negative_Affect
    Sum_worry ~ Anxiety
    
'



# Allowing factors to correlate:
fit_7<- sem(model = model_7,            # Add your syntax (saved earlier) here
              data = Data,              # Specify your dataset name here
              estimator = "MLR",
              likelihood = "wishart",
              orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_7, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_7))
fitmeasures(fit_7, c("chisq", "cfi", "srmr", "rmsea"))


#################################################################################
#################################################################################

# SUB: 

model_8 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
  
      RNT ~ Negative_Affect
    Sum_interference ~ Depression
    Sum_worry ~ Anxiety

'



# Allowing factors to correlate:
fit_8 <- sem(model = model_8,             # Add your syntax (saved earlier) here
             data = Data,              # Specify your dataset name here
             estimator = "MLR",
             likelihood = "wishart",
             orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_8, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_8))
fitmeasures(fit_8, c("chisq", "cfi", "srmr", "rmsea"))























#################################################################################

# SUB: 

model_9 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect
    Sum_worry ~ Negative_Affect
    Sum_interference ~ Depression

'



# Allowing factors to correlate:
fit_9 <- sem(model = model_9,             # Add your syntax (saved earlier) here
             data = Data,              # Specify your dataset name here
             estimator = "MLR",
             likelihood = "wishart",
             orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_9, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_9))
fitmeasures(fit_9, c("chisq", "cfi", "srmr", "rmsea"))

#################################################################################

# SUB: 

model_10 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect
    Sum_worry ~ Negative_Affect
    Sum_interference ~ Negative_Affect


'



# Allowing factors to correlate:
fit_10 <- sem(model = model_10,             # Add your syntax (saved earlier) here
             data = Data,              # Specify your dataset name here
             estimator = "MLR",
             likelihood = "wishart",
             orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_10, "std", layout = "circle", sizeLat = 5)



kable(standardizedsolution(fit_10))
fitmeasures(fit_10, c("chisq", "cfi", "srmr", "rmsea"))






















model_11 <- '
  # measurement model

RNT =~ Sum_worry + Sum_brooding  + Sum_interference + Sum_pf

Depression =~ DASS_D + PHQ9_total 
Anxiety =~ DASS_A + DASS_S + GAD_total

Negative_Affect =~ Depression + Anxiety
 
  # regressions
    RNT ~ Negative_Affect
    Sum_worry ~ NA

'



# Allowing factors to correlate:
fit_11 <- sem(model = model_11,             # Add your syntax (saved earlier) here
             data = Data,              # Specify your dataset name here
             estimator = "MLR",
             likelihood = "wishart",
             orthogonal = FALSE)

# Plot the graph 
graph <- semPaths(fit_11, "std", layout = "circle", sizeLat = 5)



fitmeasures(fit_11, c("chisq", "cfi", "srmr", "rmsea"))

fitmeasures(fit_6)