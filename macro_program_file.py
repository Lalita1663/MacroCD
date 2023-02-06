#SP LAB
#MINI PROJECT
#4 MARCH 2017 -- 14 MARCH 2017
#LALITA PUROHIT 2015UCP1663
# AND NIDHI JANGIR 2015UCP1684
# BATCH B-7,8




# global part --1 START

import sys

if(len(sys.argv)==3):

  filename=str(sys.argv[1])
  extension=filename.split(".")
  extension=extension[1]                     # NEED FILE EXTENTION FOR RECOGNIZING COMMENT PART
  
  print_or_change=int(sys.argv[2])     # 1==print the o/p 
                                       # 2==change in  file

  
  
# global part --1 END



#function -- 1 START

def parameterized_macro(par1,par2,temp1):

      
        position=par1.find('(')
        templet1=par1[:position+1]
        templet2=par1[position+1:]
        
        endargv=templet2.find(')')
        templet2=templet2[:endargv]+','    # NOW templet2 = pr1,pr2,pr3,...... ,  " Formal parameters "
        
        
        no_of_calls=temp1.count(templet1)
        
        for j in range(no_of_calls):
          position=par1.find('(')
          templet1=par1[:position+1]
          templet2=par1[position+1:]
        
          endargv=templet2.find(')')
          templet2=templet2[:endargv]+','
        
        
        
        
          position=temp1.find(templet1)    # NOW COPY THE ELEMENTS FROM '(' TO ')' 
        
          forargv=temp1[position:].strip()
          endargv=forargv.find('(')
          forargv=forargv[endargv+1:]
          
          endargv=forargv.find(')')
          forargv=forargv[:endargv] +','       # NOW forargv = pr1,pr2,pr3,...... ,
       
          
          
          endargv=temp1.find(')',position)                                 # TO REMOVE FUNCTION CALL
          temp1=temp1.replace(temp1[position:endargv+1],"$@$@$")
        
        
        
          count_commas=forargv.count(',')+1       # CC=NO. OF PARAMETERS
          temp_par2=par2
          for i in range(count_commas):                   # create line for replacement
                comma1=templet2.find(',')
                argv=templet2[:comma1]
                
                
                comma2=forargv.find(',')
                newargv=forargv[:comma2]
                
                
                if argv in (par2):
                        par2=par2.replace(argv,newargv)
                      
                        
                        
                
                argv=templet2[:comma1+1]
                newargv=forargv[:comma2+1]
                templet2=templet2.replace(argv,"")   # parameters removed after storing in argv from templet2
                
                forargv=forargv.replace(newargv,"")
        
        
          temp1=temp1.replace("$@$@$",par2)
          par2=temp_par2
        
        return(temp1)

# Function --1 END




# Function --2 START

def Change_in_file(temp1):   # to replace o/p with i/p
  fp=open(filename,"w")
  fp.write(temp1)         
  fp.close()
  
# Function --2 END






# Function --3 START

# global part --2 START

remover=[]
dlist=[]

# global part --2 ENDS

def REMOVE_COMMENTS_OF_PROGRAM(c):
      d=''
      if(extension=="c"):                         # then remove // and /*....*/ parts 
          for i in range (len(c)):
                if "//" in c:
                      
                       remover1=c.find("//")
                       remover.append(remover1)       # LIST OF POSITONS OF COMMENTS
                      
                       remover2=c.find("\n",remover1)
                       
                       replacement=(c[remover1:remover2])
                       d=c[remover1:remover2]
                       dlist.append(d)                       #  LIST OF ALL COMMENTS
                       c=c.replace(c[remover1:remover2],("???????"+str(remover1)))
                     
                       
                       
                       
                elif "/*" in c :
                      
                       remover1=c.find("/*")
                       remover.append(remover1)       # LIST OF POSITONS OF COMMENTS
                      
                       remover2=c.find("*/",remover1)
                       
                       replacement=(c[remover1:remover2])
                       d=c[remover1:remover2]
                       dlist.append(d)                       #  LIST OF ALL COMMENTS
                       c=c.replace(c[remover1:remover2],("???????"+str(remover1)))                
                
                
                
                
      
      elif(extension=="py"):
          for i in range (len(c)):
                if "#" in c:      
                       remover1=c.find("#")
                       remover.append(remover1)       # LIST OF POSITONS OF COMMENTS
                      
                       remover2=c.find("\n",remover1)
                       
                       replacement=(c[remover1:remover2])
                       d=c[remover1:remover2]
                       dlist.append(d)                       #  LIST OF ALL COMMENTS
                       c=c.replace(c[remover1:remover2],("???????"+str(remover1)))    
                       
                           

      
      elif(extension=="asm"):
         for i in range (len(c)):
                if ";" in c:
                      
                       remover1=c.find(";")
                       remover.append(remover1)       # LIST OF POSITONS OF COMMENTS
                      
                       remover2=c.find("\n",remover1)
                       
                       replacement=(c[remover1:remover2])
                       d=c[remover1:remover2]
                       dlist.append(d)                       #  LIST OF ALL COMMENTS
                       c=c.replace(c[remover1:remover2],("???????"+str(remover1)))
                     
                       
      
      
      
      else:
         print("This preprocessor doesn't support the file you given ")
  
      return(c)
         
         
# Function --3 END


# FUNCTION --4 START
def REMOVE_COMMENTS_OF_MACRO_DEFINITION(c,extension):
  
        defcount=c.count("$def")

        if(defcount==0):  
            return(c)
        else:
        
           if(extension=="c"):                        # then remove //...\n  and /*....*/ part of definition
              for i in range (defcount):
        
                start=0
                end=0
                for j in range (defcount):
        
                        start=c.find("$def",end)
                        end=c.find("@end",start)
               
                        if "//" in c[start:end]:
                               comment_count=c[start:end].count("//")
                               
                               for k in range(comment_count):                 # for more then one comment        
                                    remover1=c.find("//",start)
                                    remover2=c.find("\n",remover1)
                                    checkend=c[remover1:remover2]
                     
                                    if "@end" in checkend:
                                          c=c.replace(c[remover1:remover2],""+"@end")
                                    else:
                                          c=c.replace(c[remover1:remover2],"")
 
                                               
                        if "/*" in c[start:end]:
                               comment_count=c[start:end].count("/*")
                               
                               for k in range(comment_count):          # for more then one comment             
                                    remover1=c.find("/*",start)
                                    remover2=c.find("*/",remover1)
                                    checkend=c[remover1:remover2]
                      
                                    c=c.replace(c[remover1:remover2+2],"")
                                                                  
           elif(extension=="py"):                        # then remove #...\n part of definition
              for i in range (defcount):
        
                start=0
                end=0
                for j in range (defcount):
        
                        start=c.find("$def",end)
                        end=c.find("@end",start)
               
                        if "#" in c[start:end]:
                               comment_count=c[start:end].count("#")
                               
                               for k in range(comment_count):          # for more then one comment                
                                    remover1=c.find("#",start)
                                    remover2=c.find("\n",remover1)
                                    checkend=c[remover1:remover2]
                      
                                    if "@end" in checkend:
                                            c=c.replace(c[remover1:remover2],""+"@end")
                                    else:
                                            c=c.replace(c[remover1:remover2],"")

           elif(extension=="asm"):                      # then remove ;.......\n  part of definition
              for i in range (defcount):
        
                start=0
                end=0
                for j in range (defcount):
        
                        start=c.find("$def",end)
                        end=c.find("@end",start)
               
                        if ";" in c[start:end]:
                               comment_count=c[start:end].count(";")
                               
                               for k in range(comment_count):            # for more then one comment 
                                    remover1=c.find(";",start)
                                    remover2=c.find("\n",remover1)
                                    checkend=c[remover1:remover2]
                     
                                    if "@end" in checkend:
                                            c=c.replace(c[remover1:remover2],""+"@end")
                                    else:
                                            c=c.replace(c[remover1:remover2],"")
                                                                    
           else:
             print("WARNING: This preprocessor doesn't support the file you given ")#only .c .py and .asm files are accepted as i/p
  
        return(c)                

# FUNCTION--4 END





# FUNCTION --5 START


def REPLACE_TEMPLETS_WITH_EXPENSION(temp1,defcount):    # block for excluding macro definition from program

  for i in range (defcount):



        start=temp1.find("$def")   
        end=temp1.find("@end")
       
        
        par=temp1.split("$def")
        
        par=par[1].split("@end")   
     
        
        par=par[0].strip()  # par== templet + expension 
        sep=par.find(" ")   # no space alowed in templet bcoz " " is the only saprater of templet and expension
        
       
        
        c=temp1[:start]
        c=c+temp1[end+4:]    # remove Macro Definition
        temp1=c
      
        
        
        par1=par[:sep].strip()    #Templet
        par2=par[sep:].strip()     # expension
    
        
        if ((( '(' in par1) and (')' in par1))is True):   #if () in Templet that denotes to parameterized macro
             temp1=parameterized_macro(par1,par2,temp1)   
             
        
        
        elif(par2[0]=='(' and par2[len(par2)-1]==')'):    # if () in expension then Solve by this way
                par2=par2.replace("(","")
                par2=par2.replace(")","")
            
                p1p=temp1.find(par1)
                nop1=temp1.count(par1)
                
                for i in range (nop1):
                  if((((temp1[p1p+len(par1)]>='A' and temp1[p1p+len(par1)]<='Z') or (temp1[p1p+len(par1)]>='a' and temp1[p1p+len(par1)]<='z') ) or ((temp1[p1p-1]>='A' and temp1[p1p-1]<='Z') or (temp1[p1p-1]>='a' and temp1[p1p-1]<='z') )) is not True):
                              
                                 temp1=temp1.replace(par1, par2) 
                  


        else:                                             # else solve by this way
                p1p=temp1.find(par1)
                nop1=temp1.count(par1)
                
                for i in range (nop1):
                  if((((temp1[p1p+len(par1)]>='A' and temp1[p1p+len(par1)]<='Z') or (temp1[p1p+len(par1)]>='a' and temp1[p1p+len(par1)]<='z') ) or ((temp1[p1p-1]>='A' and temp1[p1p-1]<='Z') or (temp1[p1p-1]>='a' and temp1[p1p-1]<='z') )) is not True):
                               
                                 temp1=temp1.replace(par1, par2) 
                


# temp1 = program excluding macro definition
  return(temp1)
  

# FUNCTION --5 END





# FUNCTION --6 START


def ADD_COMMENT_OF_PROGRAM_AGAIN(remover,dlist,c):

  for i in range (len(dlist)):
                if ( "???????"+str(remover[i]) in c) :
                   c=c.replace(("???????"+str(remover[i])),dlist[i])
  return(c)


# FUNCTION --6 END


# FUNCTION --7 START


def IF_ELSE_SOLUTION(c):



  findif=c.find("$if")      
  findfirstendif=c.find("$endif")

  conditionend=c[findif+3:].find("]")
  toadd=c.find(c[findif+3])
  temp=c[findif+3:]
  temp=temp[1:conditionend]

  result=eval(temp)         
  
  no_of_elif=c[findif:findfirstendif].count("$elif")
  no_of_else=c[findif:findfirstendif].count("$else")

  if(no_of_elif==0 and  no_of_else==0):
 
   
  # if condition==TRUE
   if(result==True):  #then keep only code of if
      
       c=c.replace(c[findif:findfirstendif+6],c[conditionend+toadd+1:findfirstendif])
   elif(result==False):
     
       c=c.replace(c[findif:findfirstendif+6],"")
   
  elif(no_of_elif==0 and  no_of_else==1):
       
       no_of_else=c[findif:findfirstendif].find("$else")   #here  no_of_else==position of else
       toadd1=c.find(c[findif])
          
       if(result==True):
         # c[conditionend+toadd+1:]   # from ]......EOF
          #(c[findif:findfirstendif+6]) #complete block of if-else
         
          c=c.replace(c[findif:findfirstendif+6],c[conditionend+toadd+1:no_of_else+toadd1])
         
       elif(result==False):
           
          c=c.replace(c[findif:findfirstendif+6],c[no_of_else+toadd1+5:findfirstendif])  


  elif(no_of_elif==1 and  no_of_else==1):
       
          position_of_elif=c[findif:findfirstendif].find("$elif")   #here  position of elif
          toadd1=c.find(c[findif])
          
          if(result==True):          
                    c=c.replace(c[findif:findfirstendif+6],c[conditionend+toadd+1:position_of_elif+toadd1])
          else:
            
                  
                  position_of_elif=c[findif:findfirstendif].find("$elif")   #here is first position of elif
                  toadd1=c.find(c[findif])
                  
                  conditionend=c.find("]",position_of_elif+toadd1)
                 
                  
                  temp=c[position_of_elif+6+toadd1:conditionend]
                  elif_result=eval(temp)
                 
                  if(elif_result==True):
                       
                         no_of_else=c[findif:findfirstendif].find("$else")   #here  no_of_else==position of else
                         toadd1=c.find(c[findif])                            
                         c=c.replace(c[findif:findfirstendif+6],c[conditionend+1:no_of_else+toadd1]) 
                  else:
                         no_of_else=c.find("$else")
                         c=c.replace(c[findif:findfirstendif+6],c[no_of_else+5:findfirstendif])                          
                      
  return(c)                         
                         



# FUNCTION --7 END

# FUNCTION --8 START

def IF_SOLUTION(c,choice):



  findif=c.find("$if")
  conditionend=c.find("]")
  temp=c[findif+4:conditionend]  
 
  
  result=eval(temp)  
  find_endif=c.find("$endif")    # because the first endif
  find_elif=c.find("$elif")
  find_else=c.find("$else")
  
  
 
  if(result==True):  
       
     if(find_elif!= -1):     # if another elif is present
       temp=c[conditionend+1:find_elif]
       
       
     elif(find_elif== -1 and find_else==-1):     # if no elif and no else
       temp=c[conditionend+1:find_endif]
       

     elif(find_elif== -1 and find_else!=-1):     # if no elif and  else
       temp=c[conditionend+1:find_else]
       
       
  elif(result==False):
         
     if(find_elif!= -1):     # if another elif is present

       temp=c[find_elif:]   #send
       
       
     elif(find_elif== -1 and find_else==-1):     # if no elif and no else
     
       temp=''
       

     elif(find_elif== -1 and find_else!=-1):     # if no elif and  else
       temp=c[find_else+5:find_endif]
  if(choice==1):         
     
     return(temp)
     
  else:
     return(result)  

# FUNCTION --8 END


# FUNCTION --9 START

def EVAL_elif(block):
     

  findelif=block.find("$elif")
  conditionend=block.find("]")
  temp=block[findelif+6:conditionend]  
  result=eval(temp)  
  find_endif=block.find("$endif")    # because the first endif
  find_next_elif=block.find("$elif",findelif+6)
  find_else=block.find("$else")
  
  if(result==True):       
     if(find_next_elif!= -1):     # if another elif is present
       temp=block[conditionend+1:find_next_elif]
       
       
     elif(find_next_elif== -1 and find_else==-1):     # if no elif and no else
       temp=block[conditionend+1:find_endif]
       

     elif(find_next_elif== -1 and find_else!=-1):     # if no elif and  else
       temp=block[conditionend+1:find_else]
      

  else:    
     
     if(find_next_elif!= -1):     # if another elif is present
          find_next_elif=block.find("$elif",findelif+6)         
          temp=EVAL_elif(block[find_next_elif:])
          return(temp)
       
       
     elif(find_next_elif== -1 and find_else==-1):     # if no elif and no else
       temp=''

     elif(find_next_elif== -1 and find_else!=-1):     # if no elif and  else
       temp=block[find_else+5:find_endif]
       
       
  return(temp)
     
# FUNCTION --9 END

# FUNCTION --10 START

def GO_TO_IF_ELSE(c):
  countif=c.count("$if")     
  for i in range(countif):   # if more then one blocks are present
    if(countif!=0):           # loop termination condition
      result=IF_SOLUTION(c,2)       #of $if[]
      if(result==True):               # is True then  
          temp=IF_SOLUTION(c,1)         # temp= code for c
        
      else:               
      
        temp=IF_SOLUTION(c,1)                 # take code excluded $if Completely
        if ((("$elif" in temp) and("$else" in temp))is True):    
                temp=EVAL_elif(temp)    # if $elif and $else present then evaluate that part and sore in tamp
      findif=c.find("$if")
      findend=c.find("$endif")
      c=c.replace(c[findif:findend+6],temp)    #replace the complete one block of $if....$endif with temp "The result"
  return(c)    # and return c i.e. o/p
    
# FUNCTION 10 END


# MAIN() -- START

if(len(sys.argv)!=3):
  print("Give one input file and one choice 1 to print o/p 2 to chage file as o/p file")
elif(((print_or_change==1 )or (print_or_change==2))is False):
  print("GIVE CHOICE    1 --to print the output / 2 -- to chage  file as output file")  
else:
  file=open(filename,"r") 
  c=file.read()   #store file in variable c
  file.close()

   

  if((extension=='c' or extension=='py' or extension=='asm' ) is False):
     print("ONLY .c .py OR .asm FILES ALLOWED")
     #Change_in_file(c)
     #print(c)

  else:
    c=REMOVE_COMMENTS_OF_PROGRAM(c)    # if all definitions present within the comments ***

    defcount=c.count("$def")    # macro definition count
    countif=c.count("$if")     # if-else definition count

    if(defcount==0):      # if no macro definition then return from here
        if(countif==0):               # and no $if in program thrn return
            c=ADD_COMMENT_OF_PROGRAM_AGAIN(remover,dlist,c)  
            if(print_or_change==1):
                   print(c)    #                                                      EITHER PRINT THE O/P
            elif(print_or_change==2):
                   Change_in_file(c)   #                                           OR CHANGE IN FILE
        else:
          c=GO_TO_IF_ELSE(c)       # but if $if is present then first solve it out
          c=ADD_COMMENT_OF_PROGRAM_AGAIN(remover,dlist,c) # as program name says 
          if(print_or_change==1):
                   print(c)    #                                                         EITHER PRINT THE O/P
          elif(print_or_change==2):
                   Change_in_file(c)  #                                                       OR CHANGE IN FILE


    else:
      c=ADD_COMMENT_OF_PROGRAM_AGAIN(remover,dlist,c)      # *** To begin with the Whole program

      c=REMOVE_COMMENTS_OF_MACRO_DEFINITION(c,extension)    # remove these comments permanently
      c=REMOVE_COMMENTS_OF_PROGRAM(c)                       
      # remove comments other then macro definition and store in dlist and remover so that they can be added further
      c=REPLACE_TEMPLETS_WITH_EXPENSION(c,defcount)  # COMPLETE CODE WITHOUT COMMENTS
  
      # first do all work of $def
      # now $if starts
      if(countif!=0):     # but only if there is any defition for $if
         c=GO_TO_IF_ELSE(c)    # solve if-else completely
      c=ADD_COMMENT_OF_PROGRAM_AGAIN(remover,dlist,c) 
               
      if(print_or_change==1):
                   print(c)    #                                                         EITHER PRINT THE O/P
      elif(print_or_change==2):
                   Change_in_file(c) #                                                 OR CHANGE IN FILE

# MAIN() -- ENDS



#  10 FUNCTIONS
#  2 global declaration     
#  1 MAIN() 





