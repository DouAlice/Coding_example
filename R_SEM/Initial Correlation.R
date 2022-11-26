Data$Scaled_Dep <- as.numeric(Data$DASS_3 + Data$DASS_5 + Data$DASS_10 + Data$DASS_13 + Data$DASS_16 + Data$DASS_17 + Data$DASS_21
+ Data$PHQ9_1 + Data$PHQ9_2 + Data$PHQ9_3 + Data$PHQ9_4 + Data$PHQ9_5 + Data$PHQ9_6 + Data$PHQ9_7 + Data$PHQ9_8 + 
    Data$PHQ9_9) 

Data$Scaled_Anx <- as.numeric(Data$DASS_1 + Data$DASS_2 + Data$DASS_4 + Data$DASS_6 + Data$DASS_7 + Data$DASS_8 + Data$DASS_9 + 
    Data$DASS_11 + Data$DASS_12 + Data$DASS_14 + Data$DASS_15 + Data$DASS_18 + Data$DASS_19 + Data$DASS_20 +  
    Data$GAD7_1 + Data$GAD7_2 + Data$GAD7_3 + Data$GAD7_4 + Data$GAD7_5 + Data$GAD7_6 + Data$GAD7_7) 

Data$Scaled_NA <- (Data$Scaled_Dep + Data$Scaled_Anx )/2
Data$Scaled_Worry <- Data$RNTQ_worry 
Data$Scaled_Brood <- Data$RTNQ_brood 
Data$Scaled_Inter <- Data$RNTQ_inter 
Data$Scaled_PF    <- Data$RNTQ_pf 
Data$Sum_RNTQ       <- Data$RNTQ_worry + Data$RTNQ_brood + Data$RNTQ_inter + Data$RNTQ_pf

Data$GAD <- (Data$GAD7_1 + Data$GAD7_2 + Data$GAD7_3 + Data$GAD7_4 + Data$GAD7_5 + Data$GAD7_6 + Data$GAD7_7)/7
Data$PHQ <- (Data$PHQ9_1 + Data$PHQ9_2 + Data$PHQ9_3 + Data$PHQ9_4 + Data$PHQ9_5 + Data$PHQ9_6 + Data$PHQ9_7 + Data$PHQ9_8 + 
    Data$PHQ9_9) /9
Data$D   <- (Data$DASS_3 + Data$DASS_5 + Data$DASS_10 + Data$DASS_13 + Data$DASS_16 + Data$DASS_17 + Data$DASS_21)/7
Data$S   <- (Data$DASS_1 + Data$DASS_6 + Data$DASS_8 + Data$DASS_11 + Data$DASS_12 + Data$DASS_14 + Data$DASS_18) /7
Data$A   <- (Data$DASS_2 + Data$DASS_4 + Data$DASS_7 + Data$DASS_9 + Data$DASS_15 + Data$DASS_19 + Data$DASS_20)/7
Data2 <- Data[c("GAD", "PHQ", "D", "S", "A")]
Data2$Worry_re = Data$RNTQ_2 + Data$RNTQ_9 + Data$RNTQ_10 + Data$RNTQ_11 + Data$RNTQ_20 + Data$RNTQ_21
Data2$Brooding_re = Data$RNTQ_1 + Data$RNTQ_14 + Data$RNTQ_15 + Data$RNTQ_16 + Data$RNTQ_18
Data2$Interference_re = Data$RNTQ_4 + Data$RNTQ_5 + Data$RNTQ_8 + Data$RNTQ_13 + Data$RNTQ_19 + Data$RNTQ_22
Data2$PF_re = Data$RNTQ_3 + Data$RNTQ_6 + Data$RNTQ_7 + Data$RNTQ_12 + Data$RNTQ_17    
mydata.cor2 = cor(Data2, method = c("pearson"), use = "complete.obs")
as.data.frame(mydata.cor2) 

library(openxlsx)
write_xlsx(as.data.frame(mydata.cor2), "cor2.xlsx")

view(mydata.cor2)

library("Hmisc")
res2 <- rcorr(as.matrix(Data2))


#view(Data[c("Scaled_Anx","Scaled_Dep", "Scaled_RNT")])

#reverse RNT
for (i in 6:27) {
  Data[,i] <- 7 - Data[,i]
}

Data$Worry_re = Data$RNTQ_2 + Data$RNTQ_9 + Data$RNTQ_10 + Data$RNTQ_11 + Data$RNTQ_20 + Data$RNTQ_21
Data$Brooding_re = Data$RNTQ_1 + Data$RNTQ_14 + Data$RNTQ_15 + Data$RNTQ_16 + Data$RNTQ_18
Data$Interference_re = Data$RNTQ_4 + Data$RNTQ_5 + Data$RNTQ_8 + Data$RNTQ_13 + Data$RNTQ_19 + Data$RNTQ_22
Data$PF_re = Data$RNTQ_3 + Data$RNTQ_6 + Data$RNTQ_7 + Data$RNTQ_12 + Data$RNTQ_17

Data$RNTQ_all = Data$Worry_re + Data$Brooding_re + Data$Interference_re + Data$PF_re
CData <- Data[c("Scaled_Anx","Scaled_Dep", "Scaled_NA", "Worry_re", "Brooding_re", 
                "Interference_re", "PF_re", "RNTQ_all")]
mydata.cor = cor(CData, method = c("pearson"), use = "complete.obs")
as.data.frame(mydata.cor)

write_xlsx(as.data.frame(mydata.cor), "C:\\Users\\hd199\\Documents\\2021S1 Thesis\\Pcor.xlsx")

CorData <- rcorr(as.matrix(CData))




CData = as.numeric(unlist(CData))

cocor(~Worry_re + Scaled_Anx | Worry_re + Scaled_Dep,
      CData)
