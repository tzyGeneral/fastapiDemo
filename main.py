from app import create_app

app = create_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
