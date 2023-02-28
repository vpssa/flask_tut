from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/math',methods=['POST'])
def math_oper():
    if(request.method=='POST'):
        oper=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if(oper=='add'):
            r=num1+num2
            result= "the sum of"+ str(num1) +" and "+str(num2)+" is "+r
        if(oper=='subtract'):
            r=num1-num2
            result= "the subtraction of"+ str(num1) +" and "+str(num2)+" is "+r
        if(oper=='multiply'):
            r=num1*num2
            result= "the multiplication of"+ str(num1) +" and "+str(num2)+" is "+r
        if(oper=='divide'):
            r=num1/num2
            result= "the division of"+ str(num1) +" and "+str(num2)+" is "+r
        print(result)
        return render_template("results.html",result=result)



# @app.route('/postman_action',methods=['POST'])
# def math_oper1():
#     if(request.method=='POST'):
#         oper=request.json['operation']
#         num1=int(request.json['num1'])
#         num2=int(request.json['num2'])
#         if(oper=='add'):
#             r=num1+num2
#             result= "the sum of"+ str(num1) +" and "+str(num2)+" is "+r
#         if(oper=='subtract'):
#             r=num1-num2
#             result= "the subtraction of"+ str(num1) +" and "+str(num2)+" is "+r
#         if(oper=='multiply'):
#             r=num1*num2
#             result= "the multiplication of"+ str(num1) +" and "+str(num2)+" is "+r
#         if(oper=='divide'):
#             r=num1/num2
#             result= "the division of"+ str(num1) +" and "+str(num2)+" is "+r

#     return jsonify("result.html",result=result)


if __name__=="__main__":
    app.run(host='0.0.0.0')