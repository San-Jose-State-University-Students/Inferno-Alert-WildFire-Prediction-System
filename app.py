from cmath import log
from fileinput import filename
from flask import Flask,request, url_for, redirect, render_template,jsonify
import pickle
from matplotlib.font_manager import json_dump
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/predict', methods=['POST'])
def predict_F():
    
    if request.method == 'POST':
        json_data = request.get_json()
        rain = float(json_data['rain'])
        temp = float(json_data['temp'])
        humidity = float(json_data['humidity'])
        wind = float(json_data['wind'])
       
        ffmc = get_ffmc(temp, rain, humidity, wind)
        dmc = get_dmc(rain, temp, humidity)
        dc = get_dc(rain, temp)
        isi = get_isi(wind, ffmc)
        bui  = get_bui(dc, dmc)
        fwi = get_fwi(bui, isi)

        model = pickle.load(open("model.pkl", 'rb'))
        #df = pd.DataFrame(isi, bui, fwi)
        list = [5, isi, bui, fwi]
        df = pd.DataFrame(list)
        df = df.T

        predict = model.predict(df)
        
        if predict == 0:
            message = {'predict':'Fire Not Possible'}
        else:
            message = {'predict':'Fire Possible'}


        return jsonify(message), 201



import math
import numpy as np
from numpy import log as ln


def get_fwi(bui, isi):
    if( bui <= 80):
        f_d = 0.626 * pow(bui, 0.809) + 2
    else:
        f_d = 1000/(25 + 108.64 * math.exp(-0.023 * bui))

    b = 0.1 * isi * f_d

    if(b >1):
        return math.exp(2.72 * pow(0.434 * ln(b), 0.647))
    
    return b

def get_bui(dc, dmc):
    if(dmc <= 0.4 * dc):
        return  (0.8 * dc*dmc)/(dmc + 0.4*dc)
    else:
        return dmc - (1 - (0.8 * dc) /(dmc + 0.4 * dc)) * (0.92 + pow(0.0114 * dmc, 1.7))


def get_isi(wind, ffmc):
    f_w = math.exp(0.05039 * wind)
    f_f = 91.9 * math.exp(-0.1386 * ffmc) * (1 + pow(ffmc, 5.31)/(4.93 * pow(10, 7)))
    return 0.208 * f_w * f_f

def get_dc(rain, temp):
    d_0 = 374.36
    r_d = 0.83 * rain -1.27
    q_o = 800* math.exp(-d_0/400)
    q_r = q_o + 3.937 * r_d
    d_r = 400 * ln(800/q_r)
    v = 0.36 * (temp + 2.8) + 3.8
    return d_0 + 0.5 * v

def get_dmc(rain, temp, humidity):
    p_o = 77.20
    r_e = 0.92 * rain - 1.27
    m_o = 20 + math.exp(5.6348 - p_o/43.43)
    if p_o <= 33:
        b= 100 /(0.5 + 0.3 * p_o)
    
    if p_o > 33 and p_o <= 65:
        b = 14- 1.3*ln(p_o)
    if p_o > 65:
        b = 6.2 * ln(p_o)
    
    m_r = m_o + 1000 * r_e / (48.77 + b* r_e)
    p_r = 244.72 - 43.43 * ln(m_r - 20)
    k = 1.894 * (temp + 1.1) * (100 - humidity) * 13.9 * pow(10, -6)

    return p_o + 100 * k

def get_ffmc(temp, rain, humidity, wind):

    m_o = 147.2 * (101 - 0)/(59.5)
    r_f = 0.1
    if(rain > 0.5):
        r_f = rain - 0.5
    if(m_o <= 150):
        m_r = m_o+ + 42.5*r_f * (math.exp(-100/(251 - m_o))) * (1 - math.exp(-6.93/r_f))
    else:
        m_r = m_o + 42.5 * r_f * (math.exp(-100/(251 - m_o))) * (1 - math.exp(-6.93/r_f)) + 0.0015 * (m_o - 150) ** 2 * pow(r_f, 0.5)

    if m_r > 250:
        m_r = 250
    
    e_d = 0.942 * pow(humidity, 0.679) + 11 * math.exp( (humidity - 100)/10) + 0.18 * (21.1 - temp) * (1 - math.exp(-0.115 * humidity))

    k_i = ( 0.424 * (1 - pow((100 -humidity)/100, 1.7))) + (0.0694 * pow(wind, 0.5) * (1 - pow((100 - humidity)/100, 8)))
    
    if( m_o > e_d):

        k_o = 0.424 * (1 - pow(humidity/100, 1.7)) + 0.0694 * pow(wind, 0.5) * (1 - pow(humidity/100, 8))
        k_d =  k_o * 0.581 * math.exp(0.0365 * temp)
        m = e_d + (m_o - e_d) * pow(10, -k_d)
    
    
    e_w = 0.618 * pow(humidity, 0.753) + 10 * math.exp( (humidity - 100)/10) + 0.18 * (21.1 - temp) * (1 - math.exp(-0.115 * humidity))

    if( m_o < e_w):
        k_w = k_i * 0.581 * math.exp(0.0365 * temp)
        m = e_w - (e_w - m_o) * pow(10, -k_w)

    return 59.5 * (250 - m)/(147.2 + m)


if __name__ == '__main__':
    app.run(debug=True)