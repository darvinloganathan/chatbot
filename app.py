from flask import Flask, render_template, request, jsonify
import pickle
dict={1: 'Experience our unique culture where its all about technology and people empowerment,Send your resume to careers@changepond.com',
      2: 'linkedin https://www.linkedin.com/company/changepond/mycompany/ ,fackbook https://www.facebook.com/Changepond ,twitter https://twitter.com/changepondonweb',
      3: 'We are open 9am-9pm Monday-Friday!',
     4:'You can contact us at +91 44 47480000, +91 44 47480003,salesindia@changepond.com,https://www.changepond.com/contact',
     5: 'we provide services like Application Modernization,Enterprise Omni-channel Solutions,Hyper Automation,RPA,Integration Platform',
     6:'You can locate us at Changepond Technologies Pvt., Ltd.,H-2 SIPCOT IT Park, Old Mahabalipuram Road, Siruseri,Chennai â€“ 603 103,India',
     7:'Hi there how may i help you',
     8: 'Talk to you later'}
app = Flask(__name__)
model=pickle.load(open('clf1','rb'))
def response(text):
    res=model.predict([text])
    res=res.item()
    res=dict[res]
    return res
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/get')
def get_bot_response():
    global seat_count
    mess = request.args.get('msg')
    res=response(mess)
    return(res)
if __name__ == "__main__":
	app.run(debug=True)
    
