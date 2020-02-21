from flask import Flask, request, render_template, session, redirect, url_for
import numpy as np
import pandas as pd
import sys

app = Flask('Zip Code Statistics')

df = pd.read_csv('./master_df.csv')

@app.route('/', methods=("POST", "GET")) #homepage
def home():
    return render_template('home.html')

@app.route('/submit') #submission page
def submit():
    user_input = request.args

    zip = user_input['zip']
    stats_zip = df[df['zip'] == int(zip)]

    try:
        if stats_zip['harvey_affected'].iloc[0] == 1:
            stats_zip = stats_zip[['zip', 'StateName', '2017 mean_median', '%_change_after_harvey'
            ]]
            sys.stdout.flush()

        elif stats_zip['dorian_affected'].iloc[0] == 1:
            stats_zip = stats_zip[['zip', 'StateName', '2019 mean_median', '%_change_after_dorian'
            ]]
            sys.stdout.flush()

        elif stats_zip['sandy_affected'].iloc[0] == 1:
            stats_zip = stats_zip[['zip', 'StateName', '2012 mean_median', '%_change_after_sandy'
            ]]
            sys.stdout.flush()

    except:
        print('exception!!!!!')
        sys.stdout.flush()

    return render_template('colors.html',
    tables=[stats_zip.to_html(classes='zip')]
    , titles=stats_zip
    )

@app.route('/data_frame', methods=("POST", "GET")) #raw df for reference
def html_table():

    return render_template('data_frame.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
