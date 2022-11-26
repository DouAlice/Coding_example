
library(tidyverse)   # Data wrangling 
library(lavaan)      # CFA/SEM
library(semPlot)     # Plotting SEM diagrams
library(psych)       # Descriptive stats
library(skimr)       # Descriptive stats 
library(semTools)    # Skew and kurtosis 
library(knitr) 
library(REdaS)



Data$GAD <- (Data$GAD7_1 + Data$GAD7_2 + Data$GAD7_3 + Data$GAD7_4 + Data$GAD7_5 + Data$GAD7_6 + Data$GAD7_7)
Data$PHQ <- (Data$PHQ9_1 + Data$PHQ9_2 + Data$PHQ9_3 + Data$PHQ9_4 + Data$PHQ9_5 + Data$PHQ9_6 + Data$PHQ9_7 + Data$PHQ9_8 + 
                  Data$PHQ9_9) 
Data$D   <- (Data$DASS_3 + Data$DASS_5 + Data$DASS_10 + Data$DASS_13 + Data$DASS_16 + Data$DASS_17 + Data$DASS_21)
Data$S   <- (Data$DASS_1 + Data$DASS_6 + Data$DASS_8 + Data$DASS_11 + Data$DASS_12 + Data$DASS_14 + Data$DASS_18) 
Data$A   <- (Data$DASS_2 + Data$DASS_4 + Data$DASS_7 + Data$DASS_9 + Data$DASS_15 + Data$DASS_19 + Data$DASS_20)
Data$Worry <- Data$Sum_worry / 6
Data$Brood <- Data$Sum_brooding /5
Data$It <- Data$Sum_interference / 6
Data$Pf <- Data$Sum_pf / 5


DD <- Data[c('GAD','PHQ','D','S','A','Worry','Brood','It','Pf')]

DD <- Data[c('GAD','PHQ','D','S','A')]
DD <- DD[-c(274,330),]


# Test Multivariate Kurtosis and Skew 

mardia(RD,na.rm = TRUE, plot=TRUE)

mardia(DD [,6:9],na.rm = TRUE, plot=TRUE)


RD <- Data[c('RNTQ_worry','RTNQ_brood','RNTQ_inter','RNTQ_pf')]

RD <- Data[c('GAD_total','PHQ9_total','DASS_S','DASS_A','DASS_D')]

# Univariate and multivariate kurtosis and skew - similar to AMOS 'Assessment of Normality'. 
 describe(RD) %>% 
    as_tibble() %>% 
    mutate(variable = rownames(describe(RD)),
           across(where(is.numeric), round, 3)) %>% 
    select(variable, min, max, skew, kurtosis) %>% 
    rbind(c(variable = "Multivariate", 
            min = NA, 
            max = NA, 
            skew = round(as.numeric(mardiaSkew(RD)[1]), 3), 
            kurtosis = round(as.numeric(mardiaKurtosis(RD)[1]), 3)
    )) %>% 
    kable()


write_xlsx(RD, "C:\\Users\\hd199\\Documents\\2021S1 Thesis\\AppendixRD.xlsx")


pairs(~DASS_D+ DASS_A + DASS_S + PHQ9_total + GAD_total,data=Data,
      main="Simple Scatterplot Matrix")

plot(Data$RTNQ_brood,Data$RNTQ_worry,
     xlab="Brooding", ylab="Worry", pch=19)
abline(v=21, col="blue")
abline(h=25, col="blue")

ggplot(Data, aes(x=RTNQ_brood, y=RNTQ_worry)) + geom_point() + labs(
  x = "Brooding", y = "Worry"
) + theme_classic() 


is.na(X1)

bart_spher(DD, use = "complete.obs")


KMO_results <- KMO(DD)
KMO_results$MSA

KMO_results$MSAi

KMO_results$Image












for (i in 1:658) {
    if (is.na(C[i,1])) 
    { C[i,1] = mean(as.numeric(C[i,1]), na.rm = TRUE)}
}
for (i in 1:658) {
    if (is.na(C[i,2])) 
    { C[i,2] = mean(as.numeric(C[i,2]), na.rm = TRUE)}
}
for (i in 1:658) {
    if (is.na(C[i,3])) 
    { C[i,3] = mean(as.numeric(C[i,3]), na.rm = TRUE)}
}

for (i in 1:658) {
    if (is.na(C[i,4])) 
    { C[i,4] = mean(as.numeric(C[i,4]), na.rm = TRUE)}
}
for (i in 1:658) {
    if (is.na(C[i,5])) 
    { C[i,5] = mean(as.numeric(C[i,5]), na.rm = TRUE)}
}



for (i in 1:658) {
    if (is.na(R[i,1])) 
    { R[i,1] = mean(as.numeric(R[i,1]), na.rm = TRUE)}
}
for (i in 1:658) {
    if (is.na(R[i,2])) 
    { R[i,2] = mean(as.numeric(R[i,2]), na.rm = TRUE)}
}
for (i in 1:658) {
    if (is.na(R[i,3])) 
    { R[i,3] = mean(as.numeric(R[i,3]), na.rm = TRUE)}
}

for (i in 1:658) {
    if (is.na(C[i,4])) 
    { R[i,4] = mean(as.numeric(R[i,4]), na.rm = TRUE)}
}
for (i in 1:658) {
    if (is.na(C[i,5])) 
    { R[i,5] = mean(as.numeric(R[i,5]), na.rm = TRUE)}
}






