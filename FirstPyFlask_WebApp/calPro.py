from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask import request

'''Insitialize the flask App..'''
appObj = Flask(__name__)
print("\nValue off App Obj : ", appObj)

@appObj.route('/myAccountDetails',methods=['GET','POST'])
def getProfileData():
    if request.method == 'POST':
               emailData_var = request.form['mail_data']
               pwdData_var = request.form['pass_enc']
               userName_var = request.form['uid_name']
               num1_var = float(request.form['x_val'])
               num2_var = float(request.form['y_val'])
               sumVal = num1_var+num2_var
               subVal = num1_var-num2_var
               prodVal = num1_var*num2_var
               quoVal = num1_var/num2_var
               reminVal = num1_var % num2_var
               return render_template('profileCalInfo.html',emailData_var=emailData_var, pwdData_var=pwdData_var, sumVal=str(sumVal), subVal=str(subVal), prodVal=str(prodVal), quoVal=str(quoVal), reminVal=str(reminVal))
    return render_template('clisting.html')


if __name__ == '__main__':
    '''Inside the main if '''
    appObj.run(debug=True, port=5993)
    print("\nAfter the If condition!!...")
