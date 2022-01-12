from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from sqlalchemy import desc

from model import db, seedData, Customer , Transaction, Account


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/Bank'
db.app = app
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/test")
def test():

    join= db.session.query(Customer, Account).join(Account).filter(Account.CustomerId==Customer.id).where(Customer.id == 1544).order_by(desc(Account.Balance)).all()
    hej = 2
    return render_template("test.html", join = join)

@app.route("/")
def startpage():
    #trendingCategories = Category.query.all()
    #trendingCategories=trendingCategories
    return render_template("index.html")

@app.route("/charts")
def charts():
    return render_template("pages/charts/chartjs.html")

@app.route("/forms")
def forms():
    return render_template("pages/forms/basic_elements.html")

@app.route("/tables")
def tables():
    return render_template("pages/tables/basic-table.html")

@app.route("/error404")
def error404():
    return render_template("pages/samples/error-404.html")

@app.route("/error500")
def error500():
    return render_template("pages/samples/error-500.html")

@app.route("/login")
def login():
    return render_template("pages/samples/login.html")

@app.route("/register")
def register():
    return render_template("pages/samples/register.html")


################### UI ELements #####################
@app.route("/buttons")
def buttons():
    return render_template("pages/ui-features/buttons.html")

@app.route("/dropdowns")
def dropdowns():
    return render_template("pages/ui-features/dropdowns.html")

@app.route("/typography")
def typography():
    return render_template("pages/ui-features/typography.html")

@app.route("/icons")
def icons():
    return render_template("pages/icons/mdi.html")

################### End Of UI ELements #####################


@app.route("/category/<id>")
def category(id):
    products = Product.query.all()
    return render_template("category.html", products=products)


if __name__ == "__main__":
    with app.app_context():
        upgrade()

    app.run(host="127.0.0.1", port=5000, debug=True)
    seedData(db)
