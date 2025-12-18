from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD']) 
def index():
    return render_template('index.html', title='Home Page') 


@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='เกี่ยวกับฉัน - About',
        name='Jagkrit',
        email='std.67122420301@ubru.ac.th',
        phone='094-291-2018'
    )


@app.route('/favorite/foods')
def favorite_foods():
    foods_list = ['ต้มยำ', 'ข้าวผัด', 'ข้าวมันไก่', 'หมูปิ้ง']
    return render_template('fav_foods.html', title='อาหารที่ชอบ', foods=foods_list)

@app.route('/favorite/sports')
def favorite_sports():
    sports_list = ['ฟุตบอล', 'บาสเกตบอล', 'แบดมินตัน', 'วอลเลย์บอล']
    return render_template('sports.html', title='กีฬาที่ชอบ', sports=sports_list)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title='ยินดีต้อนรับ')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>ไม่พบหน้านี้ (404)</h1><p>กรุณาตรวจสอบ URL อีกครั้ง</p>", 404

if __name__ == '__main__':
    
    app.run(debug=True)