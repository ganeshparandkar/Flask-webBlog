class Config:
    SECRET_KEY = '3d67f2e7f6ef66440b3551b7b714254c'  # this key will protect while modifying cookies and cross side request attacks 
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    #sending mail configurations
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #use environment variables here
    MAIL_USERNAME = 'hello2000love@gmail.com'
    MAIL_PASSWORD = 'ganesh0000'
