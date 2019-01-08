import datetime
import calendar
from flask import Flask, render_template, request, redirect, url_for

from connection import session
from database_setup import FlashRecord

app = Flask(__name__)

@app.route('/')
def homepage():
    now = datetime.datetime.now()
    date = str(now.day)
    month = str(calendar.month_name[int(now.month)])[0:3]
    year = str(now.year)
    day = str(calendar.day_name[datetime.date.today().weekday()])[0:3]

    if date[0] != '0':
        date = '0' + date
    todays_date = ' '.join([day, month, date, year])
    entry = session.query(FlashRecord).filter_by(date = unicode(todays_date)).first()
    count = 0
    if entry:
        count = entry.times
    return render_template('homepage.html', count = count)

@app.route('/history')
def history():
    d = {}
    record = session.query(FlashRecord).all()
    for r in record:
        x = str(r.date)[4:]
        x = x[4:6] + ' ' + x[0:3] + ' ' + x[-4:]
        d[x] = r.times    
    keylist = d.keys()
    keylist.sort()
    return render_template('historypage.html',record = d, keylist = keylist)


@app.route('/', methods = ['POST'])
def get_javascript_data():
    date = str(request.form['date'])
    times = int(str(request.form['times']))
    newEntry = FlashRecord(date=date, times=times)

    entry = session.query(FlashRecord).filter_by(date=unicode(date)).first()
    if not entry:
        session.add(newEntry)
    else:
        entry.times = times
    session.commit()
    return redirect(url_for('homepage'))

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
