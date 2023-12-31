from distutils.log import debug
from flask import Flask, render_template
from yaml import emit
from flask_socketio import SocketIO
from PIL import Image
from io import BytesIO
from engine import *
import base64
import re
import copy
import time

app=Flask(__name__,template_folder='Templates',static_folder='static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")
queue=[]

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('input image')
def check(input):
    lock=0
    start=time.time()
    print('image_recieved')
    image_data = re.sub('^data:image/.+;base64,', '', input)
    try:
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        image = image.resize((320,240))
        image.save('f1.jpg')
        img_arr=copy.deepcopy(cv2.imread('f1.jpg'))
        print('test')
        ans=ReturnPose(img_arr)
        crc='Correction: '
        po='Pose: '+ans[0]
        for i in ans[1]:
            crc=crc+','+i
        print(ans)
        socketio.emit('Answer_Response',{'Pose':po[:-4]})
        socketio.emit('Answer_Response2',{'Pose2':crc})
    except Exception as e: 
        print('hi')
    end=time.time()
    print('Time is {}'.format(end-start))
    lock=0
if __name__=='__main__':
    socketio.run(app,debug=True)