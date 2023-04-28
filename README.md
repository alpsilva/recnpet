# recnpet

## How to run the backend locally

1. Change to backend directory
```sh
cd backend
```

2. Install dependencies
```sh
pip install -r requirements.txt
```

3. Create a .env file with a BD_URL field and a serviceAccountKey.json in the database folder. Ask the tech lead for these files, because the app will not run without them!

4. Run the server
```sh
uvicorn main:app --reload
```
