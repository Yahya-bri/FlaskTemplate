export FLASK_APP=app
export FLASK_ENV=development
export SECRET_KEY="your secret key"
export DATABASE_URI="sqlite:///project.db"
echo "export DATABASE_URI="postgresql://username:password@host:port/database_name""
clear
flask run
