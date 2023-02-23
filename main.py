from website import create_app

app = create_app()

if __name__ == '__main__': #only execute if we run this file, not import
    app.run(debug=True)


    