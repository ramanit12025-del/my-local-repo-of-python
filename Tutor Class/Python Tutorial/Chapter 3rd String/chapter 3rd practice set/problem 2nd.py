# write a program to fill in a letter template given below with name and date
letter= '''Dear <|Name|>
            you are selected !
            <|Dated|> '''
print(letter.replace("<|Name|>","Raman").replace("<|Dated|>","18-08-2025"))
