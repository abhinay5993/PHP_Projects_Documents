from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for

'''Insitialize the flask App..'''
appObj = Flask(__name__)
print("\nValue off App Obj : ", appObj)


@appObj.route('/home/<testData>')
def launcher(testData):
    return ("Hey!! user welcome to Flask :  "+render_template('home.html', inpData=testData))


@appObj.route('/myTestNewController')
def caratLaneApp():
    return ("\nWelcome to App Team..."+render_template('clisting.html'))

@appObj.route('/product')
def product():
    print("\nRedirect to another Controller through redirect(url_for('caratLaneApp')) --> methode by passing another methode name..")
    return redirect(url_for('caratLaneApp'))

if __name__ == '__main__':
    '''Inside the main if '''
    appObj.run(debug=True, port=5993)
    print("\nAfter the If condition!!...")
