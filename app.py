from flask import Flask, render_template, request, jsonify
import re
import pickle
model=pickle.load(open('clf1','rb'))
dict={1: 'Experience our unique culture where its all about technology and people empowerment,Send your resume to careers@changepond.com',
      2: 'linkedin https://www.linkedin.com/company/changepond/mycompany/ ,fackbook https://www.facebook.com/Changepond ,twitter https://twitter.com/changepondonweb',
      3: 'We are open 9am-9pm Monday-Friday!',
     4:'You can contact us at +91 44 47480000, +91 44 47480003,salesindia@changepond.com,https://www.changepond.com/contact',
     5: 'we provide services like Application Modernization,Enterprise Omni-channel Solutions,Hyper Automation,RPA,Integration Platform',
     6:'You can locate us at Changepond Technologies Pvt., Ltd.,H-2 SIPCOT IT Park, Old Mahabalipuram Road, Siruseri,Chennai 603 103,India',
     7:'Hi there, for better experince share your name and mail id',
     8: 'Talk to you later'}
def response(text):
    res=model.predict([text])
    res=res.item()
    res=dict[res]
    return res
keywords=['career','social media','contact','service','location','bye','others']
email=[]
def check_mail(text):
    if text in keywords:
        if text=='others':
            res= 'share your query to us in talktous@changepond.com'
        else:
            res=response(text)
    else:
        x=re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        if x==[]:
            print('no mail')
        else:
            email.append(x)
        if len(email)==0:
            res='please enter your mail id for better experience'
        else:
            res="""please enter the option regarding querry, 1) service 2) carrier 3) contact 4) location 5) social media 6) others """
    return(res)
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/get')
def get_bot_response():
    global seat_count
    mess = request.args.get('msg')
    res1=check_mail(mess)
    return(res1)
if __name__ == "__main__":
	app.run()
    
